#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MuAwa
#
# Created:     19/11/2021
# Copyright:   (c) MuAwa 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Emprestimo = float(input("Qual o valor do emprestimo ? "))
Salario =  float(input("Qual o valor do salario ? "))
Parcelas = float(input("Qual a quantidade de parcelas ? "))

EmprestimoParcelas = Emprestimo/ Parcelas;

SalarioPorcento = 0.3*Salario / 0.1 ;

if SalarioPorcento > EmprestimoParcelas:
    print("Valor da parcela maior que 30% do salario")
else :
    print("Emprestimo aprovado")
