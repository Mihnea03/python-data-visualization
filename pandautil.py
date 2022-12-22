import pandas as pd
import matplotlib.pyplot as plt
import re

user_df = pd.read_csv('customers.csv')

def search_by_name(name):
    new_user_df = pd.DataFrame(columns = user_df.columns)
    for index, user in user_df.iterrows():
        if re.match(name, user['name']) != None:
            new_user_df.append({
                'alpha': user['alpha'],
                'name': user['name'],
                'email': user['email'],
                'date': user['date'],
                'yn': user['yn']
            })
    print(new_user_df)
            

def search_by_age():
    return 0

def search_by_opinion():
    return 0