from tkinter import *
from time import time
from random import choice

# Declação de variáveis globais
texto_alvo = ''
texto_digitado = ''
tempo_inicial = 0
tempo_final = 0
duracao_do_teste = 0

def calcular_velocidade(quantidade_de_palavras):
    global duracao_do_teste

    tempo_em_minutos = duracao_do_teste / 60
    velocidade = (quantidade_de_palavras / tempo_em_minutos)
    return velocidade

def escolher_texto():
    global texto_alvo

    # Abre o arquivo e armazena uma lista com todas as palavras dele
    database = open('database.txt', 'r', encoding='utf-8')
    palavras_do_database = (database.read()).split()
    palavras_escolhidas = []

    for i in range(25):
        # Escolhe uma palavra do database e adiciona na lista de palavras escolhidas, repete 25 vezes
        palavras_escolhidas.append(choice(palavras_do_database))
    
    # Junta as palavras escolhidas separadas por espaço
    texto_alvo = ' '.join(palavras_escolhidas)

    label_texto_alvo.config(text=texto_alvo)

def calcular_precisao(quantidade_de_palavras):
    global texto_digitado, texto_alvo
    erros = 0

    for palavra in (texto_digitado).split():
        if not palavra in texto_alvo.split():
            erros += 1
    
    precisao = (1.0 - (erros / quantidade_de_palavras)) * 100.0
    return precisao

def inicio_do_teste():
    global tempo_inicial, texto_alvo

    # Marca o tempo inicial
    tempo_inicial = time()

    resultado.config(text='')

def final_do_teste():
    global tempo_inical, tempo_final, duracao_do_teste, texto_digitado

    # Calcula a duração do teste
    tempo_final = time()
    duracao_do_teste = tempo_final - tempo_inicial

    # Coleta o texto digitado
    texto_digitado = campo_de_digitacao.get(1.0, END)

    # Calcula a velocidade
    quantidade_de_palavras = len(texto_digitado.split())
    velocidade = calcular_velocidade(quantidade_de_palavras)

    # Calcula a precisão
    precisao = calcular_precisao(quantidade_de_palavras)

    # Exibe na tela o resultado
    resultado.config(text=f'''Duração do teste: {duracao_do_teste:.2f} segundos
Tamanho do teste: {quantidade_de_palavras} palavras
Velocidade: {velocidade:.2f} WPM (words/minute)
Acurácia (precisão): {precisao:.2f}%''')

# Cria a janela inicial
janela = Tk()
janela.title('Velocidade de digitação')
janela.geometry('600x500')
janela.resizable(False, False)

# Iguala os pesos das colunas do grid para manter a interface simétrica e permitir centralizar elementos perfeitamente
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.columnconfigure(2, weight=1)

# Titulo do programa
titulo = Label(janela, text='Teste de digitação', font=('Jetbrains Mono', 18))
titulo.grid(column=0, row=0, columnspan=3, sticky=EW, padx=10, pady=10)

# Label com o texto-alvo a ser digitado
label_texto_alvo = Label(janela, text='Digite as palavras que aparecerão aqui, clique em "Novo teste" e em seguida em "Iniciar teste", após finalizar, clique em "Finalizar teste"', font=('Arial', 12), wraplength=500)
label_texto_alvo.grid(column=0, row=1, columnspan=3, sticky=EW, padx=10, pady=10)

# Campo onde o usuário vai digitar
campo_de_digitacao = Text(janela, width=70, height=5, wrap=WORD)
campo_de_digitacao.grid(column=0, row=2, columnspan=3, sticky=EW, padx=10, pady=10)

novo_teste = Button(janela, text='Novo teste', command=escolher_texto)
novo_teste.grid(column=0, row=3, sticky=N, padx=10, pady=10)

iniciar_teste = Button(janela, text='Iniciar teste', command=inicio_do_teste)
iniciar_teste.grid(column=1, row=3, sticky=N, padx=10, pady=10)

iniciar_teste = Button(janela, text='Finalizar teste', command=final_do_teste)
iniciar_teste.grid(column=2, row=3, sticky=N, padx=10, pady=10)

resultado = Label(janela, text='', font=('Jetbrains Mono', 12), justify=LEFT)
resultado.grid(column=0, row=4, columnspan=3, sticky=W, padx=10, pady=10)

janela.mainloop()