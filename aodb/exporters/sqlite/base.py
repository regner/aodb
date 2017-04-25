

import sqlite3

from typing import List

from . import const_tables
from ..base import BaseExporter


class BaseSQLiteExporter(BaseExporter):
    def __init__(self, input_file: str, export_file: str):
        super().__init__(input_file, export_file)

        beginning = export_file.split('-')[0]
        ending = export_file.split('.')[-1]

        self.export_file = f'{beginning}.{ending}'
        self.conn = None

    def init_db(self, tables: List[str]):
        file = self.export_file.format('db')

        self.conn = sqlite3.connect(file)
        cursor = self.conn.cursor()

        for table in tables:
            cursor.execute(const_tables.CREATE_TABLES[table])

        self.conn.commit()

    def execute_sql(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

    def process_elements(self, parent):
        for child in parent:
            if child.tag == 'farmableitem':
                self.process_farmable_item(child)

    @staticmethod
    def attributes_to_sql(element, columns=None, values=None):
        if columns is None:
            columns = ''

        if values is None:
            values = ''

        for k, v in element.attrib.items():
            columns += f'{k},'
            values += f'"{v}",'

        columns = columns.strip(',')
        values = values.strip(',')

        return columns, values

    def process_farmable_item(self, item):
        """Processes and saves a Farmable Item."""
        columns, values = self.attributes_to_sql(item)
        sql = f'INSERT INTO {const_tables.TN_FarmableItems} ({columns}) VALUES ({values});'

        self.execute_sql(sql)
