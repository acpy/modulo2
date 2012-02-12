# coding: utf-8

from Tkinter import Tk, Canvas, PhotoImage, Frame, NW
from ttk import Button

posicoes = [
    [38, 183, 103, 251],
    [113, 181, 169, 248],
    [201, 172, 255, 237],
    [299, 171, 353, 239],
    [439, 194, 502, 275],
    [530, 15, 590, 86],
    [482, 27, 538, 99],
    [427, 39, 483, 114],
    [382, 24, 437, 97],
    [318, 28, 365, 92],
    [290, 40, 335, 104],
    [216, 36, 269, 98],
    [127, 49, 180, 112],
]


class MarcaFoto(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.grid(column=0, row=0)
        self.canvas = Canvas(self, width=604, height=480)
        self.canvas.grid(column=0, row=0, columnspan=2)
        self.bt_prox = Button(self, text='Próximo', command=self.proximo)
        self.bt_prox.grid(column=0, row=1)
        nome_arq_foto = 'turma1-640x480.gif'
        self.foto = PhotoImage(file=nome_arq_foto)
        self.canvas.create_image(0, 0, image=self.foto, anchor=NW)
        self.marca_ativa = None
        
    def proximo(self):
        if self.marca_ativa is None:
            self.marca_ativa = 0
        else:
            self.marca_ativa += 1
        if self.marca_ativa == len(posicoes):
            self.marca_ativa = 0
        self.canvas.create_oval(*posicoes[self.marca_ativa],
            outline='green', width=5)    
        

root = Tk()
MarcaFoto(root)
root.mainloop()
