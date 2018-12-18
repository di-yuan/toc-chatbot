import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAKZBtEyrY6kBABdhPxerkOftrSpWFnBqQm6IqZCTXS9Yi72LBs953zv1oo2XhJYn0dSwZANZAAve4KvRh7zcBSFIlZBuGL3pmmZCyvbZAVQGZBHknv4HcxCfJlhUtIjnBsHjpWPeyZBpz61cd1ywKFGyVK20cXDb6T2KZB39ZCOySXwwZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass
def send_button_message(id, text, buttons):
    pass
"""

