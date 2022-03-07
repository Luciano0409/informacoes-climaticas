
# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75

from pyowm import OWM
#from pyowm.utils import config


# ---------- FREE API KEY examples ---------------------

owm = OWM('key')
mgr = owm.weather_manager()


# Define o local que será buscado 
#observation = mgr.weather_at_place('Palmas,BR')
#observation = mgr.weather_at_place('Goiania,BR')
observation = mgr.weather_at_place('Senador Canedo,BR')
w = observation.weather

print('Temperatura', w.temperature('celsius'))
print('Ceu', w.detailed_status)
print('Velocidade da nuvens',w.clouds)
print('Chuva',w.rain)



