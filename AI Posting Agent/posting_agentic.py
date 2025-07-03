import random
import time
import requests
import schedule
from datetime import datetime
from openai import OpenAI

# ------------------------- Configuration -------------------------

# OpenAI API client
openai_client = OpenAI(api_key="your_openai_api_key")  # Removed for security; replace with your actual key

# Telegram Bot configuration
TELEGRAM_TOKEN = "756697873:AAH5yjnens1LRfcCdxZi1b2g3h4i5j6k7l8m9n0o"  # 🔐 Replace securely in production
CHAT_ID = 123456789  # 🔐 Replace securely in production

# Prompts for AI to generate engaging content
PROMPTS = [
    "Craft a short, punchy tweet highlighting the future impact of artificial intelligence.",
    "Share an engaging and surprising tech fact that's perfect for a Telegram post.",
    "Write a motivational tech tip that inspires developers to push their limits.",
    "Share a futuristic perspective on how robotics and automation could transform daily life.",
    "Create a brief and imaginative post on the growing influence of quantum computing.",
    "Offer a sharp, insightful line about digital privacy concerns in the age of AI (2025).",
    "Write a tweet-style post that captures the power and influence of software engineering today.",
    "Post a fun, relatable insight about life as a developer in the 2020s.",
    "Share a visionary statement about the convergence of AI, IoT, and big data.",
    "Craft a short message that sparks curiosity about the ethical implications of future tech."
]

# Optional image URL
IMAGE_URL = "https://picsum.photos/512"

# ------------------------- Core Logic -------------------------

def generate_ai_message() -> str:
    """Generates a short tech message using OpenAI."""
    try:
        prompt = random.choice(PROMPTS)
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a tech-savvy assistant who writes short, engaging tech insights."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=0.8,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[{datetime.now()}] AI generation error: {e}")
        return "🤖 AI is offline. Here's a manual tech tip: Stay curious, stay building! #Tech"

def send_to_telegram(message: str, image_url: str = None) -> None:
    """Sends a message (and optional image) to Telegram."""
    try:
        if image_url:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
            payload = {
                "chat_id": CHAT_ID,
                "caption": message,
                "photo": image_url
            }
        else:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            payload = {
                "chat_id": CHAT_ID,
                "text": message
            }

        response = requests.post(url, data=payload)
        if response.ok:
            print(f"[{datetime.now()}]  Telegram message sent successfully.")
        else:
            print(f"[{datetime.now()}] Telegram API error: {response.text}")
    except Exception as e:
        print(f"[{datetime.now()}] Telegram send error: {e}")

def run_bot() -> None:
    """Main function to generate and send AI-powered message."""
    print(f"[{datetime.now()}] Running AI Auto Poster Bot...")
    message = generate_ai_message()
    print(f"[{datetime.now()}] Generated message: {message}")
    send_to_telegram(message, image_url=IMAGE_URL)

# ------------------------- Scheduler -------------------------

if __name__ == "__main__":
    run_bot()  # Run immediately
    schedule.every(24).hours.do(run_bot)

    print("⏱Scheduling initialized. Bot will run every 24 hours.\n")

    while True:
        schedule.run_pending()
        time.sleep(10)
