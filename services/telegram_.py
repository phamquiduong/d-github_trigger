import logging
from time import sleep

import requests

logger = logging.getLogger()


class TelegramService:
    def __init__(self, bot_token: str, chat_id: str, retries: int = 3, backoff: float = 1.0) -> None:
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'
        self.retries = retries
        self.backoff = backoff

    def send_message(self, message: str | None) -> None:
        if not message:
            return

        url = f'{self.base_url}/sendMessage'
        payload = {
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': 'HTML',
            'disable_web_page_preview': True,
        }

        attempt = 0
        while attempt < self.retries:
            try:
                response = requests.post(url, json=payload, timeout=10)
                response.raise_for_status()
                return
            except requests.RequestException as e:
                attempt += 1
                logger.error('Telegram send_message failed (attempt %d/%d): %s', attempt, self.retries, e)
                if attempt < self.retries:
                    sleep(self.backoff * attempt)
