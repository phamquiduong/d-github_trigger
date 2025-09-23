from constants.github import RequestActions, ReviewState, WorkflowRunConclusions, WorkflowRunStatus
from helpers.html_helper import build_link, build_pre
from schemas.base import ExtraIgnoreModel


class WorkFlowRun(ExtraIgnoreModel):
    id: int
    name: str
    html_url: str
    status: WorkflowRunStatus
    conclusion: WorkflowRunConclusions | None = None

    def as_html(self) -> str:
        html_link = build_link(link=self.html_url, display=f'Workflow#{self.id}')
        return f'⚙️  {html_link}: {self.name}'

    def conclusion_html(self) -> str:
        match self.conclusion:
            case WorkflowRunConclusions.SUCCESS:
                return '🎉  Run success'
            case WorkflowRunConclusions.FAILURE:
                return '❌  Run failed'
            case WorkflowRunConclusions.CANCELLED:
                return '🛑  Run cancelled'
            case WorkflowRunConclusions.SKIPPED:
                return '⏭️  Run skipped'
            case WorkflowRunConclusions.NEUTRAL:
                return '⚪  Run neutral'
            case WorkflowRunConclusions.STALE:
                return '🥶  Run stale'
            case WorkflowRunConclusions.TIMED_OUT:
                return '⌛  Run timed out'
            case WorkflowRunConclusions.ACTION_REQUIRED:
                return '⚠️  Action required'
            case WorkflowRunConclusions.STARTUP_FAILURE:
                return '💥  Startup failure'
            case None:
                return '❓  No conclusion'
            case _:
                return '🤔  Unknown conclusion'


class PullRequest(ExtraIgnoreModel):
    number: int
    title: str
    html_url: str
    merged: bool | None = None

    def as_html(self) -> str:
        html_link = build_link(link=self.html_url, display=f'PR#{self.number}')
        return f'🔀  {html_link}: {self.title}'

    def action_html(self, action: RequestActions | None):
        match action:
            case RequestActions.OPENED:
                return '🆕  Pull request created'
            case RequestActions.SYNCHRONIZE:
                return '🔄  Pull request updated (new commits)'
            case RequestActions.CLOSED if self.merged:
                return '🎉  Pull request merged'
            case RequestActions.CLOSED:
                return '🛑  Pull request closed'
            case _:
                return '🤔  Unknown pull request action'


class Sender(ExtraIgnoreModel):
    name: str | None = None
    login: str
    html_url: str

    def as_html(self) -> str:
        html_link = build_link(link=self.html_url, display=self.name or self.login)
        return f'👤  {html_link}'


class Review(ExtraIgnoreModel):
    body: str | None = None
    html_url: str
    state: ReviewState

    def as_html(self) -> str:
        html_link = build_link(link=self.html_url, display=f'Review#{self.state}')
        pre_text = build_pre(self.body) if self.body else ''
        return f'📝  {html_link}\n{pre_text}'

    def action_html(self):
        match self.state:
            case ReviewState.APPROVED:
                return '✅  Review approved'
            case ReviewState.CHANGES_REQUESTED:
                return '❌  Changes requested'
            case ReviewState.COMMENTED:
                return '💬  Review commented'


class Comment(ExtraIgnoreModel):
    path: str | None = None
    position: int | None = None
    html_url: str
    body: str | None = None

    def as_html(self) -> str:
        html_link = build_link(link=self.html_url, display=f'Comment#{self.path}:{self.position}')
        pre_text = build_pre(text=self.body) if self.body else ''
        return f'💬  {html_link}\n{pre_text}'


class GithubRequest(ExtraIgnoreModel):
    action: RequestActions | None = None
    workflow_run: WorkFlowRun | None = None
    pull_request: PullRequest | None = None
    sender: Sender | None = None
    review: Review | None = None
    comment: Comment | None = None
