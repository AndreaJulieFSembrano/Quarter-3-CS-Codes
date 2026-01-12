names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

daily_totals = []

for day in range(len(steps[0])):
    total = 0
    for person in range(len(steps)):
        total += steps[person][day]
    daily_totals.append(total)
    print(days[day], "total steps:", total)

highest = daily_totals[0]
highest_index = 0

for i in range(len(daily_totals)):
    if daily_totals[i] > highest:
        highest = daily_totals[i]
        highest_index = i

print("\nMost active day overall:", days[highest_index])
print("Total steps on that day:", highest)
