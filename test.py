import requests
import json

web_hook_url = 'https://hooks.slack.com/services/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'

slack_msg_online = {
  'text' : 'Coffe bot is online',
  'username': 'coffee-bot',
  'icon_emoji': ':coffeebean:',
  'attachments':[{
    'image_url': 'https://media.giphy.com/media/LqUA1opXygflK/giphy.gif'
  }]
}

r = requests.post(web_hook_url, data=json.dumps(slack_msg_online))

print(r)