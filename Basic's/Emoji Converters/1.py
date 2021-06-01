import emoji
message = input(">")
words = message.split('Good morning')
emojis = {
    ":)": "",
    ":(": ""
}
output = ""
for word in words:
    output += emojis.get(word, word) + ""
print(output)
