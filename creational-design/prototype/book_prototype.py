from typing import List
from abc import ABC, abstractmethod
import copy


class BookPrototype(ABC):
    @abstractmethod
    def clone(self) -> "BookPrototype":
        pass


class Book(BookPrototype):
    def __init__(self, title: str, author: str, chapters: List[str]) -> None:
        self.title = title
        self.author = author
        self.chapters = chapters

    def add_chapter(self, chapter: str) -> None:
        self.chapters.append(chapter)

    def clone(self) -> "Book":
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: title={self.title}, author={self.author}, chapters={self.chapters}>"


def main() -> None:
    book = Book("A Song of Ice and Fire", "G.R.R Martin", ["Winterfall", "Long Night"])
    clone_book = book.clone()
    clone_book.author = "Anirudh k"

    print(book)
    print(clone_book)


if __name__ == "__main__":
    main()
