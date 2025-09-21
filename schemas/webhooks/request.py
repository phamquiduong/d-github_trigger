from enum import StrEnum

from schemas.base import WebhookRequestBase
from schemas.webhooks.check_run import CheckRun
from schemas.webhooks.workflow_run import WorkFlowRun


class Actions(StrEnum):
    COMPLETED = 'completed'


class WebhookRequest(WebhookRequestBase):
    action: Actions | None = None
    check_run: CheckRun | None = None
    workflow_run: WorkFlowRun | None = None
