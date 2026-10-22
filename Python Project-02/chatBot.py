#Personal Chat Assistant

import datetime
import time

print("Welcome to ChatBot!")
print("Type 'bye' to exit from the chat")

name = input("Bot: Say your name to start the chat-\n")

#Importing and using current time to give greeting.
presentHour = datetime.datetime.now().hour

if 4<= presentHour <= 11:
    print("Bot: Good Morning! ",name)
elif 12<= presentHour <=3:
    print("Bot: Good Noon! ",name)
elif 4<= presentHour <=6:
    print("Bot: Good Afternoon! ",name)
elif 6<= presentHour <=7:
    print("Bot: Good Evening! ",name)
else:
    print("Bot: Good Night! ",name)

#Making keyword and bot reply using dictionary
responses = {
    "hello" : "Hi! How can i help you?",
    "who are you" : "I am a Chat-Bot",
    "how are you" : "I am fine",
    "motivate me" : "Just do it and keep going...",
    "bye" : "Tata!"
}

#Function for bot reply
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I don't know this. I am still learning"

#Taking user input and break the chat when user says,"bye".
while True:
    userInput = input(name +":")
    reply = getResponseOfBot(userInput)
    print("Bot: ", reply)
    if "bye" in userInput.lower():
        break