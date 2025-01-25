import requests 
from datetime import datetime
import pytz 
import pycountry_convert as pc
from timezonefinder import TimezoneFinder



def informacao(i):
        
    chave  = 'a2b476eb263fa2e3dba3d4a38e8b8ebc'
    city = i
    api_link_nameCity = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={chave}&units=metric&lang=pt_br'

    # Chamada da API
    r = requests.get(api_link_nameCity)

    if r.status_code == 200:
        dados = r.json()
    else:
        print("Erro ao buscar dados da API:", r.status_code)
        exit()

    # Obtendo zona, país e horas
    pais_codigo = dados['sys']['country']
    print(f"Código do país: {pais_codigo}")

    # Zona de fuso horário
    #zona_fuso = pytz.country_timezones.get(pais_codigo, ["UTC"])
    #print(f"Fuso horário: {zona_fuso}")

    # Obtendo latitude e longitude
    latitude = dados['coord']['lat']
    longitude = dados['coord']['lon']
    print(f"Coordenadas: Latitude {latitude}, Longitude {longitude}")

    # Descobrindo o fuso horário exato com timezonefinder
    tf = TimezoneFinder()
    zona_fuso = tf.timezone_at(lat=latitude, lng=longitude)
    print(f"Fuso horário detectado: {zona_fuso}")


    # Nome do país
    pais = pytz.country_names[pais_codigo]
    print(f"País: {pais}")

    # Obter a hora local
    zona = pytz.timezone(zona_fuso)
    zona_horas = datetime.now(zona).strftime("%d/%m/%Y  |  %H:%M:%S %p")
    print(f"Data e hora local: {zona_horas}")

    # Obter dados climáticos
    temp = dados['main']['temp']
    pressao = dados['main']['pressure']
    humidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']

    print(f"Temperatura: {temp}°C")
    print(f"Pressão: {pressao} hPa")
    print(f"Humidade: {humidade}%")
    print(f"Velocidade do vento: {velocidade} m/s")
    print(f"Descrição do tempo: {descricao.capitalize()}")


    import pycountry_convert as pc

  
    def country_to_continent(country_name):
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name

    # Example
    country_name = pais
    print("eu" + country_to_continent(country_name))
    continente = country_to_continent(country_name)

    
    
    # Retornando um dicionário com as informações
    return {
        'cidade': city,
        'pais': pais,
        'data_hora': zona_horas,
        'temperatura': temp,
        'pressao': pressao,
        'humidade': humidade,
        'velocidade_vento': velocidade,
        'descricao': descricao,
        'continente': continente
    }