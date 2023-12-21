import time
import requests
import json
from colorama import Fore, init
import pyfiglet
import uuid

init()

url = "https://api.discord.gx.games/v1/direct-fulfillment"

headers = {
    "Content-Type": "application/json",
    "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
}
payload = {"partnerUserId": str(uuid.uuid4())}

print(pyfiglet.figlet_format("OPERA GEN"))

while True:
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        # yay coool succesful
        if response.status_code == 200:
            # now we get that token shit
            token = json.loads(response.text)['token']
            # we do that shit in response.txt
            with open('codes.txt', 'a') as file:
                file.write("https://discord.com/billing/partner-promotions/1180231712274387115/" + token + '\n')
            # now let the goblin know
            print(Fore.GREEN + "+ Code generated successfully.")
        elif response.status_code == 429:
            retry_after = response.headers.get('Retry-After', 60) # defaulting to 60 seconds
            print(Fore.YELLOW + "- Too many requests. Waiting for: " + str(retry_after) + " seconds.")
            time.sleep(float(retry_after)) # then try the request again
        else:
            print(Fore.RED + "- Failed to generate a code. Status code: " + str(response.status_code))
    except Exception as e:
        print(Fore.RED + "- An error occurred: " + str(e)) # fuck
    finally:
        # 1 sec delay thing
        time.sleep(0)

# reset the colorama thingy idfk
print(Fore.RESET)
