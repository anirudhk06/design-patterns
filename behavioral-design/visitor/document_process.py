from abc import ABC, abstractmethod
from typing import List


class DocumentElament(ABC):
    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError("Sub classes must be implement accept() method.")


class TextBlock(DocumentElament):
    def __init__(self, text: str):
        self.text = text

    def accept(self, visitor: "DocumentVisitor"):
        visitor.visit_text_block(self)


class ImageBlock(DocumentElament):
    def __init__(self, url):
        self.url = url

    def accept(self, visitor: "DocumentVisitor"):
        visitor.visit_image_block(self)


class TableBlock(DocumentElament):
    def __init__(self, rows: List[List[str]]):
        self.rows = rows

    def accept(self, visitor: "DocumentVisitor"):
        visitor.visit_table_block(self)


class DocumentVisitor(ABC):
    @abstractmethod
    def visit_text_block(self, element):
        raise NotImplementedError(
            "Sub classes must be implement visit_text_block() method."
        )

    @abstractmethod
    def visit_image_block(self, element):
        raise NotImplementedError(
            "Sub classes must be implement visit_image_block() method."
        )

    @abstractmethod
    def visit_table_block(self, element):
        raise NotImplementedError(
            "Sub classes must be implement visit_table_block() method."
        )


class HTMLExportVisitor(DocumentVisitor):
    def __init__(self):
        self.output = []

    def visit_text_block(self, element: TextBlock):
        self.output.append(f"<p>{element.text}</p>")

    def visit_image_block(self, element: ImageBlock):
        self.output.append(f'<img src="{element.url}" />')

    def visit_table_block(self, element: TableBlock):
        self.output.append("<table>")
        for row in element.rows:
            self.output.append("<tr>")
            for cell in row:
                self.output.append(f"<td>{cell}</td>")
            self.output.append("</tr>")
        self.output.append("</table>")

    def get_html(self) -> str:
        return "\n".join(self.output)


class MarkdownExportVisitor(DocumentVisitor):
    def __init__(self):
        self.output = []

    def visit_text_block(self, element: TextBlock):
        self.output.append(element.text)

    def visit_image_block(self, element: ImageBlock):
        self.output.append(f"![image]({element.url})")

    def visit_table_block(self, element: TableBlock):
        if not element.rows:
            return

        headers = element.rows[0]
        separator = ["---"] * len(headers)

        self.output.append("| " + " | ".join(headers) + " |")
        self.output.append("| " + " | ".join(separator) + " |")

        for row in element.rows[1:]:
            self.output.append("| " + " | ".join(row) + " |")

    def get_markdown(self) -> str:
        return "\n".join(self.output)


class WordCountVisitor(DocumentVisitor):
    def __init__(self):
        self.count = 0

    def visit_text_block(self, element: TextBlock):
        self.count += len(element.text.split())

    def visit_image_block(self, element: ImageBlock):
        pass  # images have no words

    def visit_table_block(self, element: TableBlock):
        for row in element.rows:
            for cell in row:
                self.count += len(cell.split())


class Document:
    def __init__(self, elements: List[DocumentElament]):
        self.elements = elements

    def accept(self, visitor: DocumentVisitor):
        for doc in self.elements:
            doc.accept(visitor)


def main():
    doc = Document(
        [
            ImageBlock(),
            TableBlock(),
            TextBlock(),
        ]
    )

    html_visitor = HTMLExportVisitor()
    doc.accept(html_visitor)

    print(html_visitor.output)
