import pyshorteners


class LinkShortener:

    def short(self, long_url: str) -> str:
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(long_url)
        return short_url
