import requests

print("🌦 Weather App - Day 29")

API_KEY = "your api key"  # ← Replace with your key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("\nEnter city name (or 'exit' to quit): ")
    if city.lower() == "exit":
        print("👋 Exiting Weather App...")
        break

    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            print(f"\n📍 City: {data['name']}")
            print(f"🌡 Temperature: {data['main']['temp']}°C")
            print(f"☁ Condition: {data['weather'][0]['description'].capitalize()}")
            print(f"💧 Humidity: {data['main']['humidity']}%")
        else:
            print("❌ City not found. Try again.")

    except Exception as e:
        print("⚠️ Error fetching data:", e)
