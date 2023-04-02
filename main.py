from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup
import time
import requests

TARGET_URL = "https://store.ui.com/collections/unifi-protect/products/unifi-protect-g3-instant-camera"
WEBHOOK_URL = (
    "<Discord Webhook URL>"
)

def notify():
    webhook = DiscordWebhook(url=WEBHOOK_URL, content='@everyone Product is in stock!')
    return webhook.execute()
    print("Notified!")
def scrape():
    page = requests.get(TARGET_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    time.sleep(60)
    for div in soup.find(id="productDescriptionAndWizard").find_all("div"):
        if any("in stock" in span.text.lower() for span in div.find_all("span")):
            print("Found availability.")
            notify()
            break
    else:
        print("Out of stock.")
    scrape()


if __name__ == "__main__":
    scrape()