import os
from dhanhq import dhanhq

# Read keys from GitHub Secrets - never hardcode keys
client_id = os.environ.get("DHAN_CLIENT_ID")
access_token = os.environ.get("DHAN_ACCESS_TOKEN")

if not client_id or not access_token:
    print("Error: DHAN_CLIENT_ID and DHAN_ACCESS_TOKEN not set")
    exit()

dhan = dhanhq(client_id, access_token)

print("Bot started - Testing Dhan connection...")

# Safety: Only fetch data, NO trades yet
try:
    # NIFTY 50 security_id = 13 on NSE_EQ
    ltp_data = dhan.get_ltp_data(security_id="13", exchange_segment="NSE_EQ")
    ltp = ltp_data['data']['last_price']
    print(f"NIFTY 50 LTP: {ltp}")
    print("Dhan API connection successful ✅")
except Exception as e:
    print(f"Error: {e}")
