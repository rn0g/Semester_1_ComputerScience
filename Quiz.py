import os
from os import system
import platform
import datetime
import time
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
###############################################
## DECLARACAO FUNCOES
## 

def links_sobre_investimento():
    html = urlopen("https://blog.cedrotech.com/7-principais-e-melhores-sites-sobre-investimentos")
    bsObject = BeautifulSoup(html, "html.parser")
    titles = bsObject.findAll("h2")
    titles.pop()
    print("Segue abaixo alguns sites que podem ser consultados para educar-se sobre investimentos:\n\n")
    for i in titles:
        print(i.text)


def sobre():
    system("cls")
    print("O tema do quiz é investimento educacional.\n")
    print("No Brasil, uma pesquisa datou que apenas 3% dos brasileiros investiram em ações em 2020. Pessoalmente, escolhi este tema porque acredito que a falta de educação financeira e economica nas instituições brasileiras é um problema. Acredito que todos indivíduos deveriam completar 18 anos sabendo pelo menos como funciona a Bolsa de Valores do seu país.\n")
    print("É importante ensinar aqueles que praticam o ensino nas instituições a fazer escolhas financeiras. O quiz é voltado para testar este conhecimento, que reflete um dos problemas educacionais no Brasil.")
    print("Este quiz foi desenvolvido por [ma_name], estudante de Ciência da Computação na **********.")
    input("Aperte enter para continuar...")

def fatos_aleatorios():
    fatos = ["Alguns gatos são alérgicos a humanos", "A maior parte do seu cérebro é gordura.", " A bandeira dos EUA foi desenhada por um estudante, como parte de um trabalho na escola. A nota que ele recebeu foi mediana.", "São necessárias 364 lambidas para se chegar ao centro de um pirulito"]
    random.seed(datetime.datetime.today())
    random.shuffle(fatos)
    print("-->", fatos[0],"\n\n")
    input("Aperte enter para retornar...")

def welcome():
    system("cls")
    user = os.getlogin()  
    system_ = platform.system()  
    date = datetime.date.today()
    
    print("e\t\t\t\t\t\tBem-vindo,", user )
    print("Plataforma:",system_ )
    print("")
    print("Data:",date )
    print("")

def introduction():
    print("Este quiz é um quiz criado para testar o seu conhecimento em relação a área de investimentos.")
    print("Foram criadas 10 questões com múltiplas escolhas e cada questão vale um total de 1 ponto. A pontuação máxima é de 10 pontos.")
    print("O quiz é voltado para maiores de 16 anos e para qualquer um que queira aprender.")
    print("No final do quiz, a sua pontuação será demonstrada e será arquivada no arquivo 'arquivo_quiz.txt' no diretório desse programa")
    print("\n")
    print("1) Começar o quiz")
    print("2) Sites para estudo sobre a bolsa de valores")
    print("3) Fatos aleatórios")
    print("4) Sobre")
    print("5) Sair")
    print("\n")
    choice = input("Input: ")
    if choice == '1':
        return 1
    if choice == '2':
        return 2
    if choice == '3':
       return 3
    if choice == '4':
        return 4
    if choice == '5':
        return 5
    
