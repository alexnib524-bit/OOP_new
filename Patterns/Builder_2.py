from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import json


@dataclass
class HttpRequest:
    method: str
    url: str
    headers: dict[str, str] = field(default_factory=dict)
    body: str = ""
    timeout: int = 30

    def __str__(self) -> str:
        body_preview = self.body[:50] + "..." if len(self.body) > 50 else self.body
        return (
            f"{self.method} {self.url}\n"
            f"Headers: {self.headers}\n"
            f"Body: {body_preview}\n"
            f"Timeout: {self.timeout}s"
        )


class HttpRequestBuilder:
    def __init__(self):
        self._method = ""
        self._url = ""
        self._headers = {}
        self._body = ""
        self._timeout = 30
    
    def set_method(self, method: str):
        self._method = method
        return self
    
    def set_url(self, url: str):
        self._url = url
        return self
    
    def add_header(self, key: str, value: str):
        self._headers[key] = value
        return self
    
    def set_body(self, body: str):
        self._body = body
        return self
    
    def set_timeout(self, timeout: int):
        self._timeout = timeout
        return self
    
    def build(self) -> HttpRequest:
        return HttpRequest(
            method=self._method,
            url=self._url,
            headers=self._headers,
            body=self._body,
            timeout=self._timeout
        )


class Director:
    def __init__(self, builder: HttpRequestBuilder):
        self._builder = builder
    
    def build_json_post(self, url: str, data: dict) -> HttpRequest:
        return (self._builder
                .set_method("POST")
                .set_url(url)
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(data))
                .set_timeout(30)
                .build())
    
    def build_auth_get(self, url: str, token: str) -> HttpRequest:
        return (self._builder
                .set_method("GET")
                .set_url(url)
                .add_header("Authorization", f"Bearer {token}")
                .set_timeout(15)
                .build())
    
    def build_multipart_upload(self, url: str, filename: str) -> HttpRequest:
        return (self._builder
                .set_method("POST")
                .set_url(url)
                .add_header("Content-Type", "multipart/form-data")
                .set_body(f"file={filename}")
                .set_timeout(60)
                .build())


# Ожидаемый клиентский код:
director = Director(HttpRequestBuilder())
request = director.build_json_post("https://api.example.com/orders", {"item": "book"})
print(request)