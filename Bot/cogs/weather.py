
import discord
import requests
from discord.ext import commands
import aiohttp
from pyowm.owm import OWM
import asyncio
import string
import time
from datetime import datetime
owm = OWM('e23d176604fddf1d3ebb331e26301395')

def setup(client):
    client.add_cog(Weather(client))

class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def weather(self, ctx, *, place):
        ' '.join(place)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place) 
        ############################################################################################ 
        weather = observation.weather
        temperature = weather.temperature(unit = 'fahrenheit')
        humidity = weather.humidity
        air_pressure = weather.pressure
        wind = weather.wind(unit = 'miles_hour')
        visibility = weather.visibility_distance
        ############################################################################################
        sunrise = datetime.utcfromtimestamp(weather.sunrise_time(timeformat = 'unix') + weather.utc_offset).strftime('%#I:%M %p')
        sunset = datetime.utcfromtimestamp(weather.sunset_time(timeformat = 'unix') + weather.utc_offset).strftime('%#I:%M %p')
        ############################################################################################


        embed = discord.Embed(
            title = f"Weather in {string.capwords(place)}",
            description = ":cloud: " + weather.detailed_status.capitalize() + " :cloud:",
            color = ctx.author.color
        )
        embed.add_field(name = 'Temperature', value = f"""
            :thermometer: {round(temperature['temp'], 1)} °F
            :sunny: Feels like {round(temperature['feels_like'], 1)} °F
            :small_red_triangle: {round(temperature['temp_max'], 1)} °F
            :small_red_triangle_down: {round(temperature['temp_min'], 1)} °F""")
        embed.add_field(name = 'Extra Info', value = f"""
            :droplet: Humidity: {humidity}%
            :cloud_tornado: Air pressure: {air_pressure['press']}
            :wind_blowing_face: Wind speed: {round(wind['speed'], 0)}mph
            :compass: Bearing: {round(wind['deg'], 0)}°
            :telescope: Visibility distance: {visibility} meters""")
        embed.add_field(name = 'Sunrise and Sunset', value = f"""
            :sunrise: Sunrise: {sunrise}
            :city_sunset: Sunset: {sunset}""") 
        
        await ctx.send(embed = embed)