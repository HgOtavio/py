#Hugo Otávio e Ana Clarisse 
#13. Escreva um programa que solicite ao usuário que insira o nome de cinco países e suas respectivas capitais. Armazene essas informações em um dicionário e, em seguida, imprima o dicionário.




pais_capital={}
for i in range(5):
    pais=input("Digite o nome do país: ")
    capital=input("Digite o nome da capital: ")
    pais_capital[pais]=capital
print(pais_capital)