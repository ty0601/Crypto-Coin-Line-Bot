import os

from linebot import LineBotApi
from linebot.models import TextSendMessage, FlexSendMessage

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_flex_message(reply_token, alt_text, json_message):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text, json_message))


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
