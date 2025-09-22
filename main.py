import html
import json
import logging
import os
import traceback

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from schemas.webhooks.request import WebhookRequest
from services.builder import Build
from services.telegram_ import TelegramService

app = FastAPI()
logger = logging.getLogger()
telegram_service = TelegramService(bot_token=os.environ['BOT_TOKEN'], chat_id=os.environ['CHAT_ID'])


@app.exception_handler(Exception)
async def general_exception_handler(_: Request, exc: Exception):
    logger.exception(exc)

    message = f'<pre>{html.escape(''.join(traceback.format_exception(exc)))}</pre>'
    await telegram_service.send_message(message)

    return JSONResponse(
        status_code=200,
        content={'message': 'OK'}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_json = {
        'errors': exc.errors(),
    }

    logger.error(json.dumps(error_json, ensure_ascii=False))

    return JSONResponse(
        status_code=200,
        content={'message': 'OK'}
    )


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.post('/{project_name}', status_code=status.HTTP_200_OK)
async def github_action_webhook(
    project_name: str,
    webhook_request: WebhookRequest,
):
    message = Build(webhook_request).run()
    await telegram_service.send_message(message)

    return {'message': 'OK'}
