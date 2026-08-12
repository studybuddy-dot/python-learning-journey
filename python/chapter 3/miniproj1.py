#convert text based emotions into emojis
msg = input("Enter your mood:")

msg = msg.replace(":)","😊")
msg = msg.replace(":(","☹️")
msg = msg.replace(":D","😁")
msg = msg.replace(";)","😉")

print(msg)