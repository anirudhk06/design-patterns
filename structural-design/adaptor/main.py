from abc import ABC, abstractmethod


class AnalyticsTool(ABC):
    @abstractmethod
    def analyse_data(self):
        raise NotImplementedError("Sub classes must be implement analyse_data() method")


class JSONAnalyticsTool(AnalyticsTool):
    def __init__(self, json_data: str):
        self.json_data = json_data

    def analyse_data(self):
        print(f"Analysing JSON Data: {self.json_data}")


class XMLAnalyticsTool:
    def __init__(self, xml_data: str):
        self.xml_data = xml_data

    def get_xml_data(self) -> str:
        return self.xml_data


class XMLAdaptor(AnalyticsTool):
    def __init__(self, xml_tool: XMLAnalyticsTool):
        self.xml_tool = xml_tool

    def analyse_data(self):
        print(f"Analysing XML Data: {self.xml_tool.get_xml_data()}")


class Client:
    def process_data(self, tool: AnalyticsTool):
        tool.analyse_data()


def main() -> None:
    json_analytic_tool = JSONAnalyticsTool("JSON Data")
    xml_data = XMLAdaptor(XMLAnalyticsTool("XML Data"))
    client = Client()
    client.process_data(xml_data)


if __name__ == "__main__":
    main()
