food = {}


while True:
    try:
        item = input()
        item = item.lower()
        if item in food:
            food[item] += 1
        else:
            food[item] = 1
    except EOFError:
        break
sorted_numbers = sorted(food.items())
for item, number in sorted_numbers:
    print(f"{number} {item.upper()}")
