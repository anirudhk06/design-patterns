from typing import Type, List, Dict, Any, Optional
import csv
import json


class DataExporter:
    def export(self, *args, **kwargs) -> None:
        raise NotImplementedError("Subclasses must be implemented the export method.")


class JSONExporter(DataExporter):
    def export(
        self, data: List[Dict] = None, file_path: Optional[str] = "output.json"
    ) -> None:
        if not data or len(data) == 0:
            raise ValueError("Empty data.")

        if not isinstance(data, list) or not isinstance(data[0], dict):
            raise TypeError("Invaid Type: data must be a list of dict.")

        file_path: str = "output.json"
        with open(file_path, mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)


class CSVExporter(DataExporter):
    def export(
        self, data: List[Dict] = None, file_path: Optional[str] = "output.csv"
    ) -> None:
        if not data or len(data) == 0:
            raise ValueError("Empty data.")

        if not isinstance(data, list) or not isinstance(data[0], dict):
            raise TypeError("Invaid Type: data must be a list of dict.")

        file_path: str = "output.csv"

        with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = data[0].keys()

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


class XMLExporter(DataExporter):
    def export(self, data: List[Dict], file_path: Optional[str] = "output.xml") -> None:
        if not data or len(data) == 0:
            raise ValueError("Empty data.")

        if not isinstance(data, list) or not isinstance(data[0], dict):
            raise TypeError("Invaid Type: data must be a list of dict.")

        file_path: str = "output.xml"

        xml_string = self.dict_list_to_xml(data)
        with open(file_path, "w", encoding="utf-8") as xmlfile:
            xmlfile.write(xml_string)

    def dict_list_to_xml(
        self,
        data: List[Dict],
        root_tag="data",
        item_tag="item",
    ) -> str:
        xml: List = [f"<{root_tag}>"]
        for entry in data:
            xml.append(f"  <{item_tag}>")
            for key, value in entry.items():
                xml.append(f"    <{key}>{value}</{key}>")
            xml.append(f"  </{item_tag}>")
        xml.append(f"</{root_tag}>")
        return "\n".join(xml)


class ExporterFactory:
    _methods: dict[str, Type[DataExporter]] = {
        "json": JSONExporter,
        "csv": CSVExporter,
        "xml": XMLExporter,
    }

    @staticmethod
    def get_exporter(format: str = None) -> DataExporter:
        clean_format: str = str(format).lower().strip()

        if clean_format not in ExporterFactory._methods:
            raise ValueError(
                f"Invalid method of {format}. Supported formats are {', '.join(
                key for key in ExporterFactory._methods.keys()
            )}"
            )

        return ExporterFactory._methods[clean_format]()


def main() -> None:
    data: List[Dict[str, Any]] = [
        {"name": "Anirudh", "age": 25, "city": "Kochi"},
        {"name": "Rahul", "age": 28, "city": "Trivandrum"},
        {"name": "Sneha", "age": 22, "city": "Calicut"},
    ]
    exporter: DataExporter = ExporterFactory.get_exporter("xml")
    exporter.export(data)


if __name__ == "__main__":
    main()
