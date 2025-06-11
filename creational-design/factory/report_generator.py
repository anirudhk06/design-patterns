from typing import Type, Any


class ReportService:
    def generate(self, *args, **kwargs) -> None:
        raise NotImplemented("Subclasses must implemented genrate method")


class PDFReport(ReportService):
    def generate(self, data: dict[str, Any]) -> None:
        print(f"Generating PDF report with {len(data)} records.")


class ExcelReport(ReportService):
    def generate(self, data: dict[str, Any]) -> None:
        print(f"Generating Excel report with {len(data)} records.")


class TextReport(ReportService):
    def generate(self, data: dict[str, Any]) -> None:
        print(f"Generating Text report with {len(data)} records.")


class ReportFactory:
    _methods: dict[str, Type[ReportService]] = {
        "pdf": PDFReport,
        "excel": ExcelReport,
        "text": TextReport,
    }

    @staticmethod
    def get_report(method: str = "") -> ReportService:
        clean_method = str(method).strip().lower()

        if clean_method not in ReportFactory._methods:
            raise ValueError(
                f"Invalid method of '{method}'.  Supported types: pdf, excel, text."
            )

        return ReportFactory._methods[clean_method]()


def main() -> None:
    report_generator = ReportFactory()
    report = report_generator.get_report("pdf")

    data = {
        "sales": [150, 200, 250],
        "region": ["North", "South", "East"],
    }
    report.generate(data)


if __name__ == "__main__":
    main()
