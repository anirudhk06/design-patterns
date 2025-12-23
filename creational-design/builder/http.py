from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass(frozen=True)
class Request:
    url: str
    method: str
    headers: Dict[str, str] = field(default_factory=dict)
    query_params: Dict[str, str] = field(default_factory=dict)
    body: Any = None
    timeout: int = 60


class HttpRequestBuilder:
    def __init__(self):
        self._url = None
        self._method = None
        self._headers = {}
        self._query_params = {}
        self._body = None
        self._timeout = 60

    def set_url(self, url: str):
        if not url.strip():
            raise ValueError("URL must not be empty")
        self._url = url
        return self

    def set_method(self, method: str):
        allowed = {"GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"}
        if method not in allowed:
            raise ValueError("Invalid HTTP method")
        self._method = method
        return self

    def add_header(self, key: str, value: str):
        self._headers[key] = value
        return self

    def add_query_param(self, key: str, value: str):
        self._query_params[key] = value
        return self

    def set_body(self, body):
        self._body = body
        return self

    def set_timeout(self, timeout: int):
        self._timeout = timeout
        return self

    def build(self) -> Request:
        if not self._url or not self._method:
            raise ValueError("URL and Method are required")

        return Request(
            url=self._url,
            method=self._method,
            headers=self._headers,
            query_params=self._query_params,
            body=self._body,
            timeout=self._timeout,
        )

request = (
    HttpRequestBuilder()
    .set_url("https://api.example.com")
    .set_method("POST")
    .add_header("Authorization", "Bearer token")
    .add_query_param("page", "1")
    .set_body({"name": "Anirudh"})
    .set_timeout(30)
    .build()
)
