while True:

  print("|---------- CRUD ----------|")
  print("|   1- Adicionar Usuário   |")
  print("|   2- Listar Usuários     |")
  print("|   3- Editar Usuário      |")
  print("|   4- Deletar Usuário     |")
  print("|   5- Sair                |")
  print("|--------------------------|")

  while True:
        try:
          opcao = int(input("O que deseja fazer? "))
          if (opcao >= 1 and opcao <=5):
              break
          else:
              print("Digite uma opção válida, por favor. ")
        except ValueError:
            print("Letras não são aceitas, por favor insira números, de 1 a 5.")

  # Inicio das opções
  match opcao:
    case 1:
      # validação de entrada
      while True:
        try:
          qtdUsuario = int(input("Quantos usuários quer cadastrar? "))
          if qtdUsuario > 0:
              break
          else:
              print("Digite um número positivo, por favor. ")
        except ValueError:
            print("Letras não são aceitas, por favor insira números. ")

      #definição do tamanho do vetor
      nomeUsuario = [None] * qtdUsuario

      #cadastros e contador de lista
      for i in range(qtdUsuario):
        nomeUsuario[i] = input("Nome: ")

    case 2:
      #listagem de cadastros
      for i in range(len(nomeUsuario)) :
        print(f'{i+1} - {nomeUsuario[i]}')


    case 3:
      #editar usuario
      for i in range(len(nomeUsuario)) :
        print(f'{i+1} - {nomeUsuario[i]}')
      
      #validação de escolha do indice
      while True:
        try:
          numEdit = int(input('Qual deseja editar?'))
          if (numEdit >= 1 and numEdit <= len(nomeUsuario)):
              break
          else:
              print("Digite uma opção válida, por favor. ")
        except ValueError:
            print("Letras não são aceitas, por favor insira números, de 1 a 5.")

      respostaEditar = input(f"Tem certeza que deseja editar o cadastro: '{nomeUsuario[numEdit - 1]}'? [s/n] ")

      #validação de resposta
      while ((respostaEditar != "s" and respostaEditar != "n")):
        respostaEditar = input(f"Resposta inválida, digite 's' para sim ou 'n' para não ")

      #edição
      if (respostaEditar == "s"):
        nomeUsuario[numEdit - 1] = (input('Insira o nome correto: '))

    case 4:
      #deletar usuario
      for i in range(len(nomeUsuario)) :
        print(f'{i+1} - {nomeUsuario[i]}')

      while True:
        try:
          numDelete = int(input('Qual deseja deletar?'))
          if (numDelete >= 1 and numDelete <= len(nomeUsuario)):
              break
          else:
              print("Digite uma opção válida, por favor. ")
        except ValueError:
            print("Letras não são aceitas, por favor insira números, de 1 a 5.")
            
      respostaDeletar = input(f"Tem certeza que deseja deletar o cadastro: '{nomeUsuario[numDelete - 1]}'? [s/n] ")

      #validação de resposta
      while ((respostaDeletar != "s" and respostaDeletar != "n")):
        respostaDeletar = input(f"Resposta inválida, digite 's' para sim ou 'n' para não ")

      #exclusão do cadastro
      if (respostaDeletar == "s"):
          del nomeUsuario[numDelete - 1]
          print("Usuário deletado com sucesso!")

    case 5:
      #terminar o programa
      break