# Key value pairs
customer = {
    "name": "Swagatika Mahapatra",
    "age": 31,
    "is_verified": True
}

print(customer["name"])
print(customer.get("dob"))

#Update values using get method
print(customer.get("dob", "May 22"))

#Emoji converter

message = input(">")
words = message.split(' ')

emojis = {

    ":)": "😊",
    ":(": "😢",
    "<3": "❤"
}
output = ''
for word in words:
    output += emojis.get(word, word) + " "

print(output)

