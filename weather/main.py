# with open("weather_data.csv") as file:
#     data = file.read().splitlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# Directly access data in that column
#print(data["temp"])

# Puts the temperatures into a list, instead of Series with 1 column
#temp_list = data["temp"].to_list()
#print(temp_list)

# data["temp"] is the Series and .mean() is the Series method
#print(data["temp"].mean())
#print(data["temp"].max())

# Change type to dictionary where key is the column title and values are the data
#data_dict = data.to_dict()
#print(data_dict)

# Prints row
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
# Without float casting, prints as Series and outputs Name: temp, dtype: float64 as well
#print(float(monday.temp * 1.8 + 32))

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")