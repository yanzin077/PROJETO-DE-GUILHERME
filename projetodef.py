import csv
import re

filmes = []
usuarios = []
ingressos_vendidos = []
promocoes = []

def menu_principal():
    while True:
        print("\n\033[94mMenu Principal:\033[0m")
        print("1 – Gerenciar os filmes (ADM)")
        print("2 – Comprar Ingressos (CLIENTE)")
        print("3 – Cadastrar usuário (ADM ou CLIENTE)")
        print("4 - Listar todos os filmes")
        
        opcao = input("Escolha uma opção (ou 'f' para sair): ").strip().lower()

        if opcao == 'f':
            print("\033[94mVolte Sempre!!!\033[0m")
            break
        elif opcao == '1':
            gerenciar_filmes()
        elif opcao == '2':
            comprar_ingressos()
        elif opcao == '3':
            cadastrar_usuario()
        elif opcao == '4':
            listar_filmes()
        else:
            print("\033[91mOpção inválida!!!\033[0m")

def gerenciar_filmes():
    print("\nMenu de Gerenciamento de Filmes:")
    nome_usuario = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    usuario = efetuar_login(nome_usuario, senha)
    if usuario and usuario['perfil'] == "ADM":
        while True:
            print("\nOpções de Gerenciamento de Filmes:")
            print("1 – Cadastrar filme")
            print("2 – Buscar filme")
            print("3 – Atualizar dados do filme")
            print("4 – Remover filme")
            print("5 – Listar todos os ingressos vendidos por filme")
            print("6 – Gerar arquivo de ingressos vendidos para o filme")
            print("7 – Gerenciar promoções")
            print("8 – Gerenciar valores da pipoca")
            print("9 – Voltar ao menu principal")

            opcao = input("Escolha uma opção (ou 'f' para sair): ").strip().lower()

            if opcao == 'f':
                break
            elif opcao == '1':
                cadastrar_filme()
            elif opcao == '2':
                buscar_filme()
            elif opcao == '3':
                atualizar_filme()
            elif opcao == '4':
                remover_filme()
            elif opcao == '5':
                listar_ingressos_por_filme()
            elif opcao == '6':
                gerar_arquivo_ingressos_filme()
            elif opcao == '7':
                gerenciar_promocoes()
            elif opcao == '8':
                gerenciar_valores_pipoca()
            elif opcao == '9':
                break
            else:
                print("\033[91mOpção inválida!!!\033[0m")

def comprar_ingressos():
    print("\nMenu de Compra de Ingressos:")
    nome_usuario = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    usuario = efetuar_login(nome_usuario, senha)
    if usuario and usuario['perfil'] == "CLIENTE":
        while True:
            print("\nOpções de Compra de Ingressos:")
            print("1 – Comprar ingresso")
            print("2 – Comprar pipoca")
            print("3 – Listar ingressos comprados")
            print("4 – Gerar arquivo de ingressos")
            print("5 – Voltar ao menu principal")

            opcao = input("Escolha uma opção (ou 'f' para sair): ").strip().lower()

            if opcao == 'f':
                break
            elif opcao == '1':
                comprar_ingresso(usuario)
            elif opcao == '2':
                comprar_pipoca(usuario)
            elif opcao == '3':
                listar_ingressos_usuario(usuario)
            elif opcao == '4':
                gerar_arquivo_ingressos_usuario(usuario)
            elif opcao == '5':
                break
            else:
                print("\033[91mOpção inválida!!!\033[0m")

def cadastrar_usuario():
    print("\nCadastro de Usuário:")
    nome = input("Digite seu nome: ").strip()
    senha = input("Digite sua senha: ").strip()
    perfil = input("Digite seu perfil (ADM ou CLIENTE): ").strip().upper()

    if nome and senha and perfil in ["ADM", "CLIENTE"]:
        usuarios.append({"nome": nome, "senha": senha, "perfil": perfil})
        print("\033[92mUsuário cadastrado com sucesso!!!\033[0m")
    else:
        print("\033[91mInformações inválidas!!!\033[0m")

