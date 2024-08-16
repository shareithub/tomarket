import requests
import time
from colorama import Fore, Style, init
import json
from datetime import datetime
import random
from tabulate import tabulate

# Initialize Colorama
init()

# Telegram bot setup
TELEGRAM_BOT_TOKEN = 'CHANGE YOUR TOKEN OR BLANK'
TELEGRAM_CHAT_ID = 'CHANGE YOUR CHAT ID'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,en-US;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://mini-app.tomarket.ai',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://mini-app.tomarket.ai/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': 'Android',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36',
    'x-requested-with': 'org.telegram.messenger.web'
}

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram bot token or chat ID is missing.")
        return
    
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
    }
    try:
        response = requests.post(TELEGRAM_API_URL, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send Telegram message: {e}")

def get_balance(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/user/balance'
    headers['Authorization'] = token
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

def claim_daily(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/daily/claim'
    headers['Authorization'] = token
    payload = {"game_id": "fa873d13-d831-4d6f-8aee-9cff7a1d0db1"}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def start_farming(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/farm/start'
    headers['Authorization'] = token
    payload = {"game_id": "53b22103-c7ff-413d-bc63-20f6fb806a07"}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def claim_farming(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/farm/claim'
    headers['Authorization'] = token
    payload = {"game_id": "53b22103-c7ff-413d-bc63-20f6fb806a07"}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def play_game(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/game/play'
    headers['Authorization'] = token
    payload = {"game_id": "59bcd12e-04e2-404c-a172-311a0084587d"}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def claim_game(token, point):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/game/claim'
    headers['Authorization'] = token
    payload = {"game_id": "59bcd12e-04e2-404c-a172-311a0084587d", "points": point}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def get_random_color():
    return random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])

def print_table(rows, headers):
    print(tabulate(rows, headers=headers, tablefmt='grid'))

def main():
    tokens = []
    try:
        with open('tokens.txt', 'r') as token_file:
            tokens = token_file.readlines()
    except FileNotFoundError:
        print("No tokens file found.")
        return

    last_notification_time = time.time()

    while True:
        for i, token in enumerate(tokens):
            token = token.strip()
            print(Fore.YELLOW + Style.BRIGHT + f"Processing Account {i + 1} of {len(tokens)}" + Style.RESET_ALL)
            
            rows = []
            
            balance_response = get_balance(token)
            if balance_response is not None:
                balance = float(balance_response['data'].get('available_balance'))
                balance = int(balance)  # Convert to integer to remove decimal part
                tiket = balance_response['data'].get('play_passes')
                
                rows.append([
                    Fore.YELLOW + "Balance" + Style.RESET_ALL, f"{balance}",
                    Fore.YELLOW + "Tiket" + Style.RESET_ALL, f"{tiket}"
                ])
                
                daily, daily_status_code = claim_daily(token)
                if daily_status_code == 400:
                    if daily['message'] == 'already_check':
                        day = daily['data']['check_counter']
                        point = daily['data']['today_points']
                        message = f"Account {i+1}: Daily - Day {day} Already checkin | {point} Points"
                        send_telegram_message(message)
                        rows.append([
                            Fore.RED + "Daily" + Style.RESET_ALL, f"Day {day} Already checkin | {point} Points"
                        ])
                    else:
                        message = f"Account {i+1}: Daily - Failed {daily}"
                        send_telegram_message(message)
                        rows.append([
                            Fore.RED + "Daily" + Style.RESET_ALL, f"Failed {daily}"
                        ])
                elif daily_status_code == 200:
                    day = daily['data']['check_counter']
                    point = daily['data']['today_points']
                    message = f"Account {i+1}: Daily - Day {day} Claimed | {point} Points"
                    send_telegram_message(message)
                    rows.append([
                        Fore.GREEN + "Daily" + Style.RESET_ALL, f"Day {day} Claimed | {point} Points"
                    ])
                else:
                    message = f"Account {i+1}: Daily - Failed {daily}"
                    send_telegram_message(message)
                    rows.append([
                        Fore.RED + "Daily" + Style.RESET_ALL, f"Failed {daily}"
                    ])

                farming, farming_status_code = start_farming(token)
                if farming_status_code == 200:
                    end_time = datetime.fromtimestamp(farming['data']['end_at'])
                    remaining_time = end_time - datetime.now()
                    hours, remainder = divmod(remaining_time.total_seconds(), 3600)
                    minutes, _ = divmod(remainder, 60)
                    message = f"Account {i+1}: Farming - Started. Claim in: {int(hours)} hours {int(minutes)} minutes"
                    send_telegram_message(message)
                    rows.append([
                        Fore.GREEN + "Farming" + Style.RESET_ALL, f"Started. Claim in: {int(hours)} hours {int(minutes)} minutes"
                    ])
                    
                    if datetime.now() > end_time:
                        claim_response, claim_status_code = claim_farming(token)
                        if claim_status_code == 200:
                            poin = claim_response["data"]["claim_this_time"]
                            message = f"Account {i+1}: Farming - Success Claim Farming! Reward: {poin}"
                            send_telegram_message(message)
                            rows.append([
                                Fore.GREEN + "Farming" + Style.RESET_ALL, f"Success Claim Farming! Reward: {poin}"
                            ])
                        else:
                            message = f"Account {i+1}: Farming - Failed to claim farming: {claim_response}"
                            send_telegram_message(message)
                            rows.append([
                                Fore.RED + "Farming" + Style.RESET_ALL, f"Failed to claim farming: {claim_response}"
                            ])
                elif farming_status_code == 500:
                    if farming['message'] == 'game already started':
                        end_time = datetime.fromtimestamp(farming['data']['end_at'])
                        remaining_time = end_time - datetime.now()
                        hours, remainder = divmod(remaining_time.total_seconds(), 3600)
                        minutes, _ = divmod(remainder, 60)
                        message = f"Account {i+1}: Farming - Already Started. Claim in: {int(hours)} hours {int(minutes)} minutes"
                        send_telegram_message(message)
                        rows.append([
                            Fore.CYAN + "Farming" + Style.RESET_ALL, f"Already Started. Claim in: {int(hours)} hours {int(minutes)} minutes"
                        ])
                        
                        if datetime.now() > end_time:
                            claim_response, claim_status_code = claim_farming(token)
                            if claim_status_code == 200:
                                poin = claim_response["data"]["claim_this_time"]
                                message = f"Account {i+1}: Farming - Success claim farming! Reward: {poin}"
                                send_telegram_message(message)
                                rows.append([
                                    Fore.GREEN + "Farming" + Style.RESET_ALL, f"Success claim farming! Reward: {poin}"
                                ])
                            else:
                                message = f"Account {i+1}: Farming - Failed to claim farming: {claim_response}"
                                send_telegram_message(message)
                                rows.append([
                                    Fore.RED + "Farming" + Style.RESET_ALL, f"Failed to claim farming: {claim_response}"
                                ])
                    else:
                        message = f"Account {i+1}: Farming - Error. {farming}"
                        send_telegram_message(message)
                        rows.append([
                            Fore.RED + "Farming" + Style.RESET_ALL, f"Error. {farming}"
                        ])
                else:
                    message = f"Account {i+1}: Farming - Error {farming}"
                    send_telegram_message(message)
                    rows.append([
                        Fore.RED + "Farming" + Style.RESET_ALL, f"Error {farming}"
                    ])
                
                while tiket > 0:
                    play, play_status = play_game(token)
                    if play_status != 200:
                        message = f"Account {i+1}: Game - Failed to start game!"
                        send_telegram_message(message)
                        rows.append([
                            Fore.RED + "Game" + Style.RESET_ALL, "Failed to start game!"
                        ])
                    else:
                        message = f"Account {i+1}: Game - Game Started!"
                        send_telegram_message(message)
                        rows.append([
                            Fore.GREEN + "Game" + Style.RESET_ALL, "Game Started!"
                        ])
                        for _ in range(30):
                            time_left = 30 - _
                            rows.append([
                                Fore.CYAN + "Game" + Style.RESET_ALL, f"Playing game, waktu sisa {time_left} detik"
                            ])
                            time.sleep(1)
                        point = random.randint(400, 600)
                        claim, claim_status = claim_game(token, point)
                        if claim_status != 200:
                            message = f"Account {i+1}: Game - Failed to claim game points!"
                            send_telegram_message(message)
                            rows.append([
                                Fore.RED + "Game" + Style.RESET_ALL, "Failed to claim game points!"
                            ])
                        else:
                            message = f"Account {i+1}: Game - Success. Mendapatkan {point} Poin"
                            send_telegram_message(message)
                            rows.append([
                                Fore.GREEN + "Game" + Style.RESET_ALL, f"Success. Mendapatkan {point} Poin"
                            ])

                        tiket -= 1

            print_table(rows, headers=["Status", "Message"])
        
        print(Fore.BLUE + Style.BRIGHT + f"\nALL YOUR ACCOUNT SUCCESS" + Style.RESET_ALL)
        for _ in range(1800):
            minutes, seconds = divmod(1800 - _, 60)
            message = f"Next looping delay {minutes} minutes {seconds} second"
            if time.time() - last_notification_time >= 600:
                send_telegram_message(message)
                last_notification_time = time.time()
            print(Fore.CYAN + Style.BRIGHT + f"Next looping {minutes} minutes {seconds} seconds ]" + Style.RESET_ALL, end="\r", flush=True)
            time.sleep(1)

if __name__ == "__main__":
    main()
