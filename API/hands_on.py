import requests

#applied functions in the module
#print(dir(requests))

#REST API to get all users
response = requests.get("https://reqres.in/api/users")
print("responseCode", response)
print(response.json())

#REST API get request for a user
response = requests.get("https://reqres.in/api/users/5")
print("responseCode", response)
print(response.json())


#REST API post request
response = requests.post("https://reqres.in/api/user" , json = { "name": "ag-popin", "job": "learner"} )
print("responseCode", response)
print(response.json())

import user

user.get_a_user(4)

user.create_a_user({ "name": "ag-popin1", "job": "learner"})

user.update_a_user(2, {
    "name": "morpheus",
    "job": "zion resident"
})