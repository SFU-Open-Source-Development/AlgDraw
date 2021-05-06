import pandas as pd
import numpy as np
from tkinter import filedialog
from tkinter import *
# import pygame
import pygame_textinput


def input_prompt():
    '''prompts user for file using tkinter, returns path to file'''
    window = Tk()
    window.withdraw()
    prompt_file = filedialog.askopenfilename(title="Select an excel or text file",
            filetypes=[("Text Files", ("*.txt", "*.csv")), ("Excel", ("*.xls","*xlsx"))])
    window.destroy()
    return prompt_file


def input_valid(file_input, col_list, font, screen):
    '''validates user input and returns array for sorting'''
    ans_valid = False
    while not ans_valid:
        if file_input.endswith(".csv") or file_input.endswith(".txt"):
            array = read_textfile(file_input, col_list)
            ans_valid = True
        elif file_input.endswith(".xlsx") or file_input.endswith(".xls"):
            array = read_excelfile(file_input, col_list)
        else:
            error_text = font.render('You are missing .csv, .txt, .xls, .xlsx',
                                     False, (0, 0, 0))  # error message
            screen.blit(error_text, (0, 0))
            ans_valid = False
    return array


def read_textfile(filename, col_list):
    '''reads a text file and parses the input according to chosen columns'''
    array = []
    f = pd.read_csv(filename, encoding='utf-8', usecols=col_list)
    # https://www.kite.com/python/docs/pandas.DataFrame.replace
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
    f.replace(r'^\s*$', np.nan, inplace=True)
    array.append(f.astype(float))  # converts all objects in dataframe into float
    return array

def read_excelfile(filename, col_list):
    '''reads an excel file and parses the input according to chosen columns'''
    array = []
    f = pd.read_excel(filename, encoding='utf-8', usecols=col_list)
    f.replace(r'^\s*$', np.nan, inplace=True)
    array.append(f.astype(float))
    return array


if __name__ == "__main__":
