from enum import StrEnum

from schemas.base import WebhookRequestBase
from schemas.webhooks.github_user import GithubUser
from schemas.webhooks.pull_request import PullRequest
from schemas.webhooks.workflow_run import WorkFlowRun


class Actions(StrEnum):
    COMPLETED = 'completed'
    OPENED = 'opened'
    CLOSED = 'closed'


class WebhookRequest(WebhookRequestBase):
    action: Actions | None = None
    workflow_run: WorkFlowRun | None = None
    pull_request: PullRequest | None = None
    sender: GithubUser | None = None
