from flask import Flask, render_template
app=Flask(__name__)
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
list = soup.find_all("table")
print("Number of tables on site: ",len(list))
table1 = list[3]
body = table1.find_all("tr")
head = body[0]
body_rows = body[1:]
headings = []
for item in head.find_all("th"): 
    item = (item.text).rstrip("\n")
    headings.append(item)
print(headings)
all_rows = [] 
for row_num in range(len(body_rows)): # A row at a time
    row = [] 
    for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
        aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
        row.append(aa)
    all_rows.append(row)
df = pd.DataFrame(data=all_rows,columns=headings)
print(df)
df.to_csv("main.csv")
@app.route("/")
def hello():

    return str(body_rows);
if "__name__==__main__":
    app.run(debug=True)    
# from turtle import heading
# from bs4 import BeautifulSoup
# import requests
# from flask import Flask
# import re
# app=Flask(__name__)
# import pandas as pd
# r=requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
# soup=BeautifulSoup(r.text,"html.parser")
# toFind=soup.find_all("table")
# ta=toFind[3]
# body = ta.find_all("tr")
# head = body[0]
# body_rows = body[1:]
# headings = []
# headings=[]
# cleantext = ta.text
# all_rows = [] 
# for row_num in range(len(body_rows)): # A row at a time
#     row = [] 
#     for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
#         aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
#         row.append(aa)
#     all_rows.append(row)
# df = pd.DataFrame(data=all_rows,columns=headings)
# print(cleantext)
# print(toFind[0])
# @app.route("/")
# def main():
#         return str(toFind[3])
# if "__name__==__main__":
#     app.run()        