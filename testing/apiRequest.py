import requests
import json
from time import sleep

baseURL = 'https://www.1secmail.com/api/v1/?action='
authBaseUrl = 'https://internshala.com/registration'
count = 1
# Get request for 1 email id
def new_func(baseURL, count):
    getEmail = requests.get(f'{baseURL}genRandomMailbox&count={count}')
    emailInJson = getEmail.json()
    email = emailInJson[0]
    return email

email = ''
while True:
    email = new_func(baseURL, count)
    if(email.find('1secmail') == -1):
        break
print(email)


# Spliting the email into login and domain
emailList = email.split('@')
login = emailList[0]
domain = emailList[1]

# input('Press any key to continue\n')

# Getting message id
getMessage = requests.get(f'{baseURL}getMessages&login={login}&domain={domain}')
messageInJson = getMessage.json()
messageID = messageInJson[1]["id"]

# Reading message with 
readMessage = requests.get(f'{baseURL}readMessage&login={login}&domain={domain}&id={messageID}')

readMessageInJson = readMessage.json()
print(readMessageInJson["date"])

# Extracting url
bodyHTML = readMessageInJson['body']
twoPartsBody = bodyHTML.split(authBaseUrl)
twoPartsBody = twoPartsBody[1]
twoPartsBody = twoPartsBody.split('"')
authLink = twoPartsBody[0]
authLink = authBaseUrl + authLink
print(authLink)


sleep(2)

