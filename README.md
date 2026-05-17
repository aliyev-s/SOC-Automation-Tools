# 🚀 Simple SOC IP Lookup Tool (Python + AbuseIPDB API)

## What is this?
This is a quick Python script I put together to make checking suspicious IPs a lot faster during log analysis. Instead of manually copying and pasting every weird IP from firewall or SIEM logs into a browser, this script hits the AbuseIPDB API and gives you a clean threat report right inside your terminal.

## Why I built it this way:
* **No hardcoded keys:** Sticking private API keys directly into the code is a bad security practice. I designed this script to securely load credentials from environment variables (`ABUSEIPDB_API_KEY`).
* **Built-in crash protection:** Early versions crashed when AbuseIPDB didn't return an explicit country name for private or Google DNS IPs. I fixed this by switching to the `.get()` method, so it handles missing fields gracefully without breaking the workflow.
* **Fast decision making:** It automatically flags any IP with an abuse confidence score over 20%, letting Tier-1 analysts know if they need to push a block rule immediately.

---

## How to setup and run it

### 1. Requirements
You just need Python 3 and the standard `requests` library. If you don't have it, install it via terminal:
```bash
pip install requests
```

### 2. Set your API Key
Get your free API key from AbuseIPDB, then inject it into your local environment so the script can read it securely:

* **Windows (PowerShell):**
  ```powershell
  $env:ABUSEIPDB_API_KEY="your_actual_api_key_here"
  ```
* **Linux / macOS:**
  ```bash
  export ABUSEIPDB_API_KEY="your_actual_api_key_here"
  ```

### 3. Run the Script
```bash
python ip_enrichment.py
```

---

## 📊 Quick Demo
Here is what the terminal output looks like when you feed it a known malicious IP:

```text
==================================================
   SOC Automation Tool: Threat Intel Enrichment   
==================================================
Enter suspicious IP address to analyze: 185.220.101.5

==================================================
🔍 SOC THREAT INTEL REPORT FOR IP: 185.220.101.5
==================================================
🏳️  Country      : Germany
🏢 ISP          : Unassigned
⚠️  Abuse Score  : 100%
💬 Total Reports: 14032
==================================================
🚨 ALERT: This IP is highly suspicious! Block action recommended.
==================================================
```
