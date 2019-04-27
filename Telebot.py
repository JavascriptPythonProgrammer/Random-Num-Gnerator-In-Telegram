import random
import telebot 

bot = telebot.TeleBot("738228075:AAHkI1Ea1nwvL4Gego7Ns53C1BTB-WL9scc")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	if message.text == "Get Random Number":
		for x in range(1):
			answer = random.randint(1,1001)
		bot.send_message( message.chat.id, answer)
	if message.text != "Get Random Number":
		if message.text != "Thank's":
			if message.text != "!qaz@wsx2005":
				if message.text != "/start":
					if message.text != "Good Bye!":
						if message.text != "Hello!":
							if message.text != "Hello":
								bot.send_message( message.chat.id, "It's not a command")
	if message.text == "Thank's":
		bot.send_message( message.chat.id, "Not worth")
	if message.text == "!qaz@wsx2005":
		bot.send_message( message.chat.id, "Bot Create Samvel Hovhannisyan")
	if message.text == "/start":
		bot.send_message( message.chat.id, 'Write the command "Get Random Number"')
	if message.text == "Good Bye!":
		bot.send_message( message.chat.id, "Bye!")
	if message.text == "Hello!":
		bot.send_message( message.chat.id, "Hello!")
	if message.text == "Hello":
		bot.send_message( message.chat.id, "Hello!")
bot.polling( none_stop = True )