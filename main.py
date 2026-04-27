import requests
import time
import os
from datetime import datetime
from dotenv import load_dotenv

# Load secrets from a local .env file (Keep this file off GitHub!)
load_dotenv()

# --- CONFIGURATION (Environment Variables) ---
# In production, these are pulled from the server environment
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# WATCHLIST: {Coin_ID: [Target_Price, Last_Alert_Timestamp]}
# These are your Fibonacci support levels
WATCHLIST = {
    "bitcoin": [75000, 0],
    "ethereum": [2200, 0],
    "solana": [80, 0],
    "virtual-protocol": [0.68, 0],
    "pepe": [0.00000370, 0]
}

ALERT_COOLDOWN = 3600 # 1 hour cooldown to prevent notification spam
# ---------------------

def send_telegram_msg(message):
    """Broadcasts signal to the user via Telegram API."""
    if not TOKEN or not CHAT_ID:
        print("Error: Telegram credentials (TOKEN/CHAT_ID) missing!")
        return
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    try:
        requests.get(url, timeout=15)
    except Exception as e:
        print(f"Telegram broadcast failed: {e}")

print("--- ⚙️ DeFAI Price Sentinel: ACTIVE ---")

while True:
    try:
        # 1. Fetch live data from CoinGecko API
        ids = ",".join(WATCHLIST.keys())
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
        response = requests.get(url, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            now = time.time()
            print(f"\n--- 📈 Dashboard [{datetime.now().strftime('%H:%M:%S')}] ---")
            
            for coin_id, settings in WATCHLIST.items():
                if coin_id in data:
                    current_price = data[coin_id]['usd']
                    target = settings[0]
                    last_alert = settings[1]
                    
                    # 2. Calculation logic: Gap % between price and entry target
                    dist = ((current_price - target) / target) * 100
                    name = coin_id.replace("-protocol", "").upper()
                    
                    # 3. Print professional dashboard to console
                    print(f"{name.ljust(8)} | ${current_price:12.8f} | Target: {target} | Gap: {dist:+.2f}%")

                    # 4. Trigger alert if price is below target and cooldown has passed
                    if current_price <= target and (now - last_alert > ALERT_COOLDOWN):
                        msg = f"🚨 {name} BUY ALERT!\nPrice: ${current_price:.8f}\nTarget: ${target}\nGap: {dist:.2f}%\nStatus: Fibonacci Level Reached."
                        send_telegram_msg(msg)
                        WATCHLIST[coin_id][1] = now # Update alert timestamp
        
        # Stability: 2-minute sleep cycle
        time.sleep(120)

    except Exception as e:
        print(f"🔄 System Hiccup: {e}. Auto-rebooting in 60s...")
        time.sleep(60)
        
