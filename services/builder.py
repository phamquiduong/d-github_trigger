from constants.github import RequestActions, ReviewState, WorkflowRunStatus
from schemas.github import GithubRequest


class Build:
    def __init__(self, request: GithubRequest) -> None:
        self.request = request

    def run(self) -> str | None:
        r = self.request

        if r.workflow_run and r.workflow_run.status == WorkflowRunStatus.COMPLETED:
            return (
                f'<b>{r.workflow_run.as_html()}</b>\n'
                f'{r.workflow_run.conclusion_html()}'
            )

        if (
            r.pull_request and r.sender
            and r.action in [RequestActions.OPENED, RequestActions.SYNCHRONIZE, RequestActions.CLOSED]
        ):
            return (
                f'<b>{r.pull_request.as_html()}</b>\n'
                f'{r.pull_request.action_html(action=r.action)} by {r.sender.as_html()}'
            )

        if (
            r.pull_request and r.sender and r.review
            and r.action == RequestActions.SUBMITTED
            and (r.review.state == ReviewState.APPROVED or r.review.body)
        ):
            return (
                f'<b>{r.pull_request.as_html()}</b>\n'
                f'{r.review.action_html()} by {r.sender.as_html()}\n'
                f'{r.review.body_html()}'
            )

        if (
            r.pull_request and r.sender and r.comment
            and r.action == RequestActions.CREATED
        ):
            return (
                f'<b>{r.pull_request.as_html()}</b>\n'
                f'{r.sender.as_html()} comment {r.comment.as_html()}\n'
                f'{r.comment.body_html()}'
            )

        return None
