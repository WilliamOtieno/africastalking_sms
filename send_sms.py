import africastalking
from secrets import api_key

username = 'sandbox'

africastalking.initialize(username, api_key)

sms = africastalking.SMS

try:
	response = sms.send("Hey AT Ninja!", ["+254719383956"]) #Enter your phone number here
	print(response)
except Exception as e:
	print(f"Something went wrong {e}")

SMS().send()