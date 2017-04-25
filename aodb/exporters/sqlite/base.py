

import sqlite3

from typing import List

from .tables import CREATE_TABLES
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
            cursor.execute(CREATE_TABLES[table])

        self.conn.commit()

    def process_elements(self, parent):
        for child in parent:
            if child.tag == 'farmableitem':
                self.process_farmable_item(child)

            self.process_elements(child)

    def process_element(self, item, attrs_map):
        for attr in attr_mandatory:
            print(item.attrib[attr])

        for attr in attr_optional:
            if attr in item.attrib:
                print(item.attrib[attr])

    def process_farmable_item(self, item):
        """Processes and saves a Farmable Item."""


        # Mandatory attributes
        print(item.attrib['uniquename'])

        # Optional attributes

        print(item.attrib['activefarmactiondurationseconds'])
