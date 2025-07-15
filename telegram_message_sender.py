
import httpx # type: ignore
import os
from typing import Any, Dict

# Telegram channel chat ID where the message will be sent.
_CHAT_ID: str = os.getenv("TELEGRAM_CHAT_ID", "@v7_solar")

# Telegram bot token (recommended to use environment variables in production).
_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "6818149519:AAFFtWmg_Plf5xYzyVaeDDIEtCc5cXnosU8")

def send_telegram_message(text: str) -> Dict[str, Any]:
    """
    Sends a message to a Telegram channel using a bot.

    Args:
        text (str): The message text to send to the channel.

    Returns:
        dict: The JSON response from the Telegram API.

    Raises:
        httpx.HTTPError: If a network problem occurs.
        RuntimeError: If Telegram API responds with an error.
    """
    url = f"https://api.telegram.org/bot{_TOKEN}/sendMessage"
    with httpx.Client() as client:
        response = client.post(
            url,
            data={"chat_id": _CHAT_ID, "text": text}
        )
        response.raise_for_status()  # Raises for HTTP error (network, 4xx, 5xx)
        data = response.json()
        if not data.get("ok", False):
            # Telegram API error
            error = data.get('description', 'Unknown error')
            raise RuntimeError(f"Telegram API error: {error}")
        return data
