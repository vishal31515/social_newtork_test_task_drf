import os
import json
import requests
import re

BASE_URL="http://localhost:8000"

## User Sign up

while True:
    first_name = input('enter first name ')
    if first_name:
        break
    else:
        print('First Name field cant be empty')
while True:
    last_name = input('enter last name ')
    if last_name:
        break
    else:
        print('Last Name field cant be empty')
while True:
    email = input('enter email ')
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if email and (re.fullmatch(regex, email)):
        break
    else:
        print('Enter valid Email')
while True:
    password = input('Enter password ')
    if password:
        break
    else:
        print('Password field cant be empty')
url = f"{BASE_URL}/api/sign-up"
data = {"first_name":first_name,"last_name":last_name,"email":email,"username":email,"password":password}
response = requests.post(url,data = data)
if(response.ok):
    result = json.loads(response.content)
    if result['status'] == 201:
        print(f"\nPlease use these credentials for login email = {email} password = {password}\n")
    else:
        print("Something went wrong!! Please try again")
else:
    response.raise_for_status()



## For Login User
while True:
    email = input('enter email ')
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if email:
        break
    else:
        print('Enter valid Email')
while True:
    password = input('enter password ')
    if password:
        break
    else:
        print('Password field cant be empty')
url = f"{BASE_URL}/api/token/"
data = {"username":email,"password":password}
response = requests.post(url,data =data)
if(response.ok):
    jData = json.loads(response.content)
    if "access" in jData:
        access_token = jData["access"]
        # print(jData["access"])
else:
    print('Invalid credentials.Please try again')
    response.raise_for_status()



## For Post creation
print('\nCreate your post here\n')
while True:
    title = input("Enter Post Title: ")
    if title:
        break
    else:
        print("title can't be empty")
description = input("Enter description: ")
url = f"{BASE_URL}/api/post"
data = {"title":title,"description":description}
headers = {"Authorization":f"Bearer {access_token}"}
response = requests.post(url,data = data,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    if jData["status"]==201:
        print("Post created successfully")
    else:
        print("Something wrong!!")
else:
    print('Enterd data did not match to any User')
    response.raise_for_status()



## For Viewing all posts]
url = f"{BASE_URL}/api/post"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.get(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print(jData["data"])
    print("\n\n")

else:
    response.raise_for_status()



## For Like/Dislike Post
print('Like/Dislike post according to its post id')
while True:
    post = input("Enter post id ")
    try:
        val = int(post)
        break;
    except ValueError:
        print("Please enter a valid id")
url = f"{BASE_URL}/api/like-dislike"
headers = {'Authorization':f'Bearer {access_token}'}
data = {
    "post":post
}
response = requests.post(url,data = data,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print(key,jData[key])
else:
    response.raise_for_status()



## For viewing single user post
print('View post by post ID')
while True:
    params = input("Enter post id ")
    try:
        val = int(params)
        break;
    except ValueError:
        print("Please enter a valid id")

url = f"{BASE_URL}/api/post/{params}"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.get(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    if "data" in jData:
        print(jData["data"])
        print("\n")
else:
    response.raise_for_status()


## For Delete post
print('Delete post according to its post id')
while True:
    params = input("Enter post id ")
    try:
        val = int(params)
        break;
    except ValueError:
        print("Please enter a valid id")
url = f"{BASE_URL}/api/post/{params}"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.delete(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    if jData["status"]==200:
        print("Post successfully deleted")
    else:
        print("Something went wrong!!")

else:
    response.raise_for_status()