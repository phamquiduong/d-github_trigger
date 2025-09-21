from helpers.html import build_link
from schemas.base import WebhookRequestBase
from schemas.webhooks.github_user import GithubUser


class PullRequest(WebhookRequestBase):
    number: int
    title: str
    html_url: str

    def as_html(self) -> str:
        html_link = build_link(link=self.html_url, display=f'PR#{self.number}')
        return f'[{html_link} {self.title}]'


class PullRequestOpenedHandler:
    def __init__(self, pull_request: PullRequest, sender: GithubUser) -> None:
        self.pull_request = pull_request
        self.sender = sender

    def build(self) -> str | None:
        return f'✨  {self.sender.as_html()}  opened  {self.pull_request.as_html}'
