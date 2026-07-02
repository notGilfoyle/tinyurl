from app.service import URLService


def test_create_url():

    service = URLService()

    code = service.create("https://google.com")

    assert isinstance(code, str)
    assert len(code) == 6


def test_lookup():

    service = URLService()

    code = service.create("https://github.com")

    assert service.get(code) == "https://github.com"