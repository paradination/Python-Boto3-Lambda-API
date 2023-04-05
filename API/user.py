#making a dynamic functions for reusability
import requests
API_URL = "https://reqres.in/"

#REST API Function for all users
def get_all_users():
    print("getting all users........")
    response = requests.get(API_URL + "api/users")
    print("responseCode", response)
    print(response.json())
    return response.json()

#REST API get request for a user
def get_a_user(user_id):
    print("getting user", user_id)
    response = requests.get(API_URL + "api/users/" + str(user_id))
    print("responseCode", response)
    print(response.json())
    return response.json()

#REST API post request
def create_a_user(user_data):
    print ("creating a new user with details", user_data)
    response = requests.post(API_URL + "api/users" , json = user_data )
    print("responseCode", response)
    print(response.json())
    return response.json()

#update fxn
#REST API update request
def update_a_user(user_id, user_data):
    print ("updating existing user", user_id, "with", user_data)
    response = requests.put(API_URL + "api/users/" + str(user_id) , json = user_data )
    print("responseCode", response)
    print(response.json())
    return response.json()

#delete fxn
#REST API delete request
def delete_a_user(user_id):
    print ("deleting an existing user", user_id)
    response = requests.delete(API_URL + "api/users/" + str(user_id))
    print("responseCode", response)
    print(response.json())
    return response.json()