import requests
import json
import random

web_hook_url = 'https://hooks.slack.com/services/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'

images = ['https://media.giphy.com/media/oGP0Sv692lb68/giphy.gif',
 'https://media.giphy.com/media/Cqz6bKvjmFdyo/giphy.gif',
 'https://media.giphy.com/media/l4EoUY5KeQszUCAiA/giphy.gif',
 'https://media.giphy.com/media/R1fqW7QTkR8je/giphy.gif',
 'https://media.giphy.com/media/5xaYLxI6riEuY/giphy.gif',
 'https://media.giphy.com/media/oj05uAreWGy8U/giphy.gif',
 'https://media.giphy.com/media/3o7abKKlDojVbnZhAs/giphy.gif',
 'https://media.giphy.com/media/3oKIPx16LFvftHPLiM/giphy.gif']

slack_msg = {
	'text' : 'Fresh Pot!', 
	'username': 'coffee-bot', 
	'icon_emoji': ':coffeebean:',
	'attachments':[{
	 	'image_url': images[random.randint(0,len(images))]
	 	}]
	 }

requests.post(web_hook_url, data=json.dumps(slack_msg) )

# https://hooks.slack.com/services/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