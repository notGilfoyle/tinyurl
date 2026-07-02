from dataclasses import dataclass


@dataclass
class URL:
    code: str
    original_url: str