from enum import StrEnum

from schemas.base import WebhookRequestBase
from schemas.webhooks.check_run import CheckRun


class Actions(StrEnum):
    COMPLETED = 'completed'


class WebhookRequest(WebhookRequestBase):
    action: Actions | None = None
    check_run: CheckRun | None = None
