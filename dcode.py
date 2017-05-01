# coding: utf-8
# Copyright 2017 Jefferson Allan
# Importando ...
import os, sys, platform, time

# Definindo variável com o valor do sistema
sistema = platform.system()

# Função para limpar a tela
def limpa():
	if sistema == "Linux":
		os.system("clear")
	elif sistema == "Windows":
		os.system("cls")
		pass
	pass

# Função ASCII - Decimal
def decdeci(numeros):
	limpa()
	print banner
	print " [Você escolheu:]	Decodificar"
	print " [Você digitou:]	" + numeros
	separa = numeros.split()
	trata = map(int, separa)
	decimal = ''.join(chr(numero) for numero in trata)
	time.sleep(2)
	print "\n"
	print " [R::Decimal]		" + decimal
	pass

# Função ASCII - Octal
def decoct(numeros):
	limpa()
	print banner
	print " [Você escolheu:]	Decodificar"
	print " [Você digitou:]	" + numeros
	separa = numeros.split()
	toString = [str(l) for l in separa]
	toInt = [int(n,8) for n in toString]
	octal = ''.join(chr(num) for num in toInt)
	time.sleep(2)
	print "\n"
	print " [R::Octal]		" + octal
	pass

limpa()
banner = '''  
  _____                     _ _  __ _           
 |  __ \                   | (_)/ _(_)          
 | |  | | ___  ___ ___   __| |_| |_ _  ___ __ _ 
 | |  | |/ _ \/ __/ _ \ / _` | |  _| |/ __/ _` |
 | |__| |  __/ (_| (_) | (_| | | | | | (_| (_| |
 |_____/ \___|\___\___/ \__,_|_|_| |_|\___\__,_|

                                                '''
opc = '''
 [1] = [Decodifica] 	Octal ➜ ASCII
 [2] = [Decodifica] 	Decimal ➜ ASCII
 [3] = [Decodifica] 	Hexadecimal ➜ ASCII (Implementar)
 '''

# Banner & Opções
print banner
print opc

# Variaveis
escolha = input(" [?]: ")

# Escolhas
if escolha == 1:
	numeros = raw_input(" [Decodifica]: ")
	decoct(numeros)
	pass
elif escolha == 2:
	numeros = raw_input(" [Decodifica]: ")
	decdeci(numeros)
	pass

# Em construção ..