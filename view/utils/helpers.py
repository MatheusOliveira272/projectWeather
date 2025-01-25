from PIL import Image
import pycountry_convert as pc
from customtkinter import CTkImage

def carregar_imagem(caminho, tamanho=(100, 100)):
    try:
        img = Image.open(caminho)
        ctk_image = CTkImage(light_image=img, size=tamanho)
        return ctk_image
    except FileNotFoundError:
        print(f"Imagem {caminho} não encontrada.")
        return None


'''def country_to_continent(country_code):
    try:
        country_name = pc.country_alpha2_to_country_name(country_code)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        return pc.convert_continent_code_to_continent_name(continent_code)
    except KeyError:
        return "Desconhecido"
'''
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def meters_per_second_to_kmh(speed_mps):
    return speed_mps * 3.6
