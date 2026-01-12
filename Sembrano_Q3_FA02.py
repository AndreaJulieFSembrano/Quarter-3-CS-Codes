Mini-Dataset Project((Own Dataset):

Scenario:

I want to track my daily step count along with my classmates Anna and Mark for 5 days.

 The 2D Array Represents:

Rows: Each person (Me, Anna, Mark)

Columns: Step counts for 5 days (Monday to Friday)

Daily Step Counts Table
| Name | Monday | Tuesday | Wednesday | Thursday | Friday |
| ---- | ------ | ------- | --------- | -------- | ------ |
| Me   | 5200   | 5400    | 5100      | 5600     | 5800   |
| Anna | 4300   | 4500    | 4400      | 4700     | 4900   |
| Mark | 6100   | 6000    | 6200      | 6300     | 6500   |

  Code:

# Names of people
names = ["Me", "Anna", "Mark"]

# 2D list for daily step counts (Monday to Friday)
steps = [
    [5200, 5400, 5100, 5600, 5800],  # Me
    [4300, 4500, 4400, 4700, 4900],  # Anna
    [6100, 6000, 6200, 6300, 6500]   # Mark
]

# Print Mark's steps on Wednesday
print("Mark's steps on Wednesday:", steps[2][2])

# Print my steps
print("My steps...", steps[0])

# Update my Thursday steps
print("Updating my Thursday steps to 5700.")
steps[0][3] = 5700

# Print updated steps
print("My updated steps:", steps[0])


