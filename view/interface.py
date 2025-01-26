import datetime
import customtkinter as ctk
from view.utils.helpers import carregar_imagem, traduzir_texto
from model.service.weather_service import obter_informacoes_climaticas
import os

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Sistema de Clima')
app.geometry('400x300')

campo_local = ctk.CTkEntry(app, placeholder_text="Digite uma cidade", width=200, height=30, font=("Arial", 13))
campo_local.grid(row=1, column=0, columnspan=1, pady=5, padx=5)

        
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
button_search.grid(row=1, column=1, pady=5, padx=25)

#Caminho para as imagens

caminho_imagem_dia_chuvoso = os.path.join(os.path.dirname(__file__), 'images/dia_chuvoso.png')
image_dia_chuvoso = carregar_imagem(caminho_imagem_dia_chuvoso)

caminho_imagem_dia_ensolarado = os.path.join(os.path.dirname(__file__), 'images/dia_ensolarado.png')
image_dia_ensolarado = carregar_imagem(caminho_imagem_dia_ensolarado)

caminho_imagem_dia_nublado = os.path.join(os.path.dirname(__file__), 'images/dia_nublado.png')
image_dia_nublado = carregar_imagem(caminho_imagem_dia_nublado)

caminho_imagem_nascer_sol = os.path.join(os.path.dirname(__file__), 'images/nascer_sol.png')
image_nascer_sol = carregar_imagem(caminho_imagem_nascer_sol)

caminho_imagem_por_sol = os.path.join(os.path.dirname(__file__), 'images/por_sol.png')
image_por_sol = carregar_imagem(caminho_imagem_por_sol)

caminho_imagem_neve = os.path.join(os.path.dirname(__file__), 'images/neve.png')
image_neve = carregar_imagem(caminho_imagem_neve)

caminho_imagem_noite_chuvosa = os.path.join(os.path.dirname(__file__), 'images/noite_chuvosa.png')
image_noite_chuvosa = carregar_imagem(caminho_imagem_noite_chuvosa)

caminho_imagem_noite_nublada = os.path.join(os.path.dirname(__file__), 'images/noite_nublada.png')
image_noite_nublada = carregar_imagem(caminho_imagem_noite_nublada)

caminho_imagem_noite_luar = os.path.join(os.path.dirname(__file__), 'images/noite_luar.png')
image_noite_luar = carregar_imagem(caminho_imagem_noite_luar)

caminho_imagem_noite_nevoa = os.path.join(os.path.dirname(__file__), 'images/nevoeiro_noite.png')
image_noite_nevoa = carregar_imagem(caminho_imagem_noite_nevoa)

caminho_imagem_dia_nevoa = os.path.join(os.path.dirname(__file__), 'images/nevoeiro_dia.png')
image_dia_nevoa = carregar_imagem(caminho_imagem_dia_nevoa)

frame_inferior = ctk.CTkFrame(app, fg_color=None)
frame_inferior.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0,10))
app.grid_rowconfigure(3, weight=1)  # Configurar linha para expandir
app.grid_columnconfigure(0, weight=1)  # Configurar coluna para expandir

#labels

label_cidade = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 18), pady=20)
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
label_desc_tempo.grid(row=7, column=1,  padx=0, pady=0, sticky="nsew")

def atualizar_interface(clima):
    # Traduzindo os dados climáticos para português
    cidade_traduzida = traduzir_texto(clima.city).upper()
    pais_traduzido = traduzir_texto(clima.country)
    continente_traduzido = traduzir_texto(clima.continent)
    
    label_cidade.configure(text=f'{cidade_traduzida} - {pais_traduzido} / {continente_traduzido}')
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
    descricao_tempo = clima.description.lower()
    
    
    # Determinar a imagem com base no clima e na hora do dia
    if 6 <= hora_atual < 18:
        if 'chuva' in descricao_tempo:
            imagem = image_dia_chuvoso
        elif 'nublado' or 'trovoada' in descricao_tempo:
            imagem = image_dia_nublado
        elif 'neve' in descricao_tempo:
            imagem = image_neve
        elif 'névoa' in descricao_tempo:
            imagem = image_dia_nevoa
        elif 'céu limpo' in descricao_tempo:
            imagem = image_dia_ensolarado
        elif hora_atual < 8:
            imagem = image_nascer_sol
        elif hora_atual > 17:
            imagem = image_por_sol
        else:
            imagem = image_dia_ensolarado
        frame_inferior.configure(fg_color="lightblue")
        texto_cor = "black"
    else:
        if 'chuva' in descricao_tempo:
            imagem = image_noite_chuvosa
        elif 'nublado' or 'trovoada' in descricao_tempo:
            imagem = image_noite_nublada
        elif 'névoa' in descricao_tempo:
            imagem = image_dia_nevoa
        elif 'céu limpo' in descricao_tempo:
            imagem = image_noite_luar
        else:
            imagem = image_noite_luar
        frame_inferior.configure(fg_color="darkblue")
        texto_cor = "white"

    # Exibir a imagem correta
    if imagem is not None:
        label_imagem = ctk.CTkLabel(frame_inferior, text='', image=imagem, fg_color="transparent")
        label_imagem.place(x=190, y=65)
        
    else:
        print("Erro: Imagem não carregada corretamente.")

    
    
    
    ''' # Baseado no horário, escolhemos a imagem (dia ou noite)
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
    '''
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
