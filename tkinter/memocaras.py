# coding: utf-8

"""
Aplicativo para ajudar a memorizar o nome das pessoas em um curso.
"""

from Tkinter import Tk, Canvas, PhotoImage, Frame, Label
from Tkinter import HIDDEN, NORMAL, EW, W, NW
from ttk import Button

from random import choice

pessoas = [
    ('Daniel', [38, 183, 103, 251]),
    ('Pedro', [113, 181, 169, 248]),
    ('Leo Bragatti', [201, 172, 255, 237]),
    ('Flavio', [299, 171, 353, 239]),
    ('Hugo', [439, 194, 502, 275]),
    ('Tauan', [530, 15, 590, 86]),
    ('Luis', [482, 27, 538, 99]),
    ('Roger', [427, 39, 483, 114]),
    ('Rodrigo', [382, 24, 437, 97]),
    ('Danilo', [318, 28, 365, 92]),
    ('Anderson', [290, 40, 335, 104]),
    # ('Luciano', [216, 36, 269, 98]),
    ('Leo Fontolan', [127, 49, 180, 112]),
]


class MemoCaras(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.grid(column=0, row=0)
        self.canvas = Canvas(self, width=604, height=480)
        self.canvas.grid(column=0, row=0, columnspan=2)
        self.bt_prox = Button(self, text='Próximo', command=self.proximo)
        self.bt_prox.grid(column=0, row=1, sticky=W)
        self.nome = Label(self, text='(passe aqui para ver o nome)')
        self.nome.bind('<Enter>', self.mostra_nome)
        self.nome.bind('<Leave>', self.esconde_nome)
        self.nome.grid(column=1, row=1, sticky=EW)
        nome_arq_foto = 'turma1-640x480.gif'
        self.foto = PhotoImage(file=nome_arq_foto)
        self.canvas.create_image(0, 0, image=self.foto, anchor=NW)
        self.caras = {}
        for nome, bbox in pessoas:
            marca = self.canvas.create_oval(*bbox, outline='green', width=5,
                                    state=HIDDEN)
            self.caras[nome] = marca
        self.cara_ativa = None

    def proximo(self):
        if self.cara_ativa is not None:
            marca = self.caras[self.cara_ativa]
            self.canvas.itemconfigure(marca, state=HIDDEN)
        recente = self.cara_ativa
        while True:
            self.cara_ativa = choice(self.caras.keys())
            if recente != self.cara_ativa:
                break
        marca = self.caras[self.cara_ativa]
        self.canvas.itemconfigure(marca, state=NORMAL)

    def mostra_nome(self, evento):
        self.texto_nome = self.nome['text']
        self.nome['text'] = self.cara_ativa

    def esconde_nome(self, evento):
        self.nome['text'] = self.texto_nome



root = Tk()
MemoCaras(root)
root.mainloop()
