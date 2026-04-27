# defai-price-sentinel
Python-based market monitor with real-time Telegram alerts and Fibonacci Gap analysis.
# DeFAI Price Sentinel 🛡️

An autonomous, cloud-native monitoring agent built in Python to track cryptocurrency price action against Fibonacci-based entry zones. 

# 🚀 Overview
The **DeFAI Price Sentinel** is designed for high-uptime market surveillance. It tracks specific assets and calculates the "Gap Percentage" between the current market price and technical support levels, delivering real-time signals via the Telegram Bot API.

### Key Features
- **Multi-Asset Dashboard**: Real-time tracking of BTC, ETH, SOL, and ecosystem tokens like VIRTUAL and PEPE.
- **Gap Analysis**: Automated calculation of the distance (%) to your Fibonacci entry targets.
- **Cloud-Optimized**: Designed for 24/7 execution on headless servers (e.g., PythonAnywhere).
- **Security-First**: Uses environment variables (`.env`) to protect API credentials and private keys.
- **Anti-Spam Logic**: Integrated alert cooldowns to ensure high-signal notifications.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Infrastructure**: PythonAnywhere (Cloud Deployment)
- **APIs**: CoinGecko API, Telegram Bot API
- **Libraries**: `requests`, `python-dotenv`, `datetime`

## 📦 Installation & Setup
1. **Clone the Repo**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/defai-price-sentinel.git](https://github.com/YOUR_USERNAME/defai-price-sentinel.git)
   