def quiz():
    arquivo = open("arquivo_pontuacao.txt", "a+")
    points = 0
    incorrect = 0
    answers = ['A', 'C', 'C', 'D', 'E', 'A', 'C', 'C', 'A', 'B']

    print("Comecando o quiz em ")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    system('cls')

    print("Questão 1) O que é uma ação:") ## A correto
    print("A) A menor parte de uma empresa de capital aberto, negociada livremente na Bolsa de Valores")
    print("B) É todo o capital de uma empresa")
    print("C) Dinheiro de uma empresa mantido em um cofre.")
    print("D) O planejamento de uma empresa para a criação de um produto")
    print("E) Quando os funcionários de uma empresa protestam")

    input_ = input("Letra: ").upper()
    if input_ == answers[0]:
        points = points + 1
        print("Correto!")
        print("Avançando...")
        time.sleep(2)
        system('cls')
    else:
        incorrect = incorrect + 1
        print("Incorreto. A resposta correta é A.")
        print("Avançando...")
        time.sleep(5)
        system('cls')
    
    print("Questão 2) Quanto dinheiro é necessário para começar a investir?") ##  C correto
    print("A) R$100,00\nB) R$10,000,00\nC) Não existe uma quantia exata\nD) R$50,00\nE) R$500,00")
    
    input_ = input("Letra: ").upper()
    if input_ == answers[1]:
        points = points + 1
        print("Correto!")
        print("Avançando...")
        time.sleep(2)
        system('cls')
    else:
        iincorrect = incorrect + 1
        print("Incorreto. A resposta correta é C. Não existe uma quantia mínima para começar a investir.")
        print("Avançando...")
        time.sleep(5)
        system('cls')
    
    print("Questão 3) O que é o Ibovespa?") ## C correto
    print("A) Uma empresa localizada em São Paulo\nB) Refere-se ao lugar onde são realizadas as operações de compra e venda de ações\nC) Índice que contém 84 ações que são compradas e vendidas na B3\nD) Uma medida de preço\nE) Nenhuma das acima")

    input_ = input("Letra: ").upper()
    if input_ == answers[2]:
        points = points + 1
        print("Correto!")
        print("Avançando...")
        time.sleep(2)
        system("cls")
    else:
        print("Incorreto. A resposta correta é", answers[2], ". O Ibovespa é o índice indicador mais importante da B3.")
        print("Avançando...")
        incorrect = incorrect + 1
        time.sleep(5)
        system("cls")
    
    print("Questão 4) Você comprou o equivalente a R$2000,00 de ações de uma companhia. O valor da ação caiu 50%. Você decide vender. Aproximadamente quanto do valor original investido você tem?") ## CORRETO D
    print("A) R$450,00")
    print("B) R$1200,00")
    print("C) R$780,00")
    print("D) R$1000,00")
    print("E) R$00,00")    
    
    input_ = input("Letra: ").upper()
    if input_ == answers[3]:
        points = points + 1
        print("Correto!")
        print("Avançando...")
        time.sleep(3)
        system("cls")
    else: 
        incorrect = incorrect + 1
        print("Incorreto. A resposta correta é", answers[3], ". Se o valor caiu pela metade, então 50 porcento de $2000 = $1000.")
        print("Avançando...")
        time.sleep(5)
        system("cls")
    
    print("Questão 5) Day Trading é a rápida compra e venda de ativos no mesmo dia na esperança de realizar um lucro rápido. Qual das seguintes opções é verdadeira?") ## INCORRETO E PQ?
    print("A) Pode ser arriscado ")
    print("B) Pode-se consumir tempo")
    print("C) É uma estratégia de investimento de curto-prazo")
    print("D) Não há limites de compra e venda")
    print("E) Todas acima")

    input_ = input("Letra: ").upper()
    if input_ == answers[4]:
        print("Correto!")
        points = points + 1
        print("Avançando...")
        time.sleep(3)
        system("cls")
    else:
        print("Incorreto. A resposta correta é", answers[4], ". Todas as opções estão corretas.")
        incorrect = incorrect + 1
        print("Avançando...")
        time.sleep(5)
        system("cls")
    
    print("Questão 6) Opções no mercado financeiro são: ")
    print("A) Representam um contrato que da ao seu titular o direito de comprar ou de vender um determinado ativo por um valor determinado em uma data especifica do futuro")
    print("B) Escolhas diferentes que o investidor tem na hora de comprar uma acao")
    print("C) Diferentes tipos de contas de investimento disponiveis para abrir uma conta na corretora")
    print("D) Diferentes acoes na bolsa")
    print("E) Nenhuma das acima")

    input_ = input("Letra: ").upper()
    if input_ == answers[5]:
        print("Correto!")
        points = points+1
        print("Avançando...")
        time.sleep(3)
        system("cls")
    else:
        print("Incorreto. A resposta correta é", answers[5], ". Opções também é um modo de investimento de alto-risco.")
        incorrect = incorrect + 1
        print("Avançando...")
        time.sleep(5)
        system("cls")

    print("Questão 7) Como funciona a variação de preço de uma companhia na bolsa de valores?")
    print("A) A companhia decide o preco de sua ação")
    print("B) Um algoritmo desenvolvido pela companhia decide o preco que vai ser tal ação")
    print("C) O preço varia conforme a oferta e a demanda variam")
    print("D) O CEO da companhia deve negociar o preco")
    print("E) O preco varia conforme a companhia teve um dia bom ou ruim")

    input_ = input("Letra: ").upper()
    if input_ == answers[6]:
        print("Correto!")
        points = points + 1
        print("Avançando...")
        time.sleep(3)
        system("cls")
    else:
        print("Incorreto. A resposta correta é", answers[6], ". Opções também é um modo de investimento de alto-risco.")
        incorrect = incorrect + 1
        print("Avançando...")
        time.sleep(5)
        system("cls")

    print("Questão 8) Quais das companhias abaixo deu um retorno maior se em 2010 Susan comprou 300 ações nas seguintes companhias e retirou seu retorno em 2021? [FORMATO: $SIGLA -[2010-2021]")
    print("A) AAPL - [$30-$150]")
    print("B) MSFT - [$30-$336]")
    print("C) TSLA - [$17-$1013]")
    print("D) F - [$10-19.45]")
    print("E) META - [$22-$339") ## resposta = C

    input_ = input("Letra: ").upper()
    if input_ == answers[7]:
        print("Correto!")
        print("Avançando...")
        points = points + 1
        time.sleep(2)
        system("cls")
    else:
        print("Incorreto! A empresa que mais subiu desde 2010 foi a TSLA")
        incorrect = incorrect + 1
        time.sleep(5)
        system("cls")

    print("Questão 9) O que é diversificação de ativos?")
    print("A) Distribuição de capital em diferentes tipos de aplicações, reconhecido como 'não colocar todos os ovos na mesma cesta'")
    print("B) A compra de vários ativos da mesma companhia")
    print("C) Você vende o seu crypto e compra ações")
    print("D) Mudar o seu tipo de investimento")
    print("E) Nenhuma das acima")
    input_ = input("Letra: ").upper()
    if input_ == answers[8]:
        points = points + 1
        print("Correto!")
        print("Avançando...")
        time.sleep(2)
        system("cls")
    else:
        print("Incorreto. A diversificação é quando você diversifica o seu capital para diferentes ações ou industrias. A resposta correta é A.  ")
        incorrect = incorrect + 1
        system("CLS")
    
    print("Questão 10) Pode-se dizer sobre as bolsas de valores que:")
    print("A) É um orgão do governo, que regula a economia")
    print("B) Podemos dizer que a bolsa é a melhor opção para diagnosticar sinais de crise ou ótimos momentos de investimento em ações, títulos de capitalização, poupança, imóveis, negócios imobiliários e constituição do negócio próprio.")
    print("C) A bolsa de valores é ruim para o país")
    print("D) A bolsa de valores é a economia do país")
    print("E) A bolsa de valores ajuda bancos a saberem se devem ou não emprestar dinheiro para determinada empresa")
    
    input_ = input("Letra: ").upper()
    if input_ == answers[9]:
        print("Correto!")
        points = points + 1
        print("Avançando...")
        time.sleep(2)
        system("cls")
    else:
        print("Incorreto. A resposta correta é B. A bolsa de valores é um ótimo indicador de crises ou ótimos momentos do país")
        incorrect = incorrect+1
        print("Avançando...")
        time.sleep(3)
        system("cls")
    
    print("\t\t\t\t\tFim de quiz, parabéns por chegar até o final. Vamos ver a sua pontuação...")
    time.sleep(2)
    print("Corretas: ", points)
    print("Incorretas: ", incorrect)
    time.sleep(2)
    if points == 10:

        print("Parabéns, você TIROU 10! Parece que você está pronto para começar uma jornada no mercado de ações.")
    if points < 10:
        print("Quase lá! De uma olhada nos links no acesso de Links Para Estudo (2)")
    print("Um arquivo .txt com sua pontuação foi gerado no diretório deste quiz.")
    arquivo.write("Corretas: %i\n" %points)
    arquivo.write("Incorretas: %i\n" %incorrect)
    input("Aperte enter para continuar...")    

###########
##Programa
continuar = True
while continuar == True:
    welcome()
    lets_go = introduction()

    if lets_go == 1:
        quiz()

    if lets_go == 2:
        system('cls')
        links_sobre_investimento()
        input("Pressione a tecla 'enter' para voltar ao menu principal...")
        print("Voltando...")
        time.sleep(3)
        system('cls')
    if lets_go == 4:
        sobre()

    if lets_go == 5:
        print("Saindo...")
        time.sleep(2)
        continuar = False
    if lets_go == 3:
        fatos_aleatorios()

## Fim.

