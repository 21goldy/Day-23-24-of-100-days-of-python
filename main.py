# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
#
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

# data_list = data["temp"].to_list()
# print(data["temp"].max())
# print(data["temp"].min())
# print(data["temp"])
#
# print(data.temp == data["temp"].max())
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp * 9/5 + 32)
# print(data.temp * 9/5 + 32)
#
# dict = {
#         'name': ['Instagram', 'goldy', 'buddhu'],
#         'follower_count': [346, 45, 45],
#     }
# a = pandas.DataFrame(dict)
# print(a)
# a.to_csv("my_data.csv")
s_data = pandas.read_csv("squirrels_data.csv")
gray_squirrels = s_data[s_data.Primary_Fur_Color == "Gray"]
gray = len(gray_squirrels)
black_squirrels = s_data[s_data.Primary_Fur_Color == "Black"]
black = len(black_squirrels)
cinnamon_squirrels = s_data[s_data.Primary_Fur_Color == "Cinnamon"]
cinnamon = len(cinnamon_squirrels)

dictionary = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black],
}
final_data = pandas.DataFrame(dictionary)
print(final_data)
final_data.to_csv("my_data.csv")
