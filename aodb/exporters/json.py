

from json import dump
from xmljson import gdata
from xml.etree.ElementTree import fromstring

from .base import BaseExporter


class JsonExporter(BaseExporter):
    def _generate_export(self, export_file: str):
        export_file = export_file.format('json')

        clean = self.input.replace(
            ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="Items.xsd"',
            '',
            1
        )

        json = gdata.data(fromstring(clean))

        with open(export_file, 'w') as out_file:
            dump(json, out_file, indent=4)
