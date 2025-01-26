from PIL import Image
import customtkinter as ctk
import pycountry_convert as pc
from customtkinter import CTkImage
from deep_translator import GoogleTranslator

def traduzir_texto(texto, idioma_destino="pt"):
    return GoogleTranslator(source="auto", target=idioma_destino).translate(texto)


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

class alert(ctk.CTkToplevel):
    def __init__(self,parent, mensagem="Erro!", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Aviso")
        self.geometry("350x150")
        self.resizable(False, False)
        
        self.transient(parent)  # Mantém a relação com a janela principal

       # Define a janela sempre no topo
        self.attributes("-topmost", True)
       

        # Impede interação com a janela principal enquanto esta está aberta
        self.grab_set()

        # Adicionando o conteúdo da janela de alerta
        self.label = ctk.CTkLabel(self, text=mensagem, font=("Arial", 12, "bold"))
        self.label.pack(pady=20, padx=20)

        self.button_ok = ctk.CTkButton(self, text="OK", command=self.destroy)
        self.button_ok.pack(pady=10)

