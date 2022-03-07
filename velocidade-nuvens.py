from pyowm import OWM

owm = OWM('key')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Senador Canedo,BR')
w = observation.weather

print( w.clouds)