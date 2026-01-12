names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

total_steps = []

for i in range(len(steps)):
    total = 0
    for s in steps[i]:
        total += s
    total_steps.append(total)
    print(names[i], "total steps:", total)

highest = total_steps[0]
lowest = total_steps[0]
highest_index = 0

for i in range(len(total_steps)):
    if total_steps[i] > highest:
        highest = total_steps[i]
        highest_index = i
    if total_steps[i] < lowest:
        lowest = total_steps[i]

difference = highest - lowest

print("\nPerson with the highest total steps:", names[highest_index])
print("Difference between highest and lowest total steps:", difference)
