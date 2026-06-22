from dataclasses import dataclass


@dataclass
class Document:
    file_name: str
    content: str