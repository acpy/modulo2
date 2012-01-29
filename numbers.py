# coding: utf-8

"""
O PEP-3141 "A Type Hierarchy for Numbers" definiu uma hierarquia de tipos
numéricos em Python, organizada a partir das seguintes classes abastratas::

     Number
      └── Complex
           └── Real
                └── Rational
                     └── Integral

A tabela a seguir mostra os resultados de ``issubclass(C, A)``, onde ``C`` é
uma das classes concretas ``complex``, ``float``, ``fraction.Fraction``,
``long`` e ``int``; e ``A`` é uma das classes abstratas acima::

            Number    Complex     Real     Rational    Integral
  complex     1          1          0          0          0
  float       1          1          1          0          0
  Fraction    1          1          1          1          0
  long        1          1          1          1          1
  int         1          1          1          1          1

As classes concretas mencionadas acima são subclasses virtuais das respectivas
classes abstratas. Isso significa que elas foram registradas como subclasses
para efeito de serem testadas com ``issubclass`` e ``isinstance``. A forma de
registrar uma subclasse virtual é::

     >>> from numbers import Real
     >>> Real.register(float)

Em outras palavras, a hierarquia incluindo as classes concretas é assim::

     Number
      └── Complex
            ├── complex
            └── Real
                ├── float
                └── Rational
                     ├── Fraction
                     └── Integral
                          ├── long
                          └── int

Curiosamente, a classe concreta ``decimal.Decimal`` não entrou na hieraquia. O
PEP-3141 diz apenas "After consultation with its authors it has been decided
that the Decimal type should not at this time be made part of the numeric
tower."

Alguns testes::

     >>> from numbers import Number, Complex, Real, Rational, Integral
     >>> tipos_num_abs = [Number, Complex, Real, Rational, Integral]
     >>> [isinstance(1, tipo) for tipo in tipos_num_abs]
     [True, True, True, True, True]
     >>> from fractions import Fraction
     >>> um_terco = Fraction('1/3')
     >>> [isinstance(um_terco, tipo) for tipo in tipos_num_abs]
     [True, True, True, True, False]
     >>> [isinstance(1.1, tipo) for tipo in tipos_num_abs]
     [True, True, True, False, False]
     >>> [isinstance(1j, tipo) for tipo in tipos_num_abs]
     [True, True, False, False, False]


"""
