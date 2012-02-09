# coding: utf-8

"""Extrair todos os pares atributo-valor de um xml simples: duas formas
   de fazer.

    >>> res_re = extrair_re(xml)
    >>> res_etree = extrair_etree(xml)
    >>> res_re == res_etree
    True

"""

xml = '''<PAPEIS><PAPEL DESCRICAO="EMBRAER ON NM" 
         CODIGO="#EMBR3" IBOVESPA="S" DELAY="15"
         DATA="03/02/2012" HORA="19:29:38" OSCILACAO="1" 
         VALOR_ULTIMO="12,07" QUANT_NEG="4088" MERCADO="Vista"/>
         </PAPEIS>'''

import re

ER_ATRIB_VALOR = re.compile(r'(\w+)="([^"]+)"')

def extrair_re(xml):
    """Extrair todos os pares atributo-valor de um xml"""
    res = ER_ATRIB_VALOR.findall(xml)
    return dict(res)

from xml.etree.ElementTree import XML

def extrair_etree(xml):
    """Extrair todos os pares atributo-valor de um xml"""
    papel = XML(xml).find('PAPEL')
    return papel.attrib.copy()
    

if __name__=='__main__':
    import doctest
    doctest.testmod()
