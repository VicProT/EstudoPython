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


Area = float(input("Qual o tamanho da area a ser pintada em metros quadrados "))

LitrosTinta = Area/6;

Lata = LitrosTinta/18;
Galao = LitrosTinta/3.6;

ValorLata = Lata * 80+(Lata*80/0.01);
ValorGalao = Galao * 25+(Galao*25/0.01);


print("O valor sera %f para %f Latas em %f metros quadrados"(ValorLata,Lata,Area))
