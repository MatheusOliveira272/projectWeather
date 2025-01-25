import datetime
import customtkinter as ctk
from view.utils.helpers import carregar_imagem
from model.service.weather_service import obter_informacoes_climaticas
import os
from customtkinter import CTkImage
from PIL import Image


ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Sistema de Clima')
app.geometry('350x300')

campo_local = ctk.CTkEntry(app, placeholder_text="Digite o local", width=200, height=30, font=("Arial", 13))
campo_local.grid(row=1, column=0, columnspan=1, pady=10, padx=10)

        
def buscar_clima():
    cidade = campo_local.get().strip()  # Obtém o nome da cidade
    if cidade:  # Verifica se a cidade foi informada
        dados_clima = obter_informacoes_climaticas(cidade)  # Chama a API e obtém os dados
        if dados_clima:  # Verifica se os dados não são None
            atualizar_interface(dados_clima)  # Passa os dados para a interface
        else:
            print("Erro ao obter os dados da cidade.")  # Erro ao obter os dados
    else:
        print("Por favor, insira o nome de uma cidade.")
               

button_search = ctk.CTkButton(app, text='Buscar', command=buscar_clima, width=100, height=30, font=("Arial", 13))
button_search.grid(row=1, column=1, pady=10, padx=10)

#2304
caminho_imagem_sol = os.path.join(os.path.dirname(__file__), 'images/sol.png')
image_sol = carregar_imagem(caminho_imagem_sol)

caminho_imagem_lua = os.path.join(os.path.dirname(__file__), 'images/lua.png')
image_lua = carregar_imagem(caminho_imagem_lua)

frame_inferior = ctk.CTkFrame(app, fg_color=None)
frame_inferior.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0,10))
app.grid_rowconfigure(3, weight=1)  # Configurar linha para expandir
app.grid_columnconfigure(0, weight=1)  # Configurar coluna para expandir

label_cidade = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 18), pady=20)#2304
label_cidade.grid(row=3, column=0, columnspan=2, padx=10, sticky="w")

label_data = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 12), pady=5)
label_data.grid(row=4, column=0, padx=10, sticky="w")

label_hum_simb = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 13))
label_hum_simb.grid(row=5, column=0, padx=70, pady=0, sticky="nw" )

label_hum_nome = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 10))
label_hum_nome.grid(row=5, column=0, padx=70, pady=0,  sticky="sw")

label_pressao = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 12))
label_pressao.grid(row=6, column=0, padx=10, sticky="w")

label_veloc_vento = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 12))
label_veloc_vento.grid(row=7, column=0, padx=10, sticky="w")

label_humidade = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 45))
label_humidade.grid(row=5, column=0,  padx=10, sticky="w")

label_desc_tempo = ctk.CTkLabel(frame_inferior, text='', font=("Helvetica", 14, "bold"), justify= 'center')
label_desc_tempo.grid(row=7, column=1, padx=0, pady=0, sticky="w")

def atualizar_interface(clima):
    label_cidade.configure(text=f'{clima.city} - {clima.country} / {clima.continent}')
    label_data.configure(text=clima.date_time)
    label_humidade.configure(text=str(clima.humidity))
    label_pressao.configure(text=f'Pressão: {clima.pressure} hPa')
    label_veloc_vento.configure(text=f'Velocidade do vento: {clima.wind_speed} m/s')
    label_desc_tempo.configure(text=clima.description.capitalize())
    label_hum_simb.configure(text='%')
    label_hum_nome.configure(text='Humidade')

    # Vamos assumir que clima.date_time já possui a data/hora corretamente formatada
    hora_atual = clima.date_time  # Exemplo: "23/01/2025 | 17:09:50 PM"

    # Converter string para objeto datetime
    hora_atual = int(clima.date_time.split("|")[1].split(":")[0])
   
    # Baseado no horário, escolhemos a imagem (dia ou noite)
    if 6 <= hora_atual < 18:
        label_imagem = ctk.CTkLabel(frame_inferior, text='', image=image_sol, fg_color="transparent")
        label_imagem.place(x=190, y=65)
        frame_inferior.configure(fg_color="lightblue")
        texto_cor = "black"
    else:
        label_imagem = ctk.CTkLabel(frame_inferior, text='', image=image_lua, fg_color="transparent")
       # label_imagem.place(x=200, y=30)
        label_imagem.place(x=190, y=65)
        frame_inferior.configure(fg_color="darkblue")
        texto_cor = "white"

    # Atualizar cores dos textos
    label_cidade.configure(text_color=texto_cor)
    label_data.configure(text_color=texto_cor)
    label_humidade.configure(text_color=texto_cor)
    label_hum_simb.configure(text_color=texto_cor)
    label_hum_nome.configure(text_color=texto_cor)
    label_pressao.configure(text_color=texto_cor)
    label_veloc_vento.configure(text_color=texto_cor)
    label_desc_tempo.configure(text_color=texto_cor)



  
    
    #dicionario
'''def atualizar_interface(clima):
    label_cidade.configure(text=f"{clima['cidade']} - {clima['pais']} / {clima['continente']}")
    label_data.configure(text=clima['data_hora'])

    hora_atual = int(clima['data_hora'].split("|")[1].split(":")[0])
    if 6 <= hora_atual < 18:
        imagem = image_sol
        frame_inferior.configure(fg_color="lightblue")
    else:
        imagem = image_lua
        frame_inferior.configure(fg_color="darkblue")

    label_imagem = ctk.CTkLabel(frame_inferior, text='', image=imagem, fg_color="transparent")
    label_imagem.place(x=200, y=25)
'''

app.mainloop()
