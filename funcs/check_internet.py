import requests
def check_internet():
    try:
        requests.get('http://www.google.com', timeout=1)
        print("online")
        return True
    except:
        print("offline")
        return False