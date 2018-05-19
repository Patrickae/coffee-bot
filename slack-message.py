import requests
import json
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_dowm=GPIO.PUD_DOWN)
coffee_status = 0
web_hook_url = 'https://hooks.slack.com/services/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'
images = ['https://media.giphy.com/media/oGP0Sv692lb68/giphy.gif',
 'https://media.giphy.com/media/Cqz6bKvjmFdyo/giphy.gif',
 'https://media.giphy.com/media/l4EoUY5KeQszUCAiA/giphy.gif',
 'https://media.giphy.com/media/R1fqW7QTkR8je/giphy.gif',
 'https://media.giphy.com/media/5xaYLxI6riEuY/giphy.gif',
 'https://media.giphy.com/media/oj05uAreWGy8U/giphy.gif',
 'https://media.giphy.com/media/3o7abKKlDojVbnZhAs/giphy.gif',
 'https://media.giphy.com/media/3oKIPx16LFvftHPLiM/giphy.gif']
slack_msg_coffee = {
	'text' : 'Fresh Pot!', 
	'username': 'coffee-bot', 
	'icon_emoji': ':coffeebean:',
	'attachments':[{
		'image_url': images[random.randint(0,len(images))]
	}]
}
slack_msg_quit = {
	'text' : 'Coffe bot not listening', 
	'username': 'coffee-bot', 
	'icon_emoji': ':coffeebean:',
	'attachments':[{
		'image_url': 'https://media.giphy.com/media/5Zesu5VPNGJlm/giphy.gif'
	}]
}

# requests.post(web_hook_url, data=json.dumps(slack_msg_coffee) )

try:
	while True:
		if (GPIO.input(7) == 1):
			if (coffee_status == 0):
				print('coffee brewin')
				coffee_status = 1
		else:
			if (coffee_status = 1):
				print('fresh pot')
				coffee_status = 1

except KeyboardInterrupt:
	GPIO.clenup()
except:
	requests.post(web_hook_url, data=json.dumps(slack_msg_quit))


# https://hooks.slack.com/services/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