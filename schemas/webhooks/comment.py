import html

from schemas.base import WebhookRequestBase
from schemas.webhooks.github_user import GithubUser
from schemas.webhooks.pull_request import PullRequest


class Comment(WebhookRequestBase):
    path: str
    position: int
    body: str


class CommentHandler:
    def __init__(self, comment: Comment, sender: GithubUser, pull_request: PullRequest) -> None:
        self.comment = comment
        self.sender = sender
        self.pull_request = pull_request

    def build(self) -> str | None:
        return (
            f'{self.sender.as_html()} comment in {self.pull_request.as_html()}\n'
            f'<pre>{self.comment.path}:{self.comment.position}</pre>\n'
            f'<pre>{html.escape(self.comment.body)}</pre>'
        )
