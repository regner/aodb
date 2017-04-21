

import re

from abc import ABCMeta, abstractmethod
from xml.dom import minidom


class BaseExporter(metaclass=ABCMeta):
    """Base exporter class that implements common functionality between all exporters."""

    def __init__(self, input_file: str):
        """
        
        :param input_file: Location of the input file to be loaded.
        """

        self.input = None
        self.input_file = input_file

    @staticmethod
    def _clean_input(input: str) -> str:
        """Cleans the string that was loaded from the input file.
        
        :param input: The raw string from the source file to be cleaned.
        """

        pattern = re.compile(r'string m_Script = "(.*)"\n 1 string')
        search = re.search(pattern, input)

        dirty_xml = search.group(1)

        clean_xml = re.sub(r'\\r\\n\s*', '', dirty_xml)
        clean_xml = re.sub(r'\\n\s*', '', clean_xml)

        parsed_xml = minidom.parseString(clean_xml)
        pretty_xml = parsed_xml.toprettyxml(indent='\t')

        return pretty_xml

    def _load_input(self):
        """Loads and caches the input file specified when originally instantiated."""
        if self.input is None:
            with open(self.input_file) as in_file:
                raw_input = in_file.read()

            self.input = self._clean_input(raw_input)

    @abstractmethod
    def _generate_export(self, export_file: str):
        """The business logic of each exporter. Assume self._load_input has been run."""

    def genreate_export(self, export_file: str):
        """Generates the actual export.
        
        :param export_file: String location for where to save the file. Importantly the string
        must contain the Python format syntax so each exporter can set the file extension. For
        example a valid input would be `exports/items.{}`.
        """
        self._load_input()
        self._generate_export(export_file)
