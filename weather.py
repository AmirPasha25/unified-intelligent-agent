import requests
import json
from pydantic import BaseModel
from langchain.tools import StructuredTool

class Weather():

    def __init__(self, city, state, country, startdate, enddate, frequency):
        self.website = "https://api.open-meteo.com/v1/forecast?"
        coordinate_web_link = f"https://geocode.maps.co/search?q={city},{state},{country}&api_key=Please enter your open meteo key here"
        response_1 = requests.get(coordinate_web_link).json()
        first_result = response_1[0]
        self.lat = float(first_result["lat"])
        self.lon = float(first_result["lon"])
        self.startdate = startdate
        self.enddate = enddate
        self.frequency = frequency
        self.start_point = (f"{self.website}latitude={self.lat}&longitude={self.lon}&start_date={self.startdate}&end_date={self.enddate}")
        self.c_start_point = (f"{self.website}latitude={self.lat}&longitude={self.lon}")
        self.temp_h = "temperature_2m,apparent_temperature"
        self.temp_d = "temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min"
        self.precipitation_d = "precipitation_probability_max,precipitation_hours,precipitation_sum,showers_sum,snowfall_sum,rain_sum"
        self.precipitation_h = "precipitation_probability,precipitation,rain,showers,snowfall,snow_depth"
        self.sun_radiation_d = "sunrise,sunset,daylight_duration,sunshine_duration,uv_index_max,uv_index_clear_sky_max,shortwave_radiation_sum,et0_fao_evapotranspiration"
        self.cloud_visibility_h = "cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,visibility,weather_code"
        self.wind_pressure_d = "cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,visibility,weather_code"
        self.wind_pressure_h = "wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_gusts_10m,wind_direction_10m,wind_direction_80m,wind_direction_120m,wind_direction_180m,pressure_msl,surface_pressure,vapour_pressure_deficit"
        self.current_weather_c = "temperature_2m,apparent_temperature,relative_humidity_2m,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_gusts_10m,wind_direction_10m,is_day"
        # final_link = f"{website}latitude={u_latitude}&longitude={u_longitude}&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,daylight_duration,sunset,sunshine_duration,uv_index_max,uv_index_clear_sky_max,rain_sum,snowfall_sum,showers_sum,precipitation_sum,precipitation_hours,precipitation_probability_max,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant,shortwave_radiation_sum,et0_fao_evapotranspiration&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,snow_depth,weather_code,pressure_msl,surface_pressure,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,visibility,evapotranspiration,et0_fao_evapotranspiration,vapour_pressure_deficit,wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_direction_120m,wind_direction_10m,wind_direction_80m,wind_gusts_10m,wind_direction_180m,temperature_80m,temperature_120m,temperature_180m,soil_temperature_0cm,soil_temperature_6cm,soil_temperature_18cm,soil_temperature_54cm,soil_moisture_0_to_1cm,soil_moisture_1_to_3cm,soil_moisture_3_to_9cm,soil_moisture_9_to_27cm,soil_moisture_27_to_81cm&current=relative_humidity_2m,apparent_temperature,is_day,temperature_2m,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_gusts_10m,wind_direction_10m"

    def weather_website(self, link):
        response = requests.get(link)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=1)
        else:
            return f"Error {response.status_code}: {response.text}"
        
        
    def temperature(self):
        if self.frequency == "daily":
            t_final_link = f"{self.start_point}&daily={self.temp_d}"
        else:
            t_final_link = f"{self.start_point}&hourly={self.temp_h}"
        return self.weather_website(t_final_link)

    def precipitation(self):
        if self.frequency == "daily":
            p_final_link = f"{self.start_point}&daily={self.precipitation_d}"
        else:
            p_final_link = f"{self.start_point}&hourly={self.precipitation_h}"
        return self.weather_website(p_final_link)
    
    def sun_radiation(self):
        sr_final_link = f"{self.start_point}&daily={self.sun_radiation_d}"
        return self.weather_website(sr_final_link)
    
    def cloud_visibility(self):
        cv_final_link = f"{self.start_point}&hourly={self.cloud_visibility_h}"
        return self.weather_website(cv_final_link)

    def wind_pressure(self):
        if self.frequency == "daily":
            wp_final_link = f"{self.start_point}&daily={self.wind_pressure_d}"
        else:
            wp_final_link = f"{self.start_point}&hourly={self.wind_pressure_h}"
        return self.weather_website(wp_final_link)

    def current_weather(self):
        if self.frequency == "current":
            cr_final_link = f"{self.c_start_point}&current={self.current_weather_c}"
            return self.weather_website(cr_final_link)

