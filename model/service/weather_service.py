import requests 
from datetime import datetime
import pytz 
import pycountry
import pycountry_convert as pc
from timezonefinder import TimezoneFinder
from model.weather_model import Weather
from view.utils.helpers import alert


def obter_informacoes_climaticas(cidade):
    chave = 'a2b476eb263fa2e3dba3d4a38e8b8ebc'
    api_link_nameCity = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&units=metric&lang=pt_br'
    
    
    
    try:
        
        from view.interface import app
        resposta = requests.get(api_link_nameCity)
        resposta.raise_for_status()
        dados = resposta.json()
        
        if 'sys' not in dados or 'country' not in dados['sys']:
            raise KeyError("Cidade não encontrada!")

        pais_codigo = dados['sys']['country']
        latitude = dados['coord']['lat']
        longitude = dados['coord']['lon']

        # Descobrindo o fuso horário exato com timezonefinder
        tf = TimezoneFinder()
        zona_fuso = tf.timezone_at(lat=latitude, lng=longitude)
        zona = pytz.timezone(zona_fuso)
        zona_horas = datetime.now(zona).strftime("%d/%m/%Y  |  %H:%M:%S %p")

        # Nome do país e continente
        pais = pycountry.countries.get(alpha_2=pais_codigo).name


        def country_to_continent(country_name):
            try:
                country_alpha2 = pc.country_name_to_country_alpha2(country_name)
                country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
                return pc.convert_continent_code_to_continent_name(country_continent_code)
            except KeyError:
                alert = alert()
                alert.mainloop()  # Exibe a janela
                return None

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
        }'''
        
        
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

    except (KeyError, requests.exceptions.RequestException) as e:
            alert(app, f"Cidade não encontrada \n Verifique se o nome está digitado corretamente").mainloop()  # Mostra uma janela de erro
            return None
