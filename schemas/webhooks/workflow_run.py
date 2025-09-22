from enum import StrEnum

from helpers.html import build_link
from schemas.base import WebhookRequestBase


class Status(StrEnum):
    REQUESTED = 'requested'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    QUEUED = 'queued'
    PENDING = 'pending'
    WAITING = 'waiting'


class Conclusions(StrEnum):
    ACTION_REQUIRED = 'action_required'
    CANCELLED = 'cancelled'
    FAILURE = 'failure'
    NEUTRAL = 'neutral'
    SKIPPED = 'skipped'
    STALE = 'stale'
    SUCCESS = 'success'
    TIMED_OUT = 'timed_out'
    STARTUP_FAILURE = 'startup_failure'
    NULL = 'null'


class WorkFlowRun(WebhookRequestBase):
    id: int
    name: str
    html_url: str
    status: Status
    conclusion: Conclusions

    def as_html(self) -> str:
        html_link = build_link(self.html_url, f'Workflow#{self.id}')
        return f'<b>[{html_link} {self.name}]</b>'


class WorkflowRunHandler:
    def __init__(self, workflow_run: WorkFlowRun) -> None:
        self.workflow_run = workflow_run

    def run(self) -> str | None:
        if self.workflow_run.status == Status.COMPLETED:
            html_display = self.workflow_run.as_html()

            if self.workflow_run.conclusion == Conclusions.SUCCESS:
                return f'✅  {html_display} run success'

            if self.workflow_run.conclusion == Conclusions.FAILURE:
                return f'❌  {html_display} run fail'

        return None
