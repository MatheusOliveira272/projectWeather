import requests 
from datetime import datetime
import pytz 
import pycountry
import pycountry_convert as pc
from timezonefinder import TimezoneFinder
from model.weather_model import Weather


def obter_informacoes_climaticas(cidade):
    chave = 'a2b476eb263fa2e3dba3d4a38e8b8ebc'
    api_link_nameCity = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&units=metric&lang=pt_br'

    # Chamada da API
    r = requests.get(api_link_nameCity)

    '''if r.status_code == 200:
        dados = r.json()
    else:
        raise Exception(f"Erro ao buscar dados da API: {r.status_code}")
'''
#2304
    try:
        dados = r.json()
    except ValueError:
        raise Exception("Erro ao processar a resposta da API")

    pais_codigo = dados['sys']['country']
    latitude = dados['coord']['lat']
    longitude = dados['coord']['lon']

    # Descobrindo o fuso horário exato com timezonefinder
    tf = TimezoneFinder()
    zona_fuso = tf.timezone_at(lat=latitude, lng=longitude)
    zona = pytz.timezone(zona_fuso)
    zona_horas = datetime.now(zona).strftime("%d/%m/%Y  |  %H:%M:%S %p")

    # Nome do país e continente
    #pais = pytz.country_names[pais_codigo]2304
    pais = pycountry.countries.get(alpha_2=pais_codigo).name


    def country_to_continent(country_name):
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        return pc.convert_continent_code_to_continent_name(country_continent_code)

    continente = country_to_continent(pais)

    # Retornar os dados climáticos como dicionario
    '''return {
        'cidade': cidade,
        'pais': pais,
        'data_hora': zona_horas,
        'temperatura': dados['main']['temp'],
        'pressao': dados['main']['pressure'],
        'humidade': dados['main']['humidity'],
        'velocidade_vento': dados['wind']['speed'],
        'descricao': dados['weather'][0]['description'],
        'continente': continente
    }'''#2304
    
    # Criar objeto da classe Weather
    clima_obj = Weather(
        city=cidade,
        country=pais,
        continent=continente,
        temperature=dados['main']['temp'],
        pressure=dados['main']['pressure'],
        humidity=dados['main']['humidity'],
        wind_speed=dados['wind']['speed'],
        description=dados['weather'][0]['description'],
        date_time=zona_horas
    )

    return clima_obj
