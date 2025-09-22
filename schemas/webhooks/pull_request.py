from abc import ABC, abstractmethod

from helpers.html import build_link
from schemas.base import WebhookRequestBase
from schemas.webhooks.github_user import GithubUser


class PullRequest(WebhookRequestBase):
    number: int
    title: str
    html_url: str
    merged: bool

    def as_html(self) -> str:
        html_link = build_link(link=self.html_url, display=f'PR#{self.number}')
        return f'<b>[{html_link} {self.title}]</b>'


class PullRequestHandlerBase(ABC):
    def __init__(self, pull_request: PullRequest, sender: GithubUser) -> None:
        self.pull_request = pull_request
        self.sender = sender

    @abstractmethod
    def build(self) -> str | None: ...


class PullRequestOpenedHandler(PullRequestHandlerBase):
    def build(self) -> str | None:
        return f'✨  {self.sender.as_html()} opened {self.pull_request.as_html()}'


class PullRequestClosedHandler(PullRequestHandlerBase):
    def build(self) -> str | None:
        if self.pull_request.merged is True:
            return f'🔀  {self.sender.as_html()} merged {self.pull_request.as_html()}'

        return f'❌  {self.sender.as_html()} closed {self.pull_request.as_html()}'


class PullRequestSynchronizeHandler(PullRequestHandlerBase):
    def build(self) -> str | None:
        return f'🔄  {self.sender.as_html()} updated {self.pull_request.as_html()}'
