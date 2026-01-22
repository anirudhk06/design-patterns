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


class User:
    def __init__(self, username: str, is_admin: bool):
        self.username = username
        self.is_admin = is_admin


class SecureDocumentProxy(Document):
    def __init__(self, filename: str, user: User):
        self._real_document = None
        self.filename = filename
        self.user = user

    def show(self):
        if not self.user.is_admin:
            print("Access denied")
            return

        if self._real_document is None:
            self._real_document = RealDocument(self.filename)

        self._real_document.show()


def main() -> None:
    admin = User("alice", True)
    guest = User("bob", False)

    doc = SecureDocumentProxy("secret.pdf", admin)
    doc.show()

    doc2 = SecureDocumentProxy("secret.pdf", guest)
    doc2.show()


if __name__ == "__main__":
    main()
