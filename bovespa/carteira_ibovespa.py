# coding: utf-8

"""Este script obtém uma relação de ações que formam o índice Bovespa.

Este é um sub-conjunto pequeno porém representativo de todos os papéis
negociados na Bovespa.

Tentei extrair os dados direto da página [1], mas eu queria as informações
de setor, porém elas não vêm junto com a página inicial, talvez sejam
baixadas por AJAX ou codificadas em imensas campos hidden como __VIEWSTATE 
e outras aberrações características de uma página feita com ferramentas
da Microsoft. No final, resolvi copiando via copy&paste mesmo a partir
do Firefox, usando a consulta "Setor de Atuação" para obter também esta
coluna, que não aparece na exibição padrão por ordem de código.

[1] http://www.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOVESPA&idioma=pt-br

"""

import codecs
import json

NOME_ARQ = 'carteira_ibovespa'

def numvirgula(s):
    if s.count(u',') not in (0, 1):
        raise ValueError('O numero pode ter somente 0 ou 1 virgula.')
    s = s.replace(u'.', u'') # retirar pontos nos milhares
    return float(s.replace(u',', u'.'))

EPSILON = 1.0e-10

def conferir(a, b, rotulo='', tolerancia=EPSILON):
    if abs(a-b) > EPSILON:
        msg = 'Erro ao conferir %s: %r != %r'
        raise ValueError(msg % (rotulo, a, b))

with codecs.open(NOME_ARQ+'.txt', encoding='utf-8') as txt:
     # remover brancos e \n do final e dividir nas tabulações
    linhas = [lin.split('\t') for lin in txt]

# linhas de inicio de setor tem 7 colunas, demais linhas tem 5 colunas
assert set(len(lin) for lin in linhas) == set([5, 7])

colunas_papel = 'codigo acao tipo qtd part'.split()
colunas_setor = ['setor'] + colunas_papel + ['part_setor']

setor = None
qtd_total = part_total = part_setor = 0
acoes = {}
setores = {}
for lin in linhas[:-1]: # nao processar linha totais
    # remover brancos em volta de cada campo
    lin = [cpo.strip() for cpo in lin]
    if len(lin) == 7: # linha que inicia grupo de setor
        if setor is not None:
            conferir(setores[setor], part_setor, 'acumulado part_setor')    
        setor = lin.pop(0)  
        setores[setor] = numvirgula(lin.pop()) # participacao do setor
        part_setor = 0
    campos = dict(zip(colunas_papel, lin))
    campos['setor'] = setor
    qtd_total += numvirgula(campos['qtd'])
    part_setor += numvirgula(campos['part'])
    part_total += numvirgula(campos['part'])
    codigo = campos.pop('codigo')
    if codigo in acoes:
        raise ValueErro('Codigo duplicado: ' + codigo) 
    acoes[codigo] = campos

print 'conferindo totais:'
print linhas[-1][-3:]
part_setores = sum(setores.values())
print qtd_total, part_total, part_setores
conferir(qtd_total, numvirgula(linhas[-1][-3]), 'qtd_total')
conferir(part_total, numvirgula(linhas[-1][-2]), 'part_total')
conferir(part_setores, numvirgula(linhas[-1][-1]), 'part_setores')

with codecs.open(NOME_ARQ+'.json','wb', encoding='utf-8') as saida_json:
    json.dump(acoes, saida_json, indent=2)
print NOME_ARQ+'.json escrito.'