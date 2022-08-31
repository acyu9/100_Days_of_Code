heights = [180, 124, 165, 173, 189, 169, 146]

total = 0

for height in heights:
    total += height

average = round(total / len(heights))
print(f"Average height of students is {average}")


# Could use counter in for loop instead of len
# Could use sum function instead of for loop