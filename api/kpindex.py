import requests

def get_kp_index(url):
    response = requests.get(url)
    data = response.json()

    # De laatste Kp-index waarde
    latest_kp = data[-1]['kp_index']
    currert_time = data[-1]['time_tag']

    return latest_kp
