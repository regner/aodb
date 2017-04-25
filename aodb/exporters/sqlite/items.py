

from . import const_tables
from .base import BaseSQLiteExporter


class SQLiteExporterItems(BaseSQLiteExporter):
    def _generate_export(self):
        tables = [
            const_tables.TN_FarmableItems,
            const_tables.TN_StackableItems,
        ]

        self.init_db(tables)
        self.process_elements(self.get_xml_root())
