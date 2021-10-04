# PUCPR
# Matheus Leonardi Balão
# Disciplina Raciocínio Computacional
# Atividade Somativa 1 - Zombie DICE


# Bibliotecas utilizadas

from time import sleep
from collections import namedtuple
from random import *

# Declaração da classe

class Zombie_Dice:
    # Variáveis e estruturas de dados
    rodada = 1
    tubo = []
    lista_de_jogadores = []
    Dados = namedtuple("Cor", ["verde", "amarelo", "vermelho"])
    dado = Dados("CPCTPC", "TPCTPC", "TPTCPT")

    # Print divisor
    def print_linha(self):
        print("*" * 64)

    # Pedir número de jogadores
    def numero_jogadores(self):
        resposta = int(input("Quantos jogadores vocês são? (2-9)\n"))
        self.print_linha()
        if resposta < 2 or resposta > 9:
            print("Número de zumbis inválido, escolha entre 2 e 9 jogadores")
        else:
            for indice in range(resposta):
                sleep(0.5)
                nome = input(f"Digite o nome do jogador {indice + 1}:\n")
                self.print_linha
                cerebros = 0
                tiros = 0
                passos = 0
                # Estrutura de dados para contabilização
                jogador = [indice, nome, cerebros, tiros, passos]
                self.lista_de_jogadores.append(jogador)

    # Colocar dados no tubo
    def carregar_tubo(self):
        # Adicionar dados verdes no tubo
        self.tubo = []
        for i in range(6):
            self.tubo.append(self.dado.verde)
        # Adicionar dados amarelos no tubo
        for i in range(4):
            self.tubo.append(self.dado.amarelo)
        # Adicionar dados vermelhos no tubo
        for i in range(3):
            self.tubo.append(self.dado.vermelho)

    # Exibir rodada
    def exibir_rodada(self):
        self.print_linha()
        rodada = f"{self.rodada:02d}"
        print(f"{'RODADA ' + rodada:^64}")
        self.print_linha()

    # Apresentar score
    def apresentar_score(self):
        for jogador in self.lista_de_jogadores:
            print(f"{jogador[0] + 1} {jogador[1]}: {jogador[2]} cérebros.")
            self.print_linha()

    # Zerar tiros
    def zerar_tiros(self):
        for jogador in self.lista_de_jogadores:
            jogador[3] = 0

    # Contar os dados dentro do tubo
    def contar_dados_tubo(self):
        dados_verdes = 0
        dados_amarelos = 0
        dados_vermelhos = 0
        for dado in self.tubo:
            dados_verdes += 1 if dado == self.dado.verde else 0
            dados_amarelos += 1 if dado == self.dado.amarelo else 0
            dados_vermelhos += 1 if dado == self.dado.vermelho else 0
        print(
            f'Dados no tubo: {dados_verdes} verdes, {dados_amarelos} amarelos e {dados_vermelhos} vermelhos.')
        self.print_linha()

    # Verificar vitória

    def verificar_vitoria(self):
        for jogador in self.lista_de_jogadores:
            if jogador[2] >= 13:
                print(
                    f"VITORIOSOO! {jogador[1]} Tá com a pança cheia de cérebros!")
                exit()

    # Verificar a cor do dado
    def cor_dado(self, dado_sorteado):
        cor = ''
        if dado_sorteado == self.dado.verde:
            cor = "DADO VERDE"
        elif dado_sorteado == self.dado.amarelo:
            cor = "DADO AMARELO"
        else:
            cor = "DADO VERMELHO"
        return print(cor)

    # Tirar três dados do tubo
    def tirar_dados(self, jogador):
        print(f"Rolando os dados para {jogador[1]}:")
        self.print_linha()
        for i in range(3):
            sleep(1)
            numero_sorteado = randint(0, len(self.tubo) - 1)
            # Dado sorteado
            dado_sorteado = self.tubo[numero_sorteado]
            # Face sorteada
            face_sorteada = randint(0, 5)
            # Verificar face
            self.cor_dado(dado_sorteado)
            if dado_sorteado[face_sorteada] == "C":
                print("CÉÉREBRO!!")
                print("Você comeu um cérebro!")
                self.tubo.pop(numero_sorteado)
                self.contar_dados_tubo()
                jogador[2] += 1

            elif dado_sorteado[face_sorteada] == "T":
                print("TIIIRO!")
                print("Você levou um tiro!")
                self.tubo.pop(numero_sorteado)
                self.contar_dados_tubo()
                jogador[3] += 1

            else:
                print("PASSOS!")
                print("A vítima escapou nessa rodada!")
                self.tubo.pop(numero_sorteado)
                self.contar_dados_tubo()
                self.tubo.append(dado_sorteado)
                jogador[4] += 1
            self.print_linha()

        self.print_linha()
        print(f"{jogador[1]}, você tem {jogador[2]} cérebros e {jogador[3]} tiros")
        if jogador[3] < 3:
            continuar_resposta = input(
                f"{jogador[1]} continuar jogando os dados? (S/N) \n")
            if (continuar_resposta == "S" or continuar_resposta == "s"):
                self.tirar_dados(jogador)
        else:
            print(
                f"Vishh {jogador[1]}, você levou {jogador[3]} tiros e zerou seu cemitério de cérebros.")
            sleep(0.5)
            print("Passando a jogada para o próximo jogador...")
            sleep(0.5)
            jogador[2] = 0
            sleep(1)
            self.print_linha()

    # Função jogar
    def jogar(self):
        while True:
            self.print_linha()
            print("=                       JOGO ZOMBIE DICE                       =")
            self.print_linha()
            print("Bem-vindos, zumbis.")
            sleep(0.8)
            self.numero_jogadores()
            self.carregar_tubo()
            self.print_linha()
            print("=                      VAMOS COMEÇAR O JOGO                    =")
            self.print_linha()
            sleep(1)
            self.print_linha()
            print("=                        ROLANDO OS DADOS...                   =")
            self.print_linha()

            while True:
                for jogador in self.lista_de_jogadores:
                    self.tirar_dados(jogador)
                    if jogador[0] == self.lista_de_jogadores[len(self.lista_de_jogadores) - 1][0]:
                        self.rodada += 1
                        self.exibir_rodada()
                        self.zerar_tiros()
                        self.verificar_vitoria()
                    self.carregar_tubo()


# Começar jogo
Game01 = Zombie_Dice()
Game01.jogar()
