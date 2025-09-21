from helpers.html import build_link
from schemas.base import WebhookRequestBase


class GithubUser(WebhookRequestBase):
    name: str | None
    login: str
    html_url: str

    def as_html(self) -> str:
        return build_link(link=self.html_url, display=self.name or self.login)