def cadastrar_filme():
    titulo = input("Digite o título do filme: ").strip()
    sala = input("Digite o número da sala: ").strip()
    horario = input("Digite o horário (formato HH:MM): ").strip()
    capacidade = input("Digite a capacidade de assentos da sala: ")
    valor = input("Digite o valor do ingresso: ")

    if not capacidade.isdigit() or int(capacidade) <= 0 or not valor.replace('.', '', 1).isdigit() or float(valor) <= 0:
        print("\033[91mValores inválidos!!!\033[0m")
        return

    if not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', horario):
        print("\033[91mFormato de horário inválido!!!\033[0m")
        return

    for filme in filmes:
        if filme['horario'] == horario and filme['sala'] == sala:
            print("\033[91mJá existe um filme cadastrado neste horário e sala!!!\033[0m")
            return

    filmes.append({"titulo": titulo, "sala": sala, "horario": horario, "capacidade": int(capacidade), "valor": float(valor)})
    print("\033[92mFilme cadastrado com sucesso!!!\033[0m")

def listar_filmes():
    print("\nLista de Filmes:")
    for filme in filmes:
        print("\nTítulo:", filme['titulo'])
        print("Sala:", filme['sala'])
        print("Horário:", filme['horario'])
        print("Capacidade:", filme['capacidade'])
        print("Valor:", filme['valor'])

def buscar_filme():
    titulo = input("Digite o título do filme que deseja buscar: ").strip()
    for filme in filmes:
        if filme['titulo'] == titulo:
            print("Filme encontrado:")
            print(f"Título: {filme['titulo']}")
            print(f"Sala: {filme['sala']}")
            print(f"Horário: {filme['horario']}")
            print(f"Capacidade: {filme['capacidade']}")
            print(f"Valor: R${filme['valor']}")
            return
    print("\033[91mFilme não encontrado.\033[0m")

def atualizar_filme():
    titulo = input("Digite o título do filme que deseja atualizar: ").strip()
    for filme in filmes:
        if filme['titulo'] == titulo:
            sala = input("Digite o número da nova sala: ").strip()
            horario = input("Digite o novo horário (formato HH:MM): ").strip()
            capacidade = input("Digite a nova capacidade de assentos da sala: ")
            valor = input("Digite o novo valor do ingresso: ")

            if not capacidade.isdigit() or int(capacidade) <= 0 or not valor.replace('.','',1).isdigit() or float(valor) <= 0:
                print("\033[91mValores inválidos!!!\033[0m")
                return

            if not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', horario):
                print("\033[91mFormato de horário inválido!!!\033[0m")
                return

            filme['sala'] = sala
            filme['horario'] = horario
            filme['capacidade'] = int(capacidade)
            filme['valor'] = float(valor)
            print("\033[92mFilme atualizado com sucesso!!!\033[0m")
            return
    print("\033[91mFilme não encontrado.\033[0m")

def remover_filme():
    titulo = input("Digite o título do filme que deseja remover: ").strip()
    for filme in filmes:
        if filme['titulo'] == titulo:
            filmes.remove(filme)
            print("\033[92mFilme removido com sucesso!\033[0m")
            return
    print("\033[91mFilme não encontrado.\033[0m")

def listar_ingressos_por_filme():
    titulo = input("Digite o título do filme para listar os ingressos vendidos: ").strip()
    for ingresso in ingressos_vendidos:
        if ingresso["Filme"] == titulo:
            print(ingresso)
    else:
        print("\033[91mNão foram encontrados ingressos vendidos para este filme.\033[0m")

def gerenciar_promocoes():
    print("\nMenu de Gerenciamento de Promoções:")
    print("1 – Criar promoção")
    print("2 – Remover promoção") 
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        criar_promocao()
    elif opcao == '2':
        remover_promocao()
    else:
        print("\033[91mOpção inválida!\033[0m")

def criar_promocao():
    titulo = input("Digite o título do filme para a promoção: ").strip()
    desconto = float(input("Digite o valor do desconto (em %): ").strip())

    if desconto < 0:
        print("\033[91mO desconto não pode ser negativo!!!\033[0m")
        return

    for filme in filmes:
        if filme['titulo'] == titulo:
            promocoes.append({"filme": titulo, "desconto": desconto})
            print("\033[92mPromoção criada com sucesso!!!\033[0m")
            return
    else:
        print("\033[91mFilme não encontrado!\033[0m")

def remover_promocao():
    titulo = input("Digite o título do filme para remover a promoção: ").strip()
    for promocao in promocoes:
        if promocao['filme'] == titulo:
            promocoes.remove(promocao)
            print("\033[92mPromoção removida com sucesso!!!\033[0m")
            return
    else:
        print("\033[91mPromoção não encontrada para este filme!!!\033[0m")

