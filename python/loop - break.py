items_on_sale = [
    "blue_shirt",
    "striped_socks",
    "knit_dress",
    "red_headband",
    "dinosaur_onesie",
]

print("Checking the sale list!")
for item in items_on_sale:
    print(item)
    if item == "knit_dress":
        break
print("End of search!")


dog_breeds_available_for_adoption = [
    "french_bulldog",
    "dalmation",
    "shihtzu",
    "poodle",
    "collie",
]
dog_breed_I_want = "dalmation"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break
