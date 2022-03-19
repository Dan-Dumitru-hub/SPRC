# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #ex1
    URL='https://sprc.dfilip.xyz/lab1/task1/check?nume=Tipa Dan-Dumitru&grupa=343C3'
    headers = {'secret2': 'SPRCisBest'}
    r = requests.post(URL, data = {'secret' : 'SPRCisNice'},headers=headers )
    print(r.content)

    #ex2
    URL = 'https://sprc.dfilip.xyz/lab1/task2'
    data = {'username':'sprc', 'password':'admin', 'nume':'Tipa Dan-Dumitru'}
    r = requests.post(URL, data=json.dumps(data))
    print(r.content)

    #ex3
    URL = 'https://sprc.dfilip.xyz/lab1/task3/login'
    URL1 = 'https://sprc.dfilip.xyz/lab1/task3/check'
    data = {'username': 'sprc', 'password': 'admin', 'nume': 'Tipa Dan-Dumitru'}

    r = requests.Session()
    s=r.post(URL,data=json.dumps(data))
    print(s.text)
    s=r.get(URL1)
    print(s.text)

   # r1 = requests.get(URL)
   # print(r1.content)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
