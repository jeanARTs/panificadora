import os

#### MENU ####
#Imprime na tela o menu
print("1 - Nova Venda")
print("2 - Gerar Relatório")
print("3 - Sobre")
print("4 - Sair")

while(True): #loop infinito
#Pegar a Opção do Usuário
opcao = input("Digite a opção desejada: ")

#Verificar qual opção o usuário escolheu
if (opcao == "1"): #se
  os.system('clear')#Limpa a tela 
  print("Nova Venda")
  sal_qt = input("Digite a quantidade de Pães de Sal: ")
  leite_qt = input("Digite a quantidade de Pães de Leite: ")
  milho_qt = input("Digite a quantidade de Pães de Milho: ")
  total = sal_qt + leite_qt + milho_qt
  print("Total de pães: %.0f deu R$ %.2f" % (total, total*0.25))

  input("\n\nPressione  ENTER para continuar: ")
  os.system('clear')
elif (opcao == "2"): #senao se
  print("Relatório")
elif (opcao == "3"):
  print("sobre")
elif (opcao == "4"):
  print("Sair")
  break #interrompe a executação do laço
else:
  print("Opção inválida, porfavor tente novamente")

print ("programa finalizado!")

