import os
import json #  É um formato de aruivo e Usada para manipular arquivos de forma mais facil
import time #Está sendo usada com um timer no codigo
import impressora

arquivo_usuarios = 'usuarios.txt' #Está nomeando o arquivo dos dados de usuario

def limpar_console():
    os.system('cls') #Limpar o console

def salvar_usuarios():
    with open(arquivo_usuarios, 'w') as arquivo: # With = Abrir o arquivo e garantir que apos a execução ele feche adequadamente
#open  = Abrir o arquivo que está no parametro , 'w' é a forma com que ele interagi com o aruivo sendo write
        json.dump(usuarios, arquivo) #.dump é a função que salva as coisa no .json

def carregar_usuarios(): # Ele Verifica de existe o arquivo com os dados de user e apos verificar ele faz uma leitura nele e carrega no código
    if os.path.exists(arquivo_usuarios):
        with open(arquivo_usuarios, 'r') as arquivo:
            return json.load(arquivo)
    else:
        return {} #Caso não ache nenhum aruivo retorna um dicionario com nada

def cadastro():
    limpar_console()
    print("Bem-vindo a tela de cadastro, escolha um usuário e senha:")
    login = input("\nDigite seu login: ")
    senha = input("Digite sua senha: ")
    limpar_console()
    acesso = True
    while acesso:
        if login in usuarios: #Verica de o login que digitou ja está cadastrado
            print("\nLogin já existe. Tente novamente.")
            login = input("\nDigite seu login: ")
            senha = input("Digite sua senha: ")
            limpar_console()
        else:
            usuarios[login] = senha #Se não ele salva em um dicionario
            salvar_usuarios()
            print("\nCADASTRO FEITO COM SUCESSO!!")
            time.sleep(2)
            acesso = False

def logar():
    print("BEM-VINDO A TELA DE LOGIN!!\n")
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    limpar_console()
    acesso = True
    while acesso:
        if login in usuarios and usuarios[login] == senha: #Verifica se a senha e o login estão no arquivo json
            acesso = False # Caso sim, ele sai desse loop
            limpar_console()
        else:
            print("Usuário ou senha inválido")
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            limpar_console()



usuarios = carregar_usuarios()

next = True
while next:
    limpar_console()
    print("OLÁ SEJA BEM-VINDO AO NOSSO SISTEMA DE IMPRESSORA!!\n"
          "\nEscolha uma das opções a seguir: ")
    r = int(input("1 - Logar\n"
              "2 - Cadastre-se\n"
              "\nOpção número: "))



    if r == 1:
        limpar_console()
        logar()
        retorno = impressora.AbreConexaoImpressora(1, 'i9', 'USB', 0)
        if retorno == 0:
            print("LOGADO COM SUCESSO!!!")
            next = False
        else:
            limpar_console()
            print("!!!ERRO!!! NENHUMA IMMPRESSORA CONECTADA...")
            time.sleep(3)
        limpar_console()

    elif r == 2:
        cadastro()
        limpar_console()
    else:
        limpar_console()
        print("Opção inválida")
        time.sleep(1)


