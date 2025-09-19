import logging

from telegram import Bot, LinkPreviewOptions
from telegram.constants import ParseMode

logger = logging.getLogger()


class TelegramService:
    def __init__(self, bot_token: str, chat_id: str) -> None:
        self.bot = Bot(token=bot_token)
        self.chat_id = chat_id

    async def send_message(self, message: str | None) -> None:
        if not message:
            return

        link_preview = LinkPreviewOptions(is_disabled=True)
        await self.bot.send_message(
            chat_id=self.chat_id,
            text=message,
            parse_mode=ParseMode.HTML,
            link_preview_options=link_preview
        )
