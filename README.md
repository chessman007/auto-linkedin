# About:
This program automates the hassel of using LinkedIn the normal way.

Watch the MBAs heads' implode when you don't adhere to their social engineering.

Avoid psycological manipulation by our corporate overlords.

Save time by not clicking endlessly though LinkedIn's terrible user interface.

This program is designed to automatically connect with peers over LinkedIn given a chat history of people posting their urls.

# Instructions:

## Install chromedriver
download into ./driver/
https://sites.google.com/chromium.org/driver/downloads

## Paste chat history
paste all chat history that should be parsed into ./config/chat_history.txt

## Run
python perform_social_interactions.py -webdriver [PATH TO WEBDRIVER]
example: "python perform_social_interactions.py -webdriver ./driver/webdriver"

Further instructions will be given in the terminal...