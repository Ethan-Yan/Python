##error

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "Account Sid"
auth_token  = "{{ Auth Token }}"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="My name is Ethan",
    to="+1 ",    # Replace with your phone number
    from_="+1 ") # Replace with your Twilio number
print (message.sid)
