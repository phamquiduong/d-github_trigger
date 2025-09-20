import logging

from schemas.webhooks.check_run import CheckRun, Conclusions
from schemas.webhooks.request import Actions, WebhookRequest

logger = logging.getLogger()


class Build:
    def __init__(self, webhook_request: WebhookRequest) -> None:
        self.request = webhook_request

    def run(self) -> str | None:
        # Check run handler
        if self.request.action == Actions.COMPLETED and self.request.check_run:
            return CheckRunHandler(self.request.check_run).run()

        return None


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
