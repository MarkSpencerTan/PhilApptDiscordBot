import requests
import time
from discord import Webhook, RequestsWebhookAdapter

discord_webhook="<DISCORD_WEBHOOK>"

def find_appointments():
    from_date = "2021-06-04"
    to_date = "2021-12-31"
    site_id = "43"

    url = 'https://www.passport.gov.ph/appointment/timeslot/available?fromDate={from_date}&toDate={to_date}&siteId={site_id}&requestedSlots=1'.format(from_date=from_date, to_date=to_date, site_id=site_id)
    x = requests.post(url)

    while True:
        found_availability = False
        for slot in x.json():
            if slot.get("IsAvailable"):
                found_availability = True
                print("found available slot!")
                send_notification()
                # sleep for an hour before checking again
                time.sleep(3600)
        if not found_availability:
            print("no availability found ... retrying in 1 minute")
            time.sleep(60)

def send_notification():
    webhook = Webhook.from_url(discord_webhook, adapter=RequestsWebhookAdapter())
    webhook.send("found appointment availability!")
    print("notification sent!")

if __name__ == "__main__":
    find_appointments()