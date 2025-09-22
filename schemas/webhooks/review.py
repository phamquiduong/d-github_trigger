from enum import StrEnum

from schemas.base import WebhookRequestBase
from schemas.webhooks.github_user import GithubUser
from schemas.webhooks.pull_request import PullRequest


class State(StrEnum):
    APPROVED = 'approved'
    CHANGES_REQUESTED = 'changes_requested'
    COMMENTED = 'commented'


class Review(WebhookRequestBase):
    body: str | None
    html_url: str
    state: State


class ReviewHandler:
    def __init__(self, review: Review, sender: GithubUser, pull_request: PullRequest) -> None:
        self.review = review
        self.sender = sender
        self.pull_request = pull_request

    def build(self) -> str | None:
        body_pre = f'<pre>{self.review.body}</pre>' if self.review.body else ''
        return f'✅  {self.sender.as_html()} {self.review.state} {self.pull_request.as_html()}\n{body_pre}'
