from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    @abstractmethod
    def search(self, text: str, query: str) -> bool: ...


class CaseSensitiveSearch(SearchStrategy):
    def search(self, text: str, query: str) -> bool:
        return query in text


class CaseInsensitiveSearch(SearchStrategy):
    def search(self, text: str, query: str) -> bool:
        return query.lower() in text.lower()


class WholeWordSearch(SearchStrategy):
    def search(self, text: str, query: str) -> bool:
        return query.lower() in text.lower().split(" ")


class TextSearcher:
    def __init__(self, strategy: SearchStrategy = None) -> None:
        if not isinstance(strategy, SearchStrategy):
            raise ValueError("Invalid search strategy")

        self.strategy = strategy

    def find(self, text: str, query: str) -> bool:
        text, query = str(text).strip(), str(query).strip()
        if not text or not query:
            return False
        return self.strategy.search(str(text), str(query))

    def set_strategy(self, strategy: SearchStrategy) -> None:
        if not isinstance(strategy, SearchStrategy):
            raise ValueError("Invalid search strategy")

        self.strategy = strategy


def main() -> None:
    searcher = TextSearcher(WholeWordSearch())
    print(searcher.find("Hello world", "Hello"))

    searcher.set_strategy(CaseSensitiveSearch())
    print(searcher.find("Hello world", "hello"))

    searcher.set_strategy(CaseInsensitiveSearch())
    print(searcher.find("Hello world", "hello"))


if __name__ == "__main__":
    main()
