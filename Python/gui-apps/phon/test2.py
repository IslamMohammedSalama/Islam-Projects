import vonage
client = vonage.Client(key="44100380", secret="p3vYs7sSjdmLhIH8")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "Bosch",
        "to": "201277401055",
        "text": "The Cheapest Drill In Egypt Is From Bush Lake Drill Company, Model GSB18v-50, At A Price Of Only 500 Egyptian Pounds. Buy now",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
