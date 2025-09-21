from enum import StrEnum

from pydantic import HttpUrl

from schemas.base import WebhookRequestBase


class PullRequest(WebhookRequestBase):
    id: int
    url: HttpUrl

    @property
    def html_url(self) -> HttpUrl:
        parts = str(self.url).split('/')
        owner, repo, pr_number = parts[-4], parts[-3], parts[-1]
        html_url = f'https://github.com/{owner}/{repo}/pull/{pr_number}'
        return HttpUrl(html_url)

    def as_html(self):
        return f'[<a href="{self.html_url}">PR#{self.id}</a>]'


class Conclusions(StrEnum):
    SUCCESS = 'success'
    FAILURE = 'failure'


class CheckRun(WebhookRequestBase):
    id: int
    name: str
    html_url: HttpUrl
    conclusion: Conclusions
    pull_requests: list[PullRequest]

    def as_html(self):
        return f'[<a href="{self.html_url}">Action#{self.id}</a>: <b>{self.name}</b>]'


class CheckRunHandler:
    def __init__(self, check_run: CheckRun) -> None:
        self.check_run = check_run

    def run(self) -> str | None:
        pr_html = ''.join(f'{pr.as_html()}' for pr in self.check_run.pull_requests)
        check_run_html = self.check_run.as_html()

        if self.check_run.conclusion == Conclusions.SUCCESS:
            return f'✅  {pr_html}{check_run_html}  Run success'

        if self.check_run.conclusion == Conclusions.FAILURE:
            return f'❌  {pr_html}{check_run_html}  Run failure'

        return None
