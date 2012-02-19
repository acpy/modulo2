# coding: utf-8

import string

# cpf.py versao 2.1 20/12/2000
# hist�ria:
# 2.1: extra�mos calcular_dc da fun��o checar_cpf
# 2.0: n�o aceita CPFs como 111.111.111-11, 222.222.222-22 etc.

def so_digitos(txt):
	#retorna a string eliminando tudo que n�o � digito
	digitos = []
	for car in txt:
		if car in string.digits: digitos.append(car)
	return ''.join(digitos)

def calcular_dc(num):
	#calcula os d�gitos de controle a partir de uma string '123456789'
	mul = 1
	res = 0
	for dig in num:
		res = res+mul*int(dig)
		mul = mul+1
	dc1 = res % 11
	if dc1 == 10:
		dc1 = 0
	mul = 1
	res = 0
	for dig in num[1:]:
		res = res+mul*int(dig)
		mul = mul+1
	res = res+(9*dc1)
	dc2 = res % 11
	if dc2 == 10:
		dc2 = 0
	return str(dc1)+str(dc2)

def checar_cpf(cpf):
	'''retorna cpf v�lido como 000.000.000-00 ou None se for inv�lido'''
	cpf = so_digitos(cpf)
	if len(cpf) != 11:
		return None
	if cpf == cpf[0]*11:
		#000.000.000-00, 111.111.111-11 etc. s�o v�lidos mas n�o aceitamos
		return None
	num = cpf[:-2]
	dc = cpf[-2:]
	if dc == calcular_dc(num):
		return '%s.%s.%s-%s' % (num[:3],num[3:6],num[6:9],dc)
	else:
		return None

