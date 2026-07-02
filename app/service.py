from fastapi import HTTPException

from .store import url_store
from .utils import generate_code


class URLService:

    def create(self, url: str) -> str:
        while True:
            code = generate_code()

            if code not in url_store:
                break

        url_store[code] = url
        return code

    def get(self, code: str) -> str:
        if code not in url_store:
            raise HTTPException(status_code=404, detail="URL not found")

        return url_store[code]

    def list_urls(self):
        return [
            {
                "code": code,
                "original_url": url,
            }
            for code, url in url_store.items()
        ]