from csv import reader
from pandas import *

filename = "../DB.csv"


def mapper():
    categories = ["humidity", "celsius", "farenheit", "heat_index"]
    dataframe = read_csv(filename, names=categories)
    humidity = dataframe['humidity'].to_list()
    celsius = dataframe['celsius'].to_list()
    farenheit = dataframe['farenheit'].to_list()
    heat_index = dataframe['heat_index'].to_list()


mapper()