import types
import inspect

import Tkinter
import ttk

widget_bases = set(inspect.getmro(Tkinter.Widget)+
                   inspect.getmro(Tkinter.Canvas)+
                   (Tkinter.Wm,))

indice = []
for nome in dir(ttk):
    obj = getattr(ttk, nome)
    try:
        mro = inspect.getmro(obj)
    except AttributeError: # not type or class
        continue
    if (ttk.Widget in mro):
        indice.append((len(mro), nome, obj.__bases__))

indice.sort()

for len_mro, nome, bases in indice:
    print format(len_mro, '2'), nome.ljust(12), ''.join(
        [(b.__module__+'.'+b.__name__).ljust(16) for b in bases])

