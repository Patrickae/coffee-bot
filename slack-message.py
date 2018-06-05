import requests
import json
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
switch_is_up = False
num = 0
web_hook_url = 'https://hooks.slack.com/services/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'


images = ['https://media.giphy.com/media/oGP0Sv692lb68/giphy.gif',
 'https://media.giphy.com/media/Cqz6bKvjmFdyo/giphy.gif',
 'https://media.giphy.com/media/R1fqW7QTkR8je/giphy.gif',
 'https://media.giphy.com/media/5xaYLxI6riEuY/giphy.gif',
 'https://media.giphy.com/media/oj05uAreWGy8U/giphy.gif',
 'https://media.giphy.com/media/3o7abKKlDojVbnZhAs/giphy.gif',
 'https://media.giphy.com/media/3oKIPx16LFvftHPLiM/giphy.gif',
 'https://media.giphy.com/media/11Y6s1RQdou6mA/giphy.gif',
 'https://media.giphy.com/media/7jdyW2bKeUcI8/giphy.gif',
 'https://media.giphy.com/media/cKhpesDJ5iofu/giphy.gif',
 'https://media.giphy.com/media/E5NOoH80VSt0I/giphy.gif',
 'https://media.giphy.com/media/yNr8LdsnuqdnfbgVXN/giphy.gif']




slack_msg_coffee = {
	'text' : 'Fresh Pot!',
	'username': 'coffee-bot',
	'icon_emoji': ':coffeebean:',
	'attachments':[{
		'image_url': images[num]
	}]
}



slack_msg_quit = {
	'text' : 'Coffe bot not listening',
	'username': 'coffee-bot',
	'icon_emoji': ':coffeebean:',
	'attachments':[{
		'image_url': 'https://media.giphy.com/media/8zjvJAxHYMFGg/giphy.gif'
	}]
}



slack_msg_online = {
  'text' : 'Coffe bot is online',
  'username': 'coffee-bot',
  'icon_emoji': ':coffeebean:',
  'attachments':[{
    'image_url': 'https://media.giphy.com/media/LqUA1opXygflK/giphy.gif'
  }]
}

def change_random_number():
	global num
	num = random.randint(0,len(images)-1)
	global slack_msg_coffee
	slack_msg_coffee = {
	'text' : 'Fresh Pot!',
	'username': 'coffee-bot',
	'icon_emoji': ':coffeebean:',
	'attachments':[{
		'image_url': images[num]
		}]
	}

def change_switch_status(status):
	global switch_is_up
	switch_is_up = status

requests.post(web_hook_url, data=json.dumps(slack_msg_online))

try:
	while True:
		if (GPIO.input(7) == 1):
			if (switch_is_up == False):
				change_switch_status(True)
				print('coffee brewin')
		else:
			if (switch_is_up == True):
				change_switch_status(False)
				print('fresh pot')
				change_random_number()
				requests.post(web_hook_url, data=json.dumps(slack_msg_coffee))

except KeyboardInterrupt:
	GPIO.cleanup()
	requests.post(web_hook_url, data=json.dumps(slack_msg_quit))
except:
	requests.post(web_hook_url, data=json.dumps(slack_msg_quit))

# https://hooks.slack.com/services/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
