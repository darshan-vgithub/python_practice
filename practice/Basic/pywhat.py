import pywhatkit as pwk

phone_number = "+919886849137"
message = "Hello, this is an automated message sent using Python."

# Sends the message instantly (with a short delay to allow the page to load)
pwk.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True, close_time=3)
