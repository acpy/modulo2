import types
import inspect

import Tkinter

widget_bases = set(inspect.getmro(Tkinter.Widget)+
                   inspect.getmro(Tkinter.Canvas)+
                   (Tkinter.Wm,))

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
    print len_mro, nome.ljust(12), ''.join(
        [b.__name__.ljust(12) for b in bases])

