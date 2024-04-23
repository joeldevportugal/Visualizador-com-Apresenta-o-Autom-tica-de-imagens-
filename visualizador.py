# Importar as Bibliotecas a Usar -----------------------------------------------------------
from tkinter import Label, Listbox, Menu, Scrollbar, filedialog, Tk, BooleanVar, messagebox
import customtkinter
from PIL import Image, ImageTk
import os
#------------------------------------------------------------------------------------------
# Função para abrir pasta e carregar arquivos de imagem -----------------------------------
def abrir_pasta():
    pasta = filedialog.askdirectory()  # Abrir diálogo para escolher a pasta
    if pasta:
        # Limpar o Listbox antes de adicionar novos itens
        LFicheiros.delete(0, 'end')
        
        # Listar arquivos na pasta e adicionar ao Listbox
        for arquivo in os.listdir(pasta):
            if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                LFicheiros.insert('end', arquivo)
        
        # Definir a pasta atual como variável global para uso futuro
        global pasta_atual
        pasta_atual = pasta
#-------------------------------------------------------------------------------------------
# Função para exibir a imagem selecionada --------------------------------------------------
def mostrar_imagem(event):
    arquivo = LFicheiros.get(LFicheiros.curselection()[0])
    caminho = os.path.join(pasta_atual, arquivo)
    imagem = Image.open(caminho)
    imagem = imagem.resize((430, 530), Image.Resampling.LANCZOS)  # Redimensionar se necessário
    imagem_tk = ImageTk.PhotoImage(imagem)
    LImagen.config(image=imagem_tk)
    LImagen.image = imagem_tk  # Manter referência
#-------------------------------------------------------------------------------------------    
# Função para exibir a imagem anterior -----------------------------------------------------
def mostrar_anterior():
    index = LFicheiros.curselection()[0] if LFicheiros.curselection() else 0
    if index > 0:
        LFicheiros.select_clear(index)
        LFicheiros.select_set(index - 1)
        LFicheiros.event_generate('<<ListboxSelect>>')
        LFicheiros.see(index - 1)
    else:
        messagebox.showinfo("Início da Apresentação", "A sua apresentação está no início.")
#--------------------------------------------------------------------------------------------
# Função para exibir a próxima imagem -------------------------------------------------------
def mostrar_proximo():
    index = LFicheiros.curselection()[0] if LFicheiros.curselection() else -1
    if index < len(LFicheiros.get(0, 'end')) - 1:
        LFicheiros.select_clear(index)
        LFicheiros.select_set(index + 1)
        LFicheiros.event_generate('<<ListboxSelect>>')
        LFicheiros.see(index + 1)
    else:
        messagebox.showinfo("Fim da Apresentação", "A apresentação chegou ao fim.")
#--------------------------------------------------------------------------------------------
# Função para exibir a próxima imagem automaticamente ---------------------------------------
def exibir_proxima_auto():
    if len(LFicheiros.get(0, 'end')) == 0:
        return
    if not exibindo_auto.get():
        return
    index = LFicheiros.curselection()[0] if LFicheiros.curselection() else -1
    if index < len(LFicheiros.get(0, 'end')) - 1:
        LFicheiros.select_clear(index)
        LFicheiros.select_set(index + 1)
        LFicheiros.event_generate('<<ListboxSelect>>')
        Janela.after(1000, exibir_proxima_auto)  # Agendando a próxima exibição após 1 segundo
        # Rolando o Scrollbar para baixo
        scrollbar.set(index / len(LFicheiros.get(0, 'end')), (index + 1) / len(LFicheiros.get(0, 'end')))
    else:
        messagebox.showinfo("Fim da Apresentação", "A apresentação chegou ao fim.")
#---------------------------------------------------------------------------------------------
# Função para iniciar a exibição automática --------------------------------------------------
def iniciar_auto():
    global exibindo_auto
    exibindo_auto = BooleanVar(value=True)
    exibir_proxima_auto()  # Iniciando a exibição automática
#----------------------------------------------------------------------------------------------
# Função para parar a exibição automática -----------------------------------------------------
def parar_auto():
    global exibindo_auto
    exibindo_auto = BooleanVar(value=False)
    messagebox.showinfo("Apresentação", "A  Sua apresentação Esta Parada!.....")
