# coding: utf-8
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import os
# リモートリポジトリに"ご自身のチャネルのアクセストークン"をpushするのは、避けてください。
# 理由は、そのアクセストークンがあれば、あなたになりすまして、プッシュ通知を送れてしまうからです。
#LINE_CHANNEL_ACCESS_TOKEN = "Rbmsk9PUeO/9uAmRXd3p3W0hXZjhOgiXP7FvXjNRK3KwveRYwfAVoI2YvUDJp3qOaKHwAOEAiUjWCQHnWkRMcyIbxKzdJ68dJJL7UAQNVJEPhzx1k0WoFtslPAnwu3TyjkP9/Ovxr8WH/0XgjyZ7RAdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


user_id = os.environ["USER_ID"]
message = TextSendMessage(text="helloworld")
line_bot_api.push_message(user_id, TextSendMessage(text='helloworld'))

