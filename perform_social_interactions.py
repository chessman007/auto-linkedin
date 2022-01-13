import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import argparse



url_match = r'(http[s]?://)?(www.)?linkedin.com/\S*'

def scope_out_friendlist():
    with open("./config/chat_history.txt",'r') as file:
        return [x.group(0) for x in re.finditer(url_match, file.read())]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-webdriver', help='Path to web driver')
    args = parser.parse_args()

    driver = webdriver.Chrome(args.webdriver)

    person_urls = scope_out_friendlist()

    driver.get("https://www.linkedin.com/login")

    input("Press any key when you have logged into LinkedIn")

    for person_url in person_urls:
        print(person_url)
        driver.get(person_url)
        # buttons = driver.find_elements_by_class_name('artdeco-button')
        buttons = driver.find_elements(By.CLASS_NAME, 'artdeco-button')
        for b in buttons:
            if b.text == "Pending": break
            if b.text == "Connect":
                input('\tHuman confirmed, any key to shake hands. Ctrl-C to panic')
                b.click()
                driver.implicitly_wait(1) # scuffed but what isnt amiright
                # send_buttons = driver.find_elements_by_class_name('ml1')
                send_buttons = driver.find_elements(By.CLASS_NAME,'ml1')
                for s in send_buttons:
                    if s.text == "Send":
                        s.click()
        input("\tProcess for this human complete.\nPress any key to make another friend\n")


    

if __name__ == "__main__":
    main()
