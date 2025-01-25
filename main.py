from datetime import datetime
import customtkinter as ctk
from PIL import Image, ImageTk
import infoApi

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Sistema de Clima')
app.geometry('350x300')

# Configurar a geometria da grade para centralizar os widgets
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=0)

# Linha divisória (Frame simulando uma linha horizontal)
linha_divisoria1 = ctk.CTkFrame(app, height=2, fg_color="gray")
linha_divisoria1.grid(row=0, column=0, columnspan=2, sticky="ew", pady=1)

# Campo de entrada
campo_local = ctk.CTkEntry(app, placeholder_text="Digite o local", width=200, height=30, font=("Arial", 13))
campo_local.grid(row=1, column=0, columnspan=1, pady=10,padx=10)




def buscar_clima():
    cidade = campo_local.get().strip()  # Obtém o nome da cidade
    if cidade:  # Verifica se a cidade foi informada
        dados_clima = infoApi.informacao(cidade)  # Chama a API e obtém os dados
        if dados_clima:  # Verifica se os dados não são None
            atualizar_interface(dados_clima)  # Passa os dados para a interface
        else:
            print("Erro ao obter os dados da cidade.")  # Erro ao obter os dados
    else:
        print("Por favor, insira o nome de uma cidade.")


# Botão de busca
button_search = ctk.CTkButton(app, text='Search', command=buscar_clima, width=100, height=30, font=("Arial", 13))
button_search.grid(row=1, column=1, columnspan=2, pady=10, padx=10)



# Linha divisória (Frame simulando uma linha horizontal)
linha_divisoria = ctk.CTkFrame(app, height=2, fg_color="gray")
linha_divisoria.grid(row=2, column=0, columnspan=2, sticky="ew", pady=1)


#passa os valores

def atualizar_interface(dados):
    label_cidade.configure(text=f'{dados["cidade"]} - {dados["pais"]} / {dados["continente"]}')
    label_data.configure(text=dados["data_hora"])
    label_humidade.configure(text=str(dados["humidade"]))
    label_pressao.configure(text=f'Pressão: {dados["pressao"]} hPa')
    label_veloc_vento.configure(text=f'Velocidade do vento: {dados["velocidade_vento"]} m/s')
    label_desc_tempo.configure(text=dados["descricao"].capitalize())
    label_hum_simb.configure(text= '%')
    label_hum_nome.configure(text='humidade')
    
    
    # Vamos assumir que dados["data_hora"] já possui a data/hora corretamente formatada
    hora_atual = dados["data_hora"]  # Exemplo: "23/01/2025 | 17:09:50 PM"

    # Vamos extrair a hora e verificar se é AM ou PM
    hora_atual = datetime.strptime(hora_atual, "%d/%m/%Y  |  %H:%M:%S %p")
    hora_em_24h = hora_atual.strftime("%H")  # "17" para 5PM ou "08" para 8AM
    print("\nHora atual (24h):", hora_em_24h)

    # Baseado no horário, escolhemos a imagem (dia ou noite)
    if int(hora_em_24h) >= 6 and int(hora_em_24h) < 18:  # Se a hora for entre 06:00 e 18:00
        # Imagem de Sol (Dia)
        label_imagem = ctk.CTkLabel(frame_inferior, text='', image=image_sol, fg_color="transparent")
        label_imagem.place(x=200, y=25)
        frame_inferior.configure(fg_color="lightblue")
        texto_cor = "black"
    else:
        # Imagem de Lua (Noite)
        label_imagem = ctk.CTkLabel(frame_inferior, text='', image=image_lua, fg_color="transparent")
        label_imagem.place(x=200, y=25)
        frame_inferior.configure(fg_color="darkblue")
        # Ajuste a posição conforme necessário
        texto_cor = "white"

    
    

    label_cidade.configure(text_color=texto_cor)
    label_data.configure(text_color=texto_cor)
    label_humidade.configure(text_color=texto_cor)
    label_hum_simb.configure(text_color=texto_cor)
    label_hum_nome.configure(text_color=texto_cor)
    label_pressao.configure(text_color=texto_cor)
    label_veloc_vento.configure(text_color=texto_cor)
    label_desc_tempo.configure(text_color=texto_cor)




    
    
   

#corpo do projeto

# Criar um novo frame abaixo da linha divisória
frame_inferior = ctk.CTkFrame(app, fg_color=None)  # Altere a cor de fundo aqui
frame_inferior.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=0)
#frame_inferior.configure(image=image_lua_ctk)
app.grid_rowconfigure(3, weight=1)

label_cidade = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 13))
label_cidade.grid(row=3, column=0,columnspan=2, padx=10, sticky="w")

label_data = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 12))
label_data.grid(row=4, column=0, padx=10, sticky="w")

label_humidade = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 45))
label_humidade.grid(row=5, column=0,  padx=10, sticky="w")






# Carregar a imagem com a Pillow
image_sol = Image.open("projetoClima\sol.png").convert("RGBA")
  # Carregar a imagem usando Pillow
image_sol = image_sol.resize((100, 100))  # Redimensionar a imagem para o tamanho desejado


 #Carregar a imagem com a Pillow
image_lua = Image.open("projetoClima\lua.png").convert("RGBA")
  # Carregar a imagem usando Pillow
image_lua = image_lua.resize((100, 100))  # Redimensionar a imagem para o tamanho desejado


# Criar a imagem customtkinter a partir da imagem PIL
image_lua = ctk.CTkImage(light_image=image_lua, size=(100, 100))
image_sol = ctk.CTkImage(light_image=image_sol, size=(100, 100))


# Exibir a imagem em um label
'''label_imagem = ctk.CTkLabel(app, text='', image=image)
label_imagem.place(x=215, y=90)  # Ajuste a posição conforme necessário'''


label_hum_simb = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 13))
label_hum_simb.grid(row=5, column=0, padx=70, pady=0, sticky="nw" )

label_hum_nome = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 10))
label_hum_nome.grid(row=5, column=0, padx=70, pady=0,  sticky="sw")

label_pressao = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 12))
label_pressao.grid(row=6, column=0, padx=10, sticky="w")

label_veloc_vento = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 12))
label_veloc_vento.grid(row=7, column=0, padx=10, sticky="w")

label_desc_tempo = ctk.CTkLabel(frame_inferior, text='', font=("Arial", 12))
label_desc_tempo.grid(row=7, column=1, padx=0, pady=0, sticky="w")



app.mainloop()
