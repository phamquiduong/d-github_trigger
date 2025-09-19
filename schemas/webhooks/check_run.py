from enum import StrEnum

from pydantic import HttpUrl

from schemas.base import WebhookRequestBase


class PullRequest(WebhookRequestBase):
    id: int
    url: HttpUrl

    @property
    def html_url(self) -> HttpUrl:
        parts = str(self.url).split('/')
        owner, repo, pr_number = parts[-4], parts[-3], parts[-1]
        html_url = f'https://github.com/{owner}/{repo}/pull/{pr_number}'
        return HttpUrl(html_url)

    def as_html(self):
        return f'[<a href="{self.html_url}">PR#{self.id}</a>]'


class Conclusions(StrEnum):
    SUCCESS = 'success'
    FAILURE = 'failure'


class CheckRun(WebhookRequestBase):
    id: int
    name: str
    html_url: HttpUrl
    conclusion: Conclusions
    pull_requests: list[PullRequest]

    def as_html(self):
        return f'[<a href="{self.html_url}">Action#{self.id}</a>: <b>{self.name}</b>]'
