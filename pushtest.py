from flask import Flask, request, abort

import os,re

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import  InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageAction

import datetime

import openpyxl as px
from random import randint
from linebot.exceptions import LineBotApiError

LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

receiver = 'receiver id'
def pushMessage(message):
    try:
        line_bot_api.push_message(receiver, TextSendMessage(text=message))
        print("success")
    except LineBotApiError as e:
        print(e)
pushMessage("Hello!")
pushMessage("こんにちは")
pushMessage("你好")