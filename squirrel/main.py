import pandas

data = pandas.read_csv("squirrel_data.csv")
fur_colors = data["Primary Fur Color"]
fur_colors.value_counts().to_csv("fur_data.csv")