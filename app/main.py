from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .schemas import (
    ShortenRequest,
    ShortenResponse,
)
from .service import URLService

app = FastAPI(title="URL Shortener")

service = URLService()


@app.post("/shorten", response_model=ShortenResponse)
def shorten(request: ShortenRequest):

    code = service.create(str(request.url))

    return {
        "code": code,
        "short_url": f"http://localhost:8000/{code}",
    }


@app.get("/{code}")
def redirect(code: str):

    url = service.get(code)

    return RedirectResponse(url)


@app.get("/urls")
def list_urls():
    return service.list_urls()


@app.get("/info/{code}")
def get_info(code: str):

    return {
        "code": code,
        "original_url": service.get(code),
    }