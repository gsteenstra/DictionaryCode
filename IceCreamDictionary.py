ice_cream = {
    "Vanilla": 3.00,
    "Chocolate": 3.50,
    "Strawberry": 3.25,
    "Cookies and Cream": 4.00
}
print("Welcome to the Ice Cream Shop!")
print("Our Menu:", ice_cream)

print("Vanilla costs $", ice_cream["Vanilla"])

ice_cream["Mint Chocolate Chip"] = 4.25
print("New Flavor Has Been Added")

ice_cream["Chocolate"] = 3.75
print("Chocolate price has beenupdated")

del ice_cream["Strawberry"]
print("Strawberry is no longer available")

print("\nUpdated Ice Cream Menu:")

for flavor, price in ice_cream.items():
    print(flavor, "- $", price)