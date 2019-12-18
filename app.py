from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ISfO6SASKHjGv7zG7gdoIcgky12wCNPW7Od2cS+mBIsu0G8AjsT2UFZdr/rKTFLvAY4Z1c/j1uFesyBaxkbM0Vr3WFBFxXAZoxQc/w3WdG1qxcvB7bnaO9u2M3TEDncuWxd3HiF1VdSWUXNtnMYOiQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f0283bace9e8b0536cab1e394f96cec9')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉，我不瞭解您的意思'

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return


    if msg in ['hi', 'Hi']:
        r = '嗨'
    elif msg == '你吃飽了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r == '我是機器人喔'
    elif '訂位' in msg:
        r = '您是否要訂位呢？'



    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()

