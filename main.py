import time
from telegram_notify import send_telegram_message

def check_tickets():
    # Gerçek scraping burada olacak (şu an örnek)
    print("Tren koltuk durumu kontrol edildi.")
    send_telegram_message("🚄 Selçuklu → Eryaman YHT için boş koltuk bulundu!")

while True:
    check_tickets()
    time.sleep(900)  # 15 dakika
