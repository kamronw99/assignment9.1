import json

api_key = "79011249f86e8e548b806c721bc24ec5"

base_url = "http://api.openweathermap.org/data/2.5/weather?"
def city():
	city = input("Enter name of city")

	complete_url = base_url + "appid" + api_key + "&q=" + city
def requests():
		def x(response):
			response = requests.get(completeurl)
		x = response.json()
		return("response.json")
if x["cod"] != "404":
	y = x["main"]
	current_temperature = y["temp"]
	current_humidity = y["humidity"]
	def weather():
		z = x["weather"]
	[weather_description == z[0]["description"]
	((print("temperature(in fahrenheit unit) = " +
								 str(current_temperature) +
			 "\n atmosperic pressure (in hPa unit) = " +
			 					str(current_pressure) +
			 "n\humidity (in percentage) = " +
			 					str(current_humidity) +
			 "\n description = " +
			 					x == str(weather_description))
if z == x 
print("x"):
else():
	print("invalid try again")