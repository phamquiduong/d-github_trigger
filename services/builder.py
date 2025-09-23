from constants.github import RequestActions, WorkflowRunStatus
from schemas.github import GithubRequest


class Build:
    def __init__(self, request: GithubRequest) -> None:
        self.request = request

    def run(self) -> str | None:
        r = self.request

        if r.workflow_run and r.workflow_run.status == WorkflowRunStatus.COMPLETED:
            return (
                f'{r.workflow_run.as_html()}\n'
                f'{r.workflow_run.conclusion_html()}'
            )

        if (
            r.pull_request and r.sender
            and r.action in [RequestActions.OPENED, RequestActions.SYNCHRONIZE, RequestActions.CLOSED]
        ):
            return (
                f'{r.pull_request.as_html()}\n'
                f'{r.pull_request.action_html(action=r.action)}\n'
                f'{r.sender.as_html()}'
            )

        if (
            r.pull_request and r.sender and r.review
            and r.action == RequestActions.SUBMITTED
        ):
            return (
                f'{r.pull_request.as_html()}\n'
                f'{r.review.action_html()}\n'
                f'{r.sender.as_html()}\n'
                f'{r.review.as_html()}'
            )

        if (
            r.pull_request and r.sender and r.comment
            and r.action == RequestActions.CREATED
        ):
            return (
                f'{r.pull_request.as_html()}\n'
                f'{r.sender.as_html()}\n'
                f'{r.comment.as_html()}'
            )

        return None
