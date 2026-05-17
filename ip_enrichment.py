import requests
import json
import os

# Professional Approach: API key is loaded securely from environment variables
# Locally, you can set this variable or replace 'YOUR_API_KEY_HERE' for quick testing.
API_KEY = os.getenv('ABUSEIPDB_API_KEY', 'YOUR_API_KEY_HERE')

def check_ip(ip_address):
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    querystring = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    
    try:
        if API_KEY == 'YOUR_API_KEY_HERE':
            print("❌ Error: API Key not configured. Please set the ABUSEIPDB_API_KEY environment variable.")
            return
            
        # Sending request to AbuseIPDB Threat Intel Database
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            data = response.json()['data']
            
            ip = data.get('ipAddress', ip_address)
            country = data.get('countryName', 'Unknown/Private')
            isp = data.get('isp', 'Unknown ISP')
            score = data.get('abuseConfidenceScore', 0)
            total_reports = data.get('totalReports', 0)
            
            print("\n" + "="*50)
            print(f"🔍 SOC THREAT INTEL REPORT FOR IP: {ip}")
            print("="*50)
            print(f"🏳️  Country      : {country}")
            print(f"🏢 ISP          : {isp}")
            print(f"⚠️  Abuse Score  : {score}%")
            print(f"💬 Total Reports: {total_reports}")
            print("="*50)
            
            if score > 20:
                print("🚨 ALERT: This IP is highly suspicious! Block action recommended.")
            else:
                print("✅ CLEAR: No malicious activity detected for this IP.")
            print("="*50 + "\n")
            
        else:
            print(f"❌ Error: Received status code {response.status_code} from API.")
    except Exception as e:
        print(f"❌ Script Error: {e}")

if __name__ == "__main__":
    print("\n==================================================")
    print("   SOC Automation Tool: Threat Intel Enrichment   ")
    print("==================================================")
    ip = input("Enter suspicious IP address to analyze: ")
    check_ip(ip)
