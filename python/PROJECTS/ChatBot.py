#rule based python smart AI , sanyuktas studdybuddy

#creating greeting based on time
import datetime
import time

presentHour=datetime.datetime.now().hour

if 5<= presentHour <=11:
    print("Good morning!")
elif 11<= presentHour <=17:
    print("Good afternoon!")
elif 17<= presentHour <=20:
    print("Good evening!")
else:
    print("Good night!")


#program start greeting

print("Welcome to Sanyuktas studdybuddy , type 'bye' to exit this program")

#chatbot memory creation

responses={
    "hello":"Hi! How can i help you today?",
    "how are you":"I'm fine, thank you",
    "who are you":"I'm sanyuktas studdybuddy",
    "motivate":"Keep going! Every bug fix makes you a strong coder",
    "happy":"Great to hear that <3",
    "sad":"Dont worry:( Dark nights are often followed ny a bright day!",
    "functions":"Please refer chapter 7 of your learning",
    "dictionary":"Please refer chapter 5 of your learning",
    "loops":"Please refer chapter 6 of your learning",
    "bye":"Thank you for interacting with sanyuktas studdybuddy!!Have a good day!"
}

# function to get responses

def getResponse(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "Invalid operation ! Try again"

# take user input

while True:
    userInput=input("Enter your question: ")
    reply=getResponse(userInput)
    print("Bot:" ,reply)
    time.sleep(1)

    if "bye" in userInput.lower():
        break
