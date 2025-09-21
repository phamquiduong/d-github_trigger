from schemas.webhooks.request import Actions, WebhookRequest
from schemas.webhooks.workflow_run import WorkflowRunHandler


class Build:
    def __init__(self, webhook_request: WebhookRequest) -> None:
        self.request = webhook_request

    def run(self) -> str | None:
        # Workflow handler
        if self.request.action == Actions.COMPLETED and self.request.workflow_run:
            return WorkflowRunHandler(self.request.workflow_run).run()

        return None
