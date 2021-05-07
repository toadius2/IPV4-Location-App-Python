#!/usr/bin/python
import sys
from requests import get

# Define unit system to use: ("imperial" or "metric")
UNITS 	= "metric"

# Define OWM API Key to use
OWM_API_KEY	= "95f8da3ffa9f7afcdfc91f49501f493d"

# To make the output pretty
IP_DATA	= {
	"country"		: "Country",
	"countryCode"	: "County Code",
	"region"		: "Region",
	"regionName"	: "Region Name",
	"city"			: "City     ",
	"lat"			: "Latitude",
	"lon"			: "Longitude",
	"zip"			: "Postal/Zip",
	"timezone"		: "Timezone",
	"isp"			: "ISP     ",
	"org"			: "Organization",
	"as"			: "AS     ",
	"query"			: "Query    "
}

def getObj(url):
	# Requests to API
	req = get(url)
	# Returns as JSON Object
	return req.json()

def printasDict(obj):
	# For testing, usage: printasDict(getObj(url))
	print(obj)
	return

def printWeather(obj):
	# Prints relevant, simple weather
	print(obj["weather"][0]["main"]+": "+obj["weather"][0]["description"])
	print("Current temperature: "+str(obj["main"]["temp"])+"°")
	print("Feels like: "+str(obj["main"]["feels_like"])+"°")
	print("Daily Min/Max: "+str(obj["main"]["temp_min"])+"° / "+str(obj["main"]["temp_max"])+"°")
	print("Humidity: "+str(obj["main"]["humidity"])+"%")
	return

def main(self, ip_address=""):
	# Set API/URL to use
	IP_API_URL  = "http://ip-api.com/json/"
	json_ip   = getObj(IP_API_URL+ip_address)
	# Prints the data line by line in a pretty format
	for attr in json_ip.keys():
	    if attr=="status":
	    	print(""+json_ip[attr].capitalize()+"!\n")
	    	continue
	    print(IP_DATA[attr]," "+"\t\t\t->\t",json_ip[attr])
	# To divide the output
	print("\n\nWeather:\n")
	# Get OWM weather data from lat and lon
	OWM_API_URL = "http://api.openweathermap.org/data/2.5/weather?lat="+str(json_ip["lat"])+"&lon="+str(json_ip["lon"])+"&appid="+OWM_API_KEY+"&units="+UNITS
	json_owm = getObj(OWM_API_URL)
	# Prints the data line by line in a pretty format
	#for attr in json_owm.keys():
	#    print(attr,"     "+"\t\t\t->\t",json_owm[attr])
	printWeather(json_owm)
	# Prints out google maps link
	print("\nGoogle maps: https://www.google.com.ar/maps/search/"+str(json_ip["lat"])+","+str(json_ip["lon"]))

if __name__ == "__main__":
	# Tries to get a passed argument
	try:
		arg = sys.argv[1]
	except IndexError:
		# If no argument is passed, executes it anyway and shows correct usage
		main(sys.argv[0], "")
		raise SystemExit(f"Used current IP as default. Correct usage: {sys.argv[0]} <IP_address> (without <>)")
	main(sys.argv[0], sys.argv[1])