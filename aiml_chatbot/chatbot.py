import aiml
import os

kernel=aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
print("BOT>> Welcome to hotel abc")
while True:
	input_text=input("USER >>")
	response = kernel.respond(input_text)	
	print("BOT>>"+response)
