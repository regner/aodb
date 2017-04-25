

from .base import BaseSQLiteExporter
from .tables import TN_FarmableItems


class SQLiteExporterItems(BaseSQLiteExporter):
    def _generate_export(self):
        tables = [
            TN_FarmableItems,
        ]

        self.init_db(tables)
