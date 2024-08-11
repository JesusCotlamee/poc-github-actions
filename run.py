### PYTHON NATIVE DEPENDENCIES
import json
from security import safe_requests

### SCRIPT SAMPLE EXECUTED THROUGH GH WORKFLOW
print(f"💡 \033[36mScript example: Getting Brazil Covid-19 datas\033[0m")

try:
  response1 = safe_requests.get("https://covid-api.mmediagroup.fr/v1/cases?country=Brazil", timeout=60)

  country_datas = response1.json()

  cases = country_datas["All"]

  print("🤒 🇧🇷 Confirmed cases:", cases["confirmed"])
  print("🥳 🇧🇷 Recovered cases:", cases["recovered"])
  print("😢 🇧🇷 Deaths:", cases["deaths"])

except:
   print("Couldn't extract Brazil cases datas") 

try:    
  response2 = safe_requests.get("https://covid-api.mmediagroup.fr/v1/vaccines?country=Brazil", timeout=60)

  vaccines_datas = response2.json()

  vaccines = vaccines_datas["All"]

  print("📦 🇧🇷 Vaccines quantity:", vaccines["administered"])
  print("💉 🇧🇷 Vaccinated people:", vaccines["people_vaccinated"])

except:
  print("Couldn't extract Brazil vaccines datas") 
  
