#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MuAwa
#
# Created:     30/11/2021
# Copyright:   (c) MuAwa 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Arquivo = float(input("Qual o tamanho do arquivo em MB ? "))
Velocidade =  float(input("Qual a velocidade de donwload em Mbps ? "))
TotalSegundos = Arquivo/(Velocidade/8);
TotalMin = TotalSegundos/60;

print("O tempo de download sera ",TotalMin);
