import json
import re
import numpy as np
import pandas as pd
import sklearn 
import matplotlib
from matplotlib import pyplot as plt

# df=pd.read_csv("data.csv",encoding='utf-8',delimiter=';')

# По умолчанию open() на Питоне 3 использует locale.getpreferredencoding(False) 
# кодировку (к примеру, cp1251 на русской Винде). Чтобы прочитать файл, 
# закодированный в utf-8, необходимо явно кодировку передать:
with open("data.json", "r",encoding='utf-8') as read_file:
    data = json.load(read_file)

data["history"]["columns"]
data["history"]["data"]

df=pd.DataFrame(data["history"]["data"],columns=data["history"]["columns"])

# использую апимоех
import requests
import apimoex

with requests.Session() as session:
    data = apimoex.get_board_history(session, 'SNGSP')
    df = pd.DataFrame(data)
    df.set_index('TRADEDATE', inplace=True)
    print(df.head(), '\n')
    print(df.tail(), '\n')
    df.info()