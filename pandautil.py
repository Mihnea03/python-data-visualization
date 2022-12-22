import pandas as pd
import matplotlib.pyplot as plt
import re
from re import Match

user_df = pd.read_csv('customers.csv')

def search_by_name(name):
    new_user_df = pd.DataFrame(columns = user_df.columns)
    for index, user in user_df.iterrows():
        if type( re.match(name, user['name']) ) == Match[str]:
            new_user_df.insert()
            

def search_by_age():
    return 0

def search_by_opinion():
    return 0