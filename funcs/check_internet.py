import requests
def check_internet():
    try:
        requests.get('http://www.google.com', timeout=1)
        return True
    except:
        return False