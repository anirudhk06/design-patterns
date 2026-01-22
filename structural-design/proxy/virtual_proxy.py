from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def show(self):
        pass


class RealDocument(Document):
    def __init__(self, filename: str):
        print(f"[INIT] loading document: {filename}")
        self.filename = filename

    def show(self):
        print(f"[SHOW] Displaying document: {self.filename}")


class DocumentProxy(Document):

    def __init__(self, filename: str):
        self._document: RealDocument | None = None
        self.filename = filename

    def show(self):
        if not self._document:
            self._document = RealDocument(self.filename)
        self._document.show()


def main() -> None:
    doc = DocumentProxy("report.pdf")
    print("Document created")

    doc.show()
    doc.show()


if __name__ == "__main__":
    main()
