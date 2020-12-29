def getweather(cidade):
    import requests, json
    api_key = "664367e647856a4566da835890486c86"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = cidade
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"] - 273.15
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        id = x['id']
        context = {"temperatura":round(current_temperature,2),\
        "pressao":current_pressure,\
        "umidade":current_humidiy,"descricao":weather_description, "ID":id}
        return context
    else:
        return "error"
