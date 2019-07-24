sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)


words = [
    "@coolguy35",
    "#nofilter",
    "@kewldawg54",
    "reply",
    "timestamp",
    "@matchamom",
    "follow",
    "#updog",
]
usernames = []

for word in words:
    if word[0] == "@":
        usernames.append(word)
print(usernames)

words = [
    "@coolguy35",
    "#nofilter",
    "@kewldawg54",
    "reply",
    "timestamp",
    "@matchamom",
    "follow",
    "#updog",
]
usernames = []

usernames = [word for word in words if word[0] == "@"]

print(usernames)


# imprime valores maiores que 161
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)


# converte cesius em fahrenheit
celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [(temp * (9 / 5) + 32) for temp in celsius]

print(fahrenheit)
