from __future__ import print_function

import types
import inspect

try:
    import Tkinter
except ImportError:
    import tkinter as Tkinter

widget_bases = set(inspect.getmro(Tkinter.Widget)+
                   inspect.getmro(Tkinter.Canvas)+
                   (Tkinter.Wm, Tkinter.Tk))

indice = []
for nome in dir(Tkinter):
    obj = getattr(Tkinter, nome)
    try:
        mro = inspect.getmro(obj)
    except AttributeError: # not type or class
        continue
    if (obj in widget_bases
        or Tkinter.BaseWidget in mro):
        indice.append((len(mro), nome, obj.__bases__))

indice.sort()

for len_mro, nome, bases in indice:
    print(format(len_mro,'2'), nome.ljust(12), '->' if bases else '' , 
          ' '.join([b.__name__.ljust(12) for b in bases]))

