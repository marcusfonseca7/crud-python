from IPython.display import clear_output

def enter():
  input("Pressione ENTER para continuar.")

#declaração da lista
nomeUsuario = []

while True:

  clear_output()

  print("╔════════════════════════════╗")
  print("║       CRUD DE USUÁRIOS     ║")
  print("╠════════════════════════════╣")
  print("║   1- Adicionar Usuário     ║")
  print("║   2- Listar Usuários       ║")
  print("║   3- Editar Usuário        ║")
  print("║   4- Deletar Usuário       ║")
  print("║   5- Sair                  ║")
  print("╚════════════════════════════╝")
  print() # será usado no programa como "pula linha"

  while True:
        try:
          opcao = int(input("O que deseja fazer? "))
          if (opcao >= 1 and opcao <=5):
            print()
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
            print()
            break
          else:
            print("Digite um número positivo, por favor. ")
        except ValueError:
            print("Letras não são aceitas, por favor insira números. ")


      #cadastros
      for i in range(qtdUsuario):
        while True:
          nomeDigitado = (input(f"Nome da {i+1}º pessoa: "))
          if (nomeDigitado.strip() != ""):
            break
          else:
            print("Digite um nome, por favor. ")

        nomeUsuario.append(nomeDigitado.strip())
        print("Usuário Cadastrado com Sucesso!")
        print()
      enter()

    case 2:
      print()
      print("Aqui está a lista de Usuários:")

      #listagem de cadastros
      if (len(nomeUsuario) > 0):
        for i in range(len(nomeUsuario)) :
          print(f'{i+1} - {nomeUsuario[i]}')
        print()
        enter()
      else: 
        print("Nenhum usuário cadastrado até o momento!")
        print()
        enter()

    case 3:
      #editar usuario
      if (len(nomeUsuario) > 0):
        for i in range(len(nomeUsuario)) :
          print(f'{i+1} - {nomeUsuario[i]}')
        
        #validação de escolha do indice
        while True:
          try:
            numEdit = int(input('Qual deseja editar? '))
            if (numEdit >= 1 and numEdit <= len(nomeUsuario)):
                break
            else:
                print("Digite uma opção válida, por favor. ")
          except ValueError:
              print(f"Letras não são aceitas, por favor insira números, de 1 a {len(nomeUsuario)}.")

        respostaEditar = input(f"Tem certeza que deseja editar o cadastro: '{nomeUsuario[numEdit - 1]}'? [s/n] ")

        #validação de resposta
        while ((respostaEditar != "s" and respostaEditar != "n")):
          respostaEditar = input(f"Resposta inválida, digite 's' para sim ou 'n' para não ")

        #edição
        if (respostaEditar == "s"):
          while True:
            nomeUsuario[numEdit - 1] = (input("Insira o nome correto: ").strip())
            if (nomeUsuario[numEdit - 1].strip() != ""):
              print()
              print("Usuário Editado!!")
              break
            else:
              print("Digite um nome, por favor. ")
        else:
          print("Operação Cancelada!")
        enter()

      else:
        print("Nenhum usuário cadastrado até o momento!")
        enter()


    case 4:
      
      print("Usuários Listados:")
      #deletar usuario
      if (len(nomeUsuario) > 0):
        for i in range(len(nomeUsuario)) :
          print(f'{i+1} - {nomeUsuario[i]}')

        while True:
          try:
            print()
            numDelete = int(input('Qual deseja deletar? '))
            if (numDelete >= 1 and numDelete <= len(nomeUsuario)):
                break
            else:
                print("Digite uma opção válida, por favor. ")
          except ValueError:
              print(f"Letras não são aceitas, por favor insira números, de 1 a {len(nomeUsuario)}.")
              
        respostaDeletar = input(f"Tem certeza que deseja deletar o cadastro: '{nomeUsuario[numDelete - 1]}'? [s/n] ")

        #validação de resposta
        while ((respostaDeletar != "s" and respostaDeletar != "n")):
          respostaDeletar = input(f"Resposta inválida, digite 's' para sim ou 'n' para não ")

        #exclusão do cadastro
        if (respostaDeletar == "s"):
            del nomeUsuario[numDelete - 1]
            print()
            print("Usuário deletado com sucesso!")
        else:
          print("Operação Cancelada!")
        enter()

      else: 
        print("Nenhum usuário cadastrado até o momento!")
        enter()
        
    case 5:
      #terminar o programa
      break