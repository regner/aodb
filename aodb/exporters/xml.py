

from .base import BaseExporter


class XmlExporter(BaseExporter):
    def _generate_export(self, export_file: str):
        export_file = export_file.format('xml')

        with open(export_file, 'w') as out_file:
            out_file.write(self.input)
