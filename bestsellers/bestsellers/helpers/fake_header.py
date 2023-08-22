from random import choice, randint
import requests
from bestsellers.settings import SCRAPEOPS_API_KEY

def get_user_agent_list():

  return 

def random_user_agent():
  response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=' + SCRAPEOPS_API_KEY)
  json_response = response.json()
  user_agent = json_response.get('result', [])

  random_index = randint(0, len(user_agent) - 1)
  return user_agent[random_index]
    

# Upgrade-Insecure-Requests
def upgrade_insecure_requests():
    values = ["1"]
    return choice(values)


# Accept
def accept():
    media_types = [
        "application/json",
        "application/xml",
        "text/plain",
        "image/jpeg",
        "image/png",
        "audio/mpeg",
        "video/mp4",
        "application/pdf",
        "application/octet-stream",
        "text/css",
        "application/javascript",
    ]

    data = set()
    data.add("text/html")
    for _ in range(randint(4, 8)):
        data.add(choice(media_types))

    return ",".join(list(data))


# Accept-Language
def accept_language():
    pt_BR_variations = [
        "pt-BR",
        "pt-BR,pt;q=0.9",
        "pt-BR;q=0.8,en-US;q=0.5",
        "pt-BR,en-US;q=0.7,en;q=0.3",
        "pt-BR;q=0.6,en-US;q=0.4,fr;q=0.2",
    ]

    data = set()
    for _ in range(randint(1, 3)):
        data.add(choice(pt_BR_variations))

    return ",".join(list(data))


def fake_header():
    """
    Gera um cabeçalho de requisição aleatório.
    """
    return {
        "Upgrade-Insecure-Requests": upgrade_insecure_requests(),
        "Accept": accept(),
        "Accept-Language": accept_language(),
        "Accept-Encoding": "*",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "User-Agent": random_user_agent(),
        "Referer": "https://www.instagram.com/",
    }