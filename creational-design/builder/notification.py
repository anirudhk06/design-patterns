from typing import Optional
import re


def valid_email(email: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))


class Notification:
    def __init__(self, builder) -> None:
        self.sender = builder.sender
        self.receiver = builder.receiver
        self.subject = builder.subject
        self.template_path = builder.template_path
        self.content = builder.content

    def send(self) -> None:
        print(f"{self.sender} -> {self.receiver} email send seccessfully")
        return


class NotificationBuilder:
    def __init__(self) -> None:
        self.sender = None
        self.receiver = None
        self.subject = None
        self.template_path = None
        self.content = None

    def set_sender(self, email: str):
        if not email:
            raise ValueError("Please submit the sender email.")

        if not valid_email(email):
            raise ValueError("Invalid email address.")

        self.sender = email
        return self

    def set_receiver(self, email: str):
        if not email:
            raise ValueError("Please submit the receiver email.")

        if not valid_email(email):
            raise ValueError("Invalid email address.")

        self.receiver = email
        return self

    def set_subject(self, subject: str):
        self.subject = subject

        return self

    def set_template_path(self, path: str):
        self.template_path = path
        return self

    def set_content(self, content: dict):
        if not self.template_path:
            raise ValueError(
                "Cannot set content: no template path provided. Use `set_template_path()` first."
            )

        self.content = content
        return self

    def build(self) -> Notification:
        if not self.subject:
            self.subject = "Eventxpro"

        if not self.path:
            self.path = "/email/email.html"

        notifier = Notification(self)
        self.__init__()
        return notifier


def main() -> None:
    notification = (
        NotificationBuilder()
        .set_sender("anirudh@gmail.com")
        .set_receiver("mitsuha@gmail.com")
        .build()
    )
    notification.send()


if __name__ == "__main__":
    main()
