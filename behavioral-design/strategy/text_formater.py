from abc import ABC, abstractmethod


class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str: ...


class PlainTextFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text


class MarkdownFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return f"**{text}**"


class HTMLFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return f"<p>{text}</p>"


class Document:
    def __init__(self, document: str, formatter: TextFormatter = None) -> None:
        self.doc = document
        self.formatter = formatter

    def format(self) -> str:
        if self.formatter is None or not isinstance(self.formatter, TextFormatter):
            raise ValueError("Invalid formatter")
        return self.formatter.format(self.doc)

    def set_formatter(self, format: TextFormatter) -> None:
        if not isinstance(format, TextFormatter):
            raise ValueError("Invalid formatter")
        self.formatter = format


def main() -> None:
    doc = Document("Hello World")

    doc.set_formatter(PlainTextFormatter())
    print(doc.format())


if __name__ == "__main__":
    main()
