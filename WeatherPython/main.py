import json
import requests

city= input("Enter Your Preferred City:")
url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key=Z9MXEFD8LLG6MPA32HTMTKJS4&contentType=json"

response=requests.get(url)
try:
  json_response= json.loads(response.text)
except Exception:
  print("\nthe input does't fits well and throws an error!")
#info variables
temp= json_response["days"][0]["temp"]
desc= json_response["days"][0]["description"]
loc=json_response["resolvedAddress"]
#more_info
humidity= json_response["days"][0]["humidity"]
sunrise= json_response["days"][0]["sunrise"]
sunset= json_response["days"][0]["sunset"]
windspeed= json_response["days"][0]["windspeed"]

def more_info():
 try:
   print("\nWould you like to see more info on this location?")
   ask=input("Enter Y to Proceed or Q to Quit:")
  
   if ask=="y":
     print(f"\nHumidity:{humidity}")
     print(f"Sunrise:{sunrise}")
     print(f"Sunset:{sunset}")
     print(f"Windspeed:{windspeed}")
   elif ask=="q":
    pass
   else:
    print("Not a valid input!")
 except Exception:
   print("\nthe input does't fits well and throws an error!")

print(f"\n{desc}")
print(f"\nCurrent Temperature: {temp}°C")
print(f"Exact Location:{loc}")
more_info()

