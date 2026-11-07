import json

def save_data( users , locked_users):
    
    with open("users.json","w") as file:
        data ={
            "users":users,
            "locked_users":list(locked_users)
        }
        json.dump(data,file)

def load_data():
    
    try:
        with open("users.json","r") as file:
            data = json.load(file)
            
        users = data["users"]
        locked_users = set(data["locked_users"])
        
        return users, locked_users
    except FileNotFoundError:
        return {},set()