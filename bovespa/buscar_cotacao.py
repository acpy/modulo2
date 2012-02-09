# coding: utf-8

"""Extrair todos os pares atributo-valor de um xml

    >>> xml = '''<PAPEIS><PAPEL DESCRICAO="EMBRAER ON NM" 
    ...          CODIGO="#EMBR3" IBOVESPA="S" DELAY="15"
    ...          DATA="03/02/2012" HORA="19:29:38" OSCILACAO="1" 
    ...          VALOR_ULTIMO="12,07" QUANT_NEG="4088" MERCADO="Vista"/>
    ...          </PAPEIS>'''
    >>> resultado = extrair_atributos(xml)
    >>> for chave in sorted(resultado):
    ...     print '{0:>12} : {1}'.format(chave, resultado[chave])
          CODIGO : #EMBR3
            DATA : 03/02/2012
           DELAY : 15
       DESCRICAO : EMBRAER ON NM
            HORA : 19:29:38
        IBOVESPA : S
         MERCADO : Vista
       OSCILACAO : 1
       QUANT_NEG : 4088
    VALOR_ULTIMO : 12,07
"""


import re

import urllib

URL_COTACAO = 'http://www.bmfbovespa.com.br/cotacoes2000/formCotacoesMobile.asp?codsocemi='

ER_ATRIB_VALOR = re.compile(r'(\w+)="([^"]+)"')

def extrair_atributos(xml):
    """Extrair todos os pares atributo-valor de um xml"""
    return dict(ER_ATRIB_VALOR.findall(xml))

def buscar(simbolo):
    arq = urllib.urlopen(URL_COTACAO+simbolo)
    res = arq.read()
    arq.close()
    return res

if __name__=='__main__':
    import doctest
    doctest.testmod()