encerrar = True
while encerrar:
    limpar_console()
    print("Seja bem-Vindo ao MENU de impressão!\n")
    o = int(input("Escolha uma das opções abaixo:\n"
                  "1 - Imprimir texto\n"
                  "2 - Imprimir QR code\n"
                  "3 - Imprimir XML SAT\n"
                  "4 - Fechar sistema\n"
                  "\nOpção número: "))
    if o >= 1 and o <= 4:
        try:
            if o == 1:
                limpar_console()
                texto = input("Digite o texto a ser impresso:\n"
                              "\n"
                              "- ")
                limpar_console()
                next = True
                while next:
                    posicao = int(input("Posição do texto\n"
                          "1 - Esquerda\n"
                          "2 - Centro\n"
                          "3 - Direita\n"
                          "\nOpção número: "))
                    limpar_console()

                    if posicao == 1:
                        posicao = 0
                        next = False
                    elif posicao == 2:
                        posicao = 1
                        next = False
                    elif posicao == 3:
                        posicao = 2
                        next = False
                    else:
                        print("Opção inválida, Digite novamente.")
                        posicao = int(input("\nPosição do texto\n"
                          "1 - Esquerda\n"
                          "2 - Centro\n"
                          "3 - Direita\n"
                          "\nOpção número: "))
                        limpar_console()

                next = True
                while next:
                    limpar_console()
                    estilo2 = int(input("Escolha o estilo do texto:\n"
                                        "1 - Normal\n"
                                        "2 - Sublinhado\n"
                                        "3 - Modo reverso\n"
                                        "4 - Negrito\n"
                                        "Opção número: "))
                    limpar_console()

                    if estilo2 == 1:
                        somaestilo = 0
                        next = False
                    elif estilo2 == 2:
                        somaestilo = 0 + 2
                        next = False
                    elif estilo2 == 3:
                        somaestilo = 0 + 4
                        next = False
                    elif estilo2 == 4:
                        somaestilo = 0 + 8
                        next = False
                    else:
                        print("Opção inválida!!")
                        estilo2 = int(input("Escolha o estilo do texto:\n"
                                            "1 - Normal\n"
                                            "2 - Sublinhado\n"
                                            "3 - Modo reverso\n"
                                            "4 - Negrito\n"
                                            "Opção número: "))
                        limpar_console()

                next = True
                while next:
                    somala = 0
                    altura = int(input("Escolha a altura do texto (Para altura e largura padrão digite 0):\n"
                                       "0 - Padrão\n"
                                       "1 - 2x na altura\n"
                                       "2 - 3x na altura\n"
                                       "3 - 4x na altura\n"
                                       "4 - 5x na altura\n"
                                       "5 - 6x na altura\n"
                                       "6 - 7x na altura\n"
                                       "7 - 8x na altura\n"
                                       "\nOpção número: "))
                    limpar_console()

                    largura = int(input("Escolha a largura do texto (Para altura e largura padrão digite 0):\n"
                                       "0 - Padrão\n"
                                       "1 - 2x na largura\n"
                                       "2 - 3x na largura\n"
                                       "3 - 4x na largura\n"
                                       "4 - 5x na largura\n"
                                       "5 - 6x na largura\n"
                                       "6 - 7x na largura\n"
                                       "7 - 8x na largura\n"
                                       "\nOpção número: "))
                    limpar_console()

                    if altura == 0 and largura == 0:
                        somala = 0
                        next = False
                    elif altura < 8 and largura < 8:
                        if largura == 1:
                            somala = altura + 16
                        elif largura == 2:
                            somala = altura + 32
                        elif largura == 3:
                            somala = altura + 48
                        elif largura == 4:
                            somala = altura + 64
                        elif largura == 5:
                            somala = altura + 80
                        elif largura == 6:
                            somala = altura + 96
                        elif largura == 7:
                            somala = altura + 112

                        next = False
                    else:
                        print("Erro, Digite as informações novamente!")
                        time.sleep(1)
                        limpar_console()

                limpar_console()
                retorno = impressora.ImpressaoTexto(texto, posicao, somaestilo, somala)
                impressora.Corte(5)
                print("Imprimindo...")
                time.sleep(3)
        except Exception as retorno:
            print(f"Erro {retorno}, Voltando ao menu")
            time.sleep(2)
            limpar_console()
        try:
            if o == 2:
                limpar_console()
                dados = input("Digite uma mensagem ou link para o QRCode: ")
                limpar_console()
                next =True
                while next:
                    tamanho = int(input("Digite o tamanho do QRCode (entre 1 e 6): "))
                    if tamanho < 1 or tamanho > 6:
                        print("Valor inválido, digite novamente.")
                        time.sleep(1)
                        limpar_console()
                    else:
                        next = False
                        limpar_console()
                next = True
                while next:
                    limpar_console()
                    nivel = int(input("Escolha o nível de correção (entre 1 e 4): "))
                    if nivel < 1 or nivel > 4:
                        print("Valor inválido, digite novamente.")
                        time.sleep(1)
                        limpar_console()
                    else:
                        next = False
                        limpar_console()

                retorno = impressora.ImpressaoQRCode(dados, tamanho, nivel)
                impressora.Corte(5)

                print("Imprimindo o QR code....")
                time.sleep(2)
        except Exception as retorno:
            print(f"Erro {retorno}, Voltando ao menu")
            time.sleep(2)
            limpar_console()
        try:
            if o == 3:
                limpar_console()
                dados = 'path=XMLSAT.xml'
                retorno = impressora.ImprimeXMLSAT(dados, 0)
                impressora.Corte(5)
                print("Imprimindo...")
                time.sleep(2)
        except Exception as retorno:
            print(f"Erro {retorno}, Voltando ao menu")
            time.sleep(2)
            limpar_console()
        try:
            if o == 4:

                fechar = input("Você deseja realmente fechar o sistema? (S/N)\n"
                               "Resposta: ").lower()

                if fechar == 's':
                    encerrar = False
                    impressora.FechaConexaoImpressora()
                elif fechar == 'n':
                    print()
                else:
                    print("\nOpção inválida...")
                    limpar_console()
                    print("Retornando ao Menu...")
                    time.sleep(2)
        except Exception as retorno:
            print(f"Erro {retorno}, Voltando ao menu")
            time.sleep(2)
            limpar_console()
    else:
        limpar_console()
        print("OPÇÃO INVALIDA!!!")
        time.sleep(2)

