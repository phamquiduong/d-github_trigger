import logging
import os
import traceback

from fastapi import FastAPI, Request, status

from schemas.webhooks.request import WebhookRequest
from services.builder import Build
from services.tele import TelegramService

app = FastAPI()
logger = logging.getLogger()
telegram_service = TelegramService(bot_token=os.environ['BOT_TOKEN'], chat_id=os.environ['CHAT_ID'])


@app.exception_handler(Exception)
async def general_exception_handler(_: Request, exc: Exception):
    logger.exception(exc)

    message = f'<pre>{traceback.format_exception(exc)}</pre>'
    await telegram_service.send_message(message)

    return {'message': 'OK'}


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.post('/', status_code=status.HTTP_200_OK)
async def github_action_webhook(
    webhook_request: WebhookRequest
):
    message = Build(webhook_request).run()
    await telegram_service.send_message(message)

    return {'message': 'OK'}
