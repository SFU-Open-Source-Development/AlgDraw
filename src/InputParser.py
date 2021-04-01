from typing import Any, Union

import pandas as pd
import numpy as np

# validates file name input
from pandas import DataFrame, Series
from pandas.io.parsers import TextFileReader


def input_valid():
    ans_valid = False
    while not ans_valid:
        file_input = input("Type file name (include .csv or .txt): ")
        if ".csv" not in file_input and ".txt" not in file_input:
            print("You forgot to include .csv or .txt, try again")
            ans_valid = False
        else:
            ans_valid = True
    return file_input

# take in user inputs
def input_cmd():

    filename = input_valid() # takes in file name

    # possible for user to input column name
    # but needs if-statement to verify if user wants to input numbers or names
    col_input = input("Column numbers to be read (separated by ','): ")
    col_list = col_input.split(",")
    for i in range(len(col_list)):
        col_list[i] = int(col_list[i])

    #num_headers = int(input("How many headers in file?: "))

    file_delim = input("Type of column delimiter:")
    return filename, file_delim, col_list

def read_file(filename, file_delim, col_list):
    f: Union[Union[TextFileReader, Series, DataFrame, None], Any] = pd.read_csv(filename, encoding='utf-8',
                   sep=file_delim, usecols=col_list)
    # https://www.kite.com/python/docs/pandas.DataFrame.replace
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
    f.replace(r'^\s*$', np.nan, inplace=True)
    for i in col_list:
        col_list.append(float(i))  # convert each object in columns to float
    return filename, col_list  # col_list are the list of numbers to be sorted

    # if f.mode == 'r':
    #     f1 = f.readlines()
    #     index = 0
    #     a = [None] * length  # what is length
    #     for x in f1:
    #         a[index] = x
    #         print(a[index])
    #         index = index + 1


if __name__ == "__main__":

    filename, file_delim, col_list = input_cmd()
    read_file(filename, file_delim, col_list) #

    # read_file(r"C:\Users\Aliyah\OSDC\greetings.txt", 3)
    # print("thanks conor :D")
