import requests

def send_message(ACCESS_TOKEN,mes):

    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    Data = {
        "message": (None, "\n" + ''.join(mes) )
    }
    #return Data 
    requests.post(
        "https://notify-api.line.me/api/notify",
        headers=headers,
        data=Data,
    )


