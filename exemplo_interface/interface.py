# importando a biblioteca
import tkinter as tk 

def mostar_nome():
    nome = entrada_nome.get()
    resultado.config(
    text=f"Olá, {nome}"
    )

#criar a janela principal 
janela = tk.Tk()

#Definir o titulo exibido na barra superior
janela.title("Minha primeira janela")

#definir o tamanho da janela
janela.geometry("800x500")

#Mudar a cor de fundo
janela.config()

#Criar um texto dentro dentro da janela
titulo = tk.Label(
    janela,
    text="Sistema de Locação de Veiculos",
    font=("Arial",18)
)
tk.Label(
    janela,
    text="Digite seu nome: ",
    bg="Yellow",
    font=("Arial",18, "bold"), background="black", fg="white"

).pack(pady=10)

def mensagem():
    print("Botão Clicado!!!")

#Adicionando um botão
botao = tk.Button(
    janela,
    text="Clique aqui",
    command=mensagem
)


#Campo de entrada
entrada_nome = tk.Entry(
    janela,
    width=40
)
entrada_nome.pack()

tk.Button(
    janela,
    text="Confirmar",
    command=mostar_nome,
    bg="red"
).pack(pady=15)

resultado = tk.Label(
    janela,
    text=""
)
resultado.pack()

#Exibe o compenente na janela
titulo.pack(pady=30)
botao.pack(pady=20)


#Mantem a janela a aberta
janela.mainloop()