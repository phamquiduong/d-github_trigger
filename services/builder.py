from schemas.webhooks.pull_request import (PullRequestClosedHandler, PullRequestOpenedHandler,
                                           PullRequestSynchronizeHandler)
from schemas.webhooks.request import Actions, WebhookRequest
from schemas.webhooks.review import ReviewHandler
from schemas.webhooks.workflow_run import WorkflowRunHandler


class Build:
    def __init__(self, webhook_request: WebhookRequest) -> None:
        self.request = webhook_request

    def run(self) -> str | None:
        # Workflow handler
        if self.request.action == Actions.COMPLETED and self.request.workflow_run:
            return WorkflowRunHandler(self.request.workflow_run).run()

        if self.request.pull_request and self.request.sender:
            # Pull request opened handler
            if self.request.action == Actions.OPENED:
                return PullRequestOpenedHandler(self.request.pull_request, self.request.sender).build()

            # Pull request closed handler
            if self.request.action == Actions.CLOSED:
                return PullRequestClosedHandler(self.request.pull_request, self.request.sender).build()

            # Pull request synchronize
            if self.request.action == Actions.SYNCHRONIZE:
                return PullRequestSynchronizeHandler(self.request.pull_request, self.request.sender).build()

        if self.request.review and self.request.sender and self.request.action == Actions.SUBMITTED:
            return ReviewHandler(self.request.review, self.request.sender).build()

        return None