#-----------------------------------------------------------------------------------------------
# Cria a Função Sobre --------------------------------------------------------------------------
def Sobre ():
    messagebox.showinfo("Sobre", "Autor Joel Antonio"+
                        "Pais : Portugal\n"+
                        "Idade : 32 Anos\n"
                        +" By Dev Joel 2024\n"
                        +"Agradeçimento : Joao Ribeiro Sys4soft de  Oliveira do Hospital - Viseu Portugal\n"
                        +"Faço Minhas Estas Palavras\n"+"A mente que se abre a uma nova ideia, jamais Voltará ao seu tamanho original\n"+
                        "Autor:Albert Einstein ")

#-----------------------------------------------------------------------------------------------
# criar a Função sair --------------------------------------------------------------------------
def fechar_aplicacao():
    resposta = messagebox.askyesno("Fechar Aplicação", "Deseja fechar a aplicação?")
    if resposta:
        Janela.destroy()
#----------------------------------------------------------------------------------------------
# defenir cores a Usar ------------------------------------------------------------------------
co0= '#ffffff' # cor Branca
co1= '#f2f6f5' # verde Claro
co2= '#000000' # preto 
#----------------------------------------------------------------------------------------------
# configurar a Nossa Janela --------------------------------------------------------------------
Janela = customtkinter.CTk()
Janela.geometry('560x480+100+100')
Janela.resizable(0,0)
Janela.title('Visualizador Imagem Automatica mais Manual Dev Joel 2024 PT © ')
Janela.config(bg=co0)
#-----------------------------------------------------------------------------------------------
# Criar a barra de menu ------------------------------------------------------------------------
menu_bar = Menu(Janela)

# Criar o menu "Arquivo"
menu_arquivo = Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Abrir", font=('arial 13 bold'), command=abrir_pasta)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", font=('arial 13 bold'), command=fechar_aplicacao)
menu_bar.add_cascade(label="Menu", menu=menu_arquivo)

# Criar o menu "Ajuda"
menu_ajuda = Menu(menu_bar, tearoff=0)
menu_ajuda.add_command(label="Sobre", font=('arial 13 bold'), command=Sobre)
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

# Configurar a barra de menu na janela
Janela.config(menu=menu_bar)
#--------------------------------------------------------------------------------------------------
# Criar O label Imagem ----------------------------------------------------------------------------
LImagen = Label(Janela, bg='white')
LImagen.place(x=10, y=10)
#--------------------------------------------------------------------------------------------------
# Criar Listbox com Scrollbar ---------------------------------------------------------------------
LFicheiros = Listbox(Janela, width=40, height=33)
scrollbar = Scrollbar(Janela, orient='vertical', command=LFicheiros.yview, bg=co0)
LFicheiros.configure(yscrollcommand=scrollbar.set)
LFicheiros.place(x=450, y=10)
scrollbar.place(x=675, y=10, height=535)  # Ajuste conforme necessário para alinhamento
LFicheiros.bind('<<ListboxSelect>>', mostrar_imagem)
#---------------------------------------------------------------------------------------------------
# Criar Botões -------------------------------------------------------------------------------------
Banterior = customtkinter.CTkButton(Janela, text='anterior', width=50, command=mostrar_anterior, bg_color=co0, fg_color=co1, text_color=co2)
Banterior.place(x=10, y=440)
BProximo = customtkinter.CTkButton(Janela, text='Proximo', width=50, command=mostrar_proximo, bg_color=co0, fg_color=co1, text_color=co2)
BProximo.place(x=70, y=440)
BIniciar = customtkinter.CTkButton(Janela, text='iniciar Auto', width=50, command=iniciar_auto, bg_color=co0, fg_color=co1, text_color=co2)
BIniciar.place(x=135, y=440)
BParar = customtkinter.CTkButton(Janela, text='Parar Auto', width=50, command=parar_auto, bg_color=co0, fg_color=co1, text_color=co2)
BParar.place(x=219, y=440)
#---------------------------------------------------------------------------------------------------
# iniciar a Nossa Janela ---------------------------------------------------------------------------
Janela.mainloop()
#---------------------------------------------------------------------------------------------------