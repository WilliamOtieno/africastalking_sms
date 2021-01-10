import africastalking
from secrets import api_key

username = 'sandbox'

africastalking.initialize(username, api_key)

sms = africastalking.SMS
sender = 'William'

try:
	response = sms.send("Hey AT Ninja!", ["+254719383956"], sender) #Enter your phone number here
	print(response)
except Exception as e:
	print(f"Will, something went wrong: {e}")