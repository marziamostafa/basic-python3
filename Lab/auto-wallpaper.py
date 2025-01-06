""" 
problem: download and change desktop wallpaper automatically
 """
# installing --> pip install requests

import requests
import json

api_url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# we need a library to call the api from python. we will instll request library

# get the json
response=requests.get(api_url)
content=response.content.decode('UTF-8')  # content type is bytes -(b). so we decode it. and get the string value, its not a dictionary
# print(type(content))

# convert string to json
dict_content=json.loads(content)  # loads --> load string

# get the image url
image_url=dict_content['url']
print(image_url)

# download the image
res=requests.get(image_url)
print(res)

# save the image
with open('apood.png','wb') as image: # wb--> w to turncate and write. b-> data is binary
    image.write(res.content)
