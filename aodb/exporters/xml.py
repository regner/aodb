

from xml.dom import minidom

from .base import BaseExporter


class XMLExporter(BaseExporter):
    def _generate_export(self):
        export_file = self.export_file.format('xml')

        with open(export_file, 'w') as out_file:
            parsed_xml = minidom.parseString(self.input)
            pretty_xml = parsed_xml.toprettyxml(indent='\t')

            out_file.write(pretty_xml)
