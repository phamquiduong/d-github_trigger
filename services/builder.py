from constants.github import WorkflowRunStatus
from schemas.github import GithubRequest


class Build:
    def __init__(self, request: GithubRequest) -> None:
        self.request = request

    def run(self) -> str | None:
        r = self.request

        if r.workflow_run and r.workflow_run.status == WorkflowRunStatus.COMPLETED:
            return f'{r.workflow_run.as_html()}\n{r.workflow_run.conclusion_html()}'

        return None
