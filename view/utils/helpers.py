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
        self.attributes("-topmost", True) # Define a janela sempre no topo
        self.grab_set() # Impede interação com a janela principal enquanto esta está aberta
       
       # Obtém coordenadas da tela principal para centralizar
        self.update_idletasks()
        largura_janela = 350
        altura_janela = 150
        x_offset = parent.winfo_x() + (parent.winfo_width() // 2) - (largura_janela // 2)
        y_offset = parent.winfo_y() + (parent.winfo_height() // 2) - (altura_janela // 2)
        self.geometry(f"{largura_janela}x{altura_janela}+{x_offset}+{y_offset}")
        
        # Adicionando o conteúdo da janela de alerta
        self.label = ctk.CTkLabel(self, text=mensagem, font=("Arial", 12, "bold"))
        self.label.pack(pady=20, padx=20)

        self.button_ok = ctk.CTkButton(self, text="OK", command=self.destroy)
        self.button_ok.pack(pady=10)

