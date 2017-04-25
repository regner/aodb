

import sqlite3

from typing import List

from .tables import CREATE_TABLES
from ..base import BaseExporter


class BaseSQLiteExporter(BaseExporter):
    def __init__(self, input_file: str, export_file: str):
        super().__init__(input_file, export_file)

        self.db = None

    def init_db(self, tables: List[str]):
        file = self.export_file.format('db')

        conn = sqlite3.connect(file)
        cursor = conn.cursor()

        for table in tables:
            cursor.execute(CREATE_TABLES[table])

        conn.commit()
