# Putting a gif image on a canvas with Tkinter
# tested with Python24 by  vegaseat  25jun2005

from Tkinter import Tk, Canvas, PhotoImage, Frame, NW, Label

class MarcaFoto(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.grid(column=0, row=0)
        self.canvas = Canvas(self, width=604, height=480)
        self.canvas.grid(column=0, row=0, columnspan=2)
        self.coords = Label(self)
        self.coords.grid(column=0, row=1)
        nome_arq_foto = 'turma1-640x480.gif'
        self.foto = PhotoImage(file=nome_arq_foto)
        self.canvas.create_image(0, 0, image=self.foto, anchor=NW)
        self.canvas.bind('<Motion>', self.moveu)
        self.canvas.bind('<ButtonPress>', self.marcar)
        self.marca_ativa = None
        
    def moveu(self, evento):
        if self.marca_ativa is not None:
            bbox = self.canvas.coords(self.marca_ativa)
            bbox[2:4] = [evento.x, evento.y]
            self.canvas.coords(self.marca_ativa, *bbox)
        
    def marcar(self, evento):
        if self.marca_ativa is None:
            self.marca_ativa = self.canvas.create_oval(evento.x, evento.y, evento.x, evento.y,
                outline='green', width=5)
        else:
            self.coords = self.canvas.coords(self.marca_ativa)
            self.marca_ativa = None

root = Tk()
MarcaFoto(root)
root.mainloop()
