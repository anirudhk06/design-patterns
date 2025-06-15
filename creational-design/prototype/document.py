from abc import ABC, abstractmethod
import copy


class DocumentPrototype(ABC):
    @abstractmethod
    def clone() -> "DocumentPrototype":
        pass


class Document(DocumentPrototype):
    def __init__(
        self,
        title: str,
        header: dict[str, str],
        body: list[str],
        footer: dict[str, str],
    ) -> None:
        self.title = title
        self.header = header
        self.body = body
        self.footer = footer

    def set_header(self, key, value):
        self.header[key] = value

    def set_body(self, value):
        self.body.append(value)

    def set_footer(self, key, value):
        self.footer[key] = value

    def clone(self) -> "DocumentPrototype":
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: title={self.title}, header={self.header}, body={self.body}, footer={self.footer}>"


def main() -> None:
    doc = Document(
        "A song of ice and fire",
        {"author": "G.R.R Martin"},
        ["Game Of thrones", "Fire & Blood"],
        {"copyright": "2025@gameofthrongs"},
    )

    clone = doc.clone()
    clone.set_header("logo", "got.png")
    clone.set_body("Dance of the dragon")
    clone.set_footer("copyright", "2024@iceandfire")

    print(doc)
    print(clone)


if __name__ == "__main__":
    main()
