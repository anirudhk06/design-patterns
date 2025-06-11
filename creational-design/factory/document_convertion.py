from typing import Type


class DocumentConverter:
    def convert(self, *args, **kwargs) -> None:
        raise NotImplementedError("Subclasses must be implemented convert method.")


class DocxToPdfConverter(DocumentConverter):
    def convert(self, content: str = "") -> str:
        return f"Converted DOCX to PDF. Length: {len(content)}"


class MarkdownToHtmlConverter(DocumentConverter):
    def convert(self, content: str = "") -> str:
        return f"Converted MARKDOWN to HTML. Length: {len(content)}"


class DocxToTextConverter(DocumentConverter):
    def convert(self, content: str = "") -> str:
        return f"Converted DOCX to TEXT. Length: {len(content)}"


class DocumentConverterFactory:
    _methods: dict[str, Type[DocumentConverter]] = {
        "docx_to_pdf": DocxToPdfConverter,
        "markdown_to_html": MarkdownToHtmlConverter,
        "docx_to_text": DocxToTextConverter,
    }

    @staticmethod
    def get_converter(method: str = "") -> DocumentConverter:
        cleaned_method: str = str(method).lower().strip()

        if cleaned_method not in DocumentConverterFactory._methods:
            raise ValueError(
                f"Invalid method of '{method}'. Supported methods {', '.join([key for key in DocumentConverterFactory._methods.keys()])}"
            )

        return DocumentConverterFactory._methods[cleaned_method]()


def main() -> None:
    converter = DocumentConverterFactory.get_converter("markdown_to_html")
    result = converter.convert("# Hello Markdown")
    print(result)


if __name__ == "__main__":
    main()
