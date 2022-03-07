from pyowm import OWM

owm = OWM('key')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Senador Canedo,BR')
w = observation.weather

temperatura = w.temperature('celsius')

temperatura_atual = temperatura.get('temp')
sensacao_termica = temperatura.get('feels_like')




# Este if serve para verificar se a sensação termica tiver diferença maior que 2 mostrar a sensação ao inves da temperatura verdeadeira
if sensacao_termica > temperatura_atual + 2 :
    print(sensacao_termica)

elif sensacao_termica < temperatura_atual - 2:
    print(sensacao_termica)

else:
    print(temperatura_atual)