def gerenciar_valores_pipoca():
    print("\nMenu de Gerenciamento de Valores da Pipoca:")
    print("1 – Definir valor da pipoca")
    print("2 – Consultar valor da pipoca")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        definir_valor_pipoca()
    elif opcao == '2':
        consultar_valor_pipoca()
    else:
        print("\033[91mOpção inválida!!!\033[0m")

def definir_valor_pipoca():
    valor = input("Digite o valor da pipoca: ")

    if not valor.replace('.','',1).isdigit() or float(valor) <= 0:
        print("\033[91mValor inválido!!!\033[0m")
        return

    global valor_pipoca
    valor_pipoca = float(valor)
    print("\033[92mValor da pipoca definido com sucesso!!!\033[0m")

def consultar_valor_pipoca():
    if 'valor_pipoca' is globals():
        print(f"\nValor da pipoca: R${valor_pipoca:.2f}")
    else:
        print("\033[91mValor da pipoca não definido!!!\033[0m")

def efetuar_login(nome, senha):
    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            return usuario
    print("\033[91mUsuário ou senha incorretos.\033[0m")
    return None

def comprar_ingresso(usuario):
    titulo = input("Digite o título do filme que deseja comprar ingresso: ").strip()
    for filme in filmes:
        if filme['titulo'] == titulo:
            quantidade = input("Digite a quantidade de ingressos que deseja comprar: ")

            if not quantidade.isdigit() or int(quantidade) <= 0:
                print("\033[91mQuantidade inválida!!!\033[0m")
                return

            quantidade = int(quantidade)

            if quantidade <= filme['capacidade']:
                ingressos_vendidos.append({"Usuario": usuario['nome'], "Filme": filme['titulo'], "Quantidade": quantidade})
                filme['capacidade'] -= quantidade
                print(f"\033[92mIngressos comprados com sucesso para o filme!!!{filme['titulo']}!\033[0m")
                return
            else:
                print("\033[91mQuantidade de ingressos solicitada excede a capacidade disponível.\033[0m")
                return
    else:
        print("\033[91mFilme não encontrado.\033[0m")
        return
    
def comprar_pipoca(usuario):
    global valor_pipoca

    if 'valor_pipoca' not in globals():
        print("\033[91mValor da pipoca não definido!!!\033[0m")
        return

    print(f"\nValor da pipoca: R${valor_pipoca:.2f}")
    
    confirmacao = input("Deseja comprar pipoca? (Sim/Não): ").strip().lower()
    if confirmacao == 'sim':
        quantidade = input("Digite a quantidade de pipoca que deseja comprar: ")

        if not quantidade.isdigit() or int(quantidade) <= 0:
            print("\033[91mQuantidade inválida!!!\033[0m")
            return

        quantidade = int(quantidade)
        valor_total = valor_pipoca * quantidade
        print(f"\033[92mCompra realizada com sucesso!!! Total a pagar: R${valor_total:.2f}\033[0m")
    elif confirmacao == 'não':
        print("Compra de pipoca cancelada.")
    else:
        print("\033[91mOpção inválida!!!\033[0m")

def listar_ingressos_usuario(usuario):
    for ingresso in ingressos_vendidos:
        if ingresso["Usuario"] == usuario['nome']:
            print(ingresso)

def gerar_arquivo_ingressos_usuario(usuario):
    nome_arquivo = f"{usuario['nome']}_ingressos.txt"
    arquivo = open(nome_arquivo, "w")
    escritor = csv.DictWriter(arquivo, fieldnames=["Usuario", "Filme", "Quantidade"])
    escritor.writeheader()
    for ingresso in ingressos_vendidos:
        if ingresso["Usuario"] == usuario['nome']:
            escritor.writerow(ingresso)
    arquivo.close()

def gerar_arquivo_ingressos_filme():
    titulo_filme = input("Digite o título do filme para gerar o arquivo de ingressos vendidos: ").strip()
    nome_arquivo = f"{titulo_filme}_ingressos.txt"
    with open(nome_arquivo, "w") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["Usuario", "Filme", "Quantidade"])
        escritor.writeheader()
        for ingresso in ingressos_vendidos:
            if ingresso["Filme"] == titulo_filme:
                escritor.writerow(ingresso)
    print(f"\033[92mArquivo de ingressos vendidos para o filme '{titulo_filme}' gerado com sucesso!!!\033[0m")

menu_principal()
