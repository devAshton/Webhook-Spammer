import requests, colorama, time, os

def _exit():
    time.sleep(5)
    exit()

def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Invalid Webhook...\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter, WebhookAvatar):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": WebhookAvatar})
            if data.status_code == 204:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.RED}Webhook has been deleted')
    print(f'{colorama.Fore.BLUE}Finished...')

def initialize():
    print(f"""{colorama.Fore.RED}""")
    webhook = input("Enter ur webhook: ")
    name = input("Enter a webhook name: ")
    WebhookAvatar = input("Enter a avatar URL: ")
    message = input("Enter a message: ")
    delay = input("Enter a delay: ")
    amount = input("Enter an amount: ")
    deletehook = input("Delete webhook after spam? [Y/N]: ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (deletehook.lower() != "y" and deletehook.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, deletehook, WebhookAvatar)
        _exit()

if __name__ == '__main__':
    os.system('cls')
    os.system('title Webhook Spammer - by Ashton#0420')
    colorama.init()
    initialize()