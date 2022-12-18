import pandas as pd

# Change the name to match the name on CSV
MC = "Unit 4 Test MC"
FRQ = "Unit 4 Test FRQs"

total_score = float(input("Enter total score: "))

df = pd.read_csv('scores.csv')

# Calculations
added_points = (df[MC] + df[FRQ])
raw_points = added_points.div(total_score)
curved_percentage =  raw_points.pow(1/2)
curved_points = curved_percentage * total_score
rounded_points = curved_points.round(decimals=0)

# Add the calculated scores to the dataframe
df["Final Score"] = rounded_points
#print(df)

# Overwrite existing csv file
df.to_csv("scores.csv")

