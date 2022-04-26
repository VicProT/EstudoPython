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


KWH = float(input("Qual a quantidade de KWh consumidas"));
TipoInstalacao = input("Qual o tipo de instalaçao (R - I- C )");


if TipoInstalacao == "R":
    if KWH>500:
        print("Preço " ,KWH*0.4);
    if KWH<=500:
        print("Preço " ,KWH*0.65);

elif TipoInstalacao == "I":
    if KWH>1000:
            print("Preço " ,KWH*0.55);
    if KWH<=1000:
            print("Preço " ,KWH*0.60);


elif TipoInstalacao == "C":
     if KWH>5000:
          print("Preço " ,KWH*0.55);
     if KWH<=5000:
          print("Preço " ,KWH*0.60);
