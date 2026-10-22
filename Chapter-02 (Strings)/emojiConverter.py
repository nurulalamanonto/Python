#Convert text-based emotions to emojis

msg = input("Enter a massage: ")

msg = msg.replace(":)", "🙂")
msg = msg.replace(":(", "😞")
msg = msg.replace(":D", "😃")
msg = msg.replace(";)", "😉")

print(msg)