class WeatherInput(BaseModel):
    city: str
    state: str
    country: str
    startdate: str
    enddate: str
    frequency: str
    query_type: str


def weather_func(self, city: str, state: str, country: str, startdate: str, enddate: str, frequency: str, query_type: str):
    weather_1 = Weather(city, state, country, startdate, enddate, frequency)
    if query_type == 'temperature':
        return weather_1.temperature()
    elif query_type == 'precipitation':
        return weather_1.precipitation()
    elif query_type == 'sun_radiation':
        return weather_1.sun_radiation()
    elif query_type == 'cloud_visibility':
        return weather_1.cloud_visibility()
    elif query_type == 'wind_pressure':
        return weather_1.wind_pressure()
    elif query_type == 'current_weather':
        return weather_1.current_weather()
    
weather_tool = StructuredTool.from_function(name = "WeatherTool",
                                  func=weather_func,
                                  description= '''NOTE: YOU MUST STRICTLY CALL THIS FUNCTION FOR ANY KIND OF WEATHER DATA ...
                                  0. VARIABLE CONTAINS: 
                                    A. TEMPERATURE HOURLY CONTAINS: self.temp_h = "temperature_2m,apparent_temperature"
                                    B. TEMPERATURE DAILY CONTAINS: self.temp_d = "temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min"
                                    C. PRECIPITATION DAILY CONTAINS: self.precipitation_d = "precipitation_probability_max,precipitation_hours,precipitation_sum,showers_sum,snowfall_sum,rain_sum"
                                    D. PRECIPITATION HOURLY CONTAINS: self.precipitation_h = "precipitation_probability,precipitation,rain,showers,snowfall,snow_depth"
                                    E. SUN RADIATION DAILY CONTAINS: self.sun_radiation_d = "sunrise,sunset,daylight_duration,sunshine_duration,uv_index_max,uv_index_clear_sky_max,shortwave_radiation_sum,et0_fao_evapotranspiration"
                                    F. CLOUD VISIBILITY HOURLY CONTAINS: self.cloud_visibility_h = "cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,visibility,weather_code"
                                    G. WIND PRESSURE DAILY CONTAINS: self.wind_pressure_d = "cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,visibility,weather_code"
                                    H. WIND PRESSURE HOURLY CONTAINS: self.wind_pressure_h = "wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_gusts_10m,wind_direction_10m,wind_direction_80m,wind_direction_120m,wind_direction_180m,pressure_msl,surface_pressure,vapour_pressure_deficit"
                                    I. CURRENT WEATHER CONTAINS: self.current_weather_c = "temperature_2m,apparent_temperature,relative_humidity_2m,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_gusts_10m,wind_direction_10m,is_day"
                                  1. NOTE: YOU MUST ALWAYS PASS THESE AUGMENTS: city, state, country, startdate, enddate, frequency"
                                  2. STARTDATE SHOULD BE IN THIS FORMAT "2025-09-12", IF NO DATE OR DATE LIMIT IS MENTIONED USE TODAY'S DATE FOR TODAY'S DATE USE LLM.
                                  3. frequency SHOULD BE EITHER DAILY, HOURLY, CURRENT. YOU SHOULD CALL BASED ON THE USER'S QUERY.
                                  4. NOTE: QUERY TYPE YOU HAVE TO DECIDE WHAT IS USER ASKING FOR BASED ON THE INFO CALL SUITABLE FUNCTION
                                  5. DECIDE QUERY_TYPE FROM THIS ['temperature', 'precipitation', 'sun_radiation', 'cloud_visibility', 'wind_pressure', 'current_weather']
                                  6. MUST SELECT FREQUENCIES FROM THIS LIST ONLY ['daily', 'hourly', 'current']''', verbose = True, args_schema=WeatherInput)