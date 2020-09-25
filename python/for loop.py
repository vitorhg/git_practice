# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for num in areas:
    print(num)


# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, num in enumerate(areas):
    print("room", index, ": ", num)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas):
    print("room " + str(index + 1) + ": " + str(area))


# house list of lists
house = [
    ["hallway", 11.25],
    ["kitchen", 18.0],
    ["living room", 20.0],
    ["bedroom", 10.75],
    ["bathroom", 9.50],
]

# Build a for loop from scratch
for room in house:
    print("the", room[0], "is", room[1], "sqm")
