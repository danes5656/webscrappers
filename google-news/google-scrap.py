# Importing libraries
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import tkinter
from tkinter import *

# Shared locations
root = r'/Users/eduardotorres/Documents'
sl = r'/'
base_location = ''.join(
    [root, sl, r'GitHub/python-development/personal-projects/nba-predictions'])
os.chdir(base_location)
print(os.getcwd())
add_ins = ''.join([root, sl, r'stuff'])

# Starting with the project
service = Service()
options = Options()
options.add_argument('headless')

executable_chrome = ''.join([add_ins, sl, r'chromedriver'])
driver = webdriver.Chrome(executable_path=executable_chrome)

# Main function to go to google
def chatbot_response(query):
    try:
        driver.get(f'https://www.google.com/search?=' + query + '&hl=en')
        content = driver.find_elements(
            by=By.CLASS_NAME, value='xpopen').get_attribute('innerText')
        response = content.split('\n')[1]
    except:
        print('Nothing to display')
        response = None

    return response


# Creating GUI
def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state = NORMAL)

        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground = '#442265', font = ("Verdana", 12))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: "+ res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Googlebot")
base.geometry("400x500")
base.resizable(width = FALSE, height = FALSE)

# Create chat window
ChatLog = Text(base, bd = 0, bg = "white", height = "8", width = "50", font = "Arial", )
ChatLog.config(state = DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command = ChatLog.yview, cursor = "heart")
ChatLog['yscrollcommand'] = scrollbar.set 

# Create Button to send message
SendButton = Button(base, font = ("Verdana", 12, 'bold'), text = "Enter", width = "12", height = 5, 
                    bd = 0, bg = "#32de97", activebackground = "#3c9d9b", fg = '#ffffff',
                    command = send)

# Create the box to enter message
EntryBox = Text(base, bd = 0, bg = "white", width = "29", height = "5", font = "Arial")

# Place all components on the screen
scrollbar.place(x = 376, y = 6, height = 386)
ChatLog.place(x = 6, y = 6, height = 386, width = 370)
EntryBox.place(x = 128, y = 401, height = 90, width = 265)
SendButton.place(x = 6, y = 401, height = 90)
base.mainloop()

































