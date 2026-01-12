# Dataset from Activity 1(SG4)

Activity #2

names = ["Me", "Anna", "Mark"]

steps = [
    [5200, 5400, 5100, 5700, 5800],  # Me (updated Thursday)
    [4300, 4500, 4400, 4700, 4900],  # Anna
    [6100, 6000, 6200, 6300, 6500]   # Mark
]

# Summarize data for each person
for i in range(len(names)):
    total_steps = sum(steps[i])
    average_steps = total_steps / len(steps[i])
    min_steps = min(steps[i])
    max_steps = max(steps[i])

    print(
        names[i], 
        "- Total Steps:", total_steps,
        "| Average:", average_steps,
        "| Min:", min_steps,
        "| Max:", max_steps
    )

