# -*- coding:utf-8 -*-

import arrr
from pyscript import document

#Cálculo em Viga bi-apoiada
print("Cálculo em Viga bi-apoiada nas extremidades")

L=input("Comprimento da viga [m]: ")
L=eval(L.replace(",","."))

F=input("Força aplicada em [N]: ")
F=eval(F.replace(",","."))

xF=input("Local de aplicação da força [m]: ")
xF=eval(xF.replace(",","."))


#Somatória das força verticais, para cima como positivo
#Ra+Rb-F=0
#Rb=F-Ra
#Ra=F-Rb

#Momento (Ma) a respeito do ponto A em x=0, sentido horário como positivo
#F*xF-Rb*L=0
Rb=F*xF/L
Ra=F-Rb

#Momentos iguais a zero
Ma=F*xF-Rb*L
Mb=Ra*L-F*(L-xF)

Mmax=max(Ra*xF, Rb*(L-xF))  #Momento máximo

fs=input("Fator de Segurança: ")
fs=eval(fs.replace(",","."))
T=input("Tensão Máxima de Escoamento [MPa]: ")
T=eval(T.replace(",","."))
Tadm=T/fs #Tensão Admissível

W=(Mmax/(Tadm*10**6))*10**9

#Mostrar os resultados
print("As forças de Reações são: Ra=","%.2f" % Ra, "N e Rb=%.2f" % Rb, "N")
#print("Os Momentos são: Ma=%.2f" % Ma, "N.m Mb=%.2f" % Mb, "N.m")
print("Momento máximo =%.3e" % Mmax, "N.m")
print("O módulo de resistência requerido Wreq=,","%.3e" % W, "mm^3")