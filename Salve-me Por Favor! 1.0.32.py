from time import sleep

print("""Epilogo

Era um dia qualquer de chuva em Junho...

Chovia litros do lado de fora da minha casa como se algum deus tivesse esquecido a torneira ligada, 
se fosse apenas água, menos mal, mas aqueles relânpagos me deixavam receosso de um apagão.

Eu estava lendo um mangá, que acompanhava a varios anos e leria o finalmente o final naquele dia...

Para a minha decepção o final era horrivel, nada fazia sentido, os personagems que eu gostariam que ficasem juntos, 
não ficavam, pernsonagems que eu gostava morreram em vão...

Uma perda de tempo.

Foi quando de repente.

Houve um relâmpago forte e minha tela ficou toda preta. 
Por um breve momento tive um micro infarto achando que meu computador tinha queimado.
Foi quando prestei mais atenção na tela, era um Cmd ou Console de gerenciamento da Murdersoft Wind.
Aquela tela era a que geralmente só hacker em filmes entendem, tudo preto é um bocado de letras.
Eu estva prestes a desligar o computador na tomada para ir dormir quando...

""")

def clear():
    sleep(3)
    print("\nCarregando...\n")
    sleep(2)
    print("Recebido\n")
    print("\n\n\n")
    
def tela01():

    print()
    sleep(5)
    print("Tem alguem ai?")
    sleep(3)

    print("\n[ 1 ] Sim \n[ 2 ] Não \n[ 3 ] Não responder")
    escolha = int(input("\nEnviar: "))
    
    clear()

    if escolha == 1:
        print("Que bom! Preciso da sua ajuda. Fui sequestrada!")
        sleep(2)
        tela02()
    elif escolha == 2:
        print("Se não tem ninguém porque respondeu?")
        sleep(2)
        tela01_1()
    else:
        print("Tem alguém ai? Alguém, por favor")
        sleep(2)
        tela01_1()


def tela01_1():
    clear()
    print("Preciso de ajuda! Me sequestraram, estou presa!\n")
    sleep(3)
    print("SOCORRO!!!")
    print("\n[ 1 ] Vai passar trote para outro! (Desligar). \n[ 2 ] Tá bom, conte mais. \n[ 3 ] ... (Não responder).")
    escolha = int(input("\nEnviar: "))

    if escolha == 1:
        print("FIM DE JOGO")
    elif escolha == 2:
        print("Que bom!")
        sleep(2)
        tela02()
    else:
        print("Acho que esse é o meu fim...\n")
        print("FIM DE JOGO")


def tela02():
    clear()
    print("Estou em um tipo de quarto, não sei como cheguei aqui nem quanto tempo se passou.")
    print("Só sei que preciso escapar o mais rápido possível, sinto que não tenho muito tempo.")

    print("\n[ 1 ]  Quem é você? \n[ 2 ]  Como está conseguindo me mandar mensagens? \n[ 3 ]  Não vou cair nessa, vai passar trote para outro. (Desligar)")
    escolha = int(input("\nEnviar: "))

    if escolha == 1:
        sleep(2)
        tela02_1()
    elif escolha == 2:
        sleep(2)
        tela02_2()
    else:
        print("FIM DE JOGO")


def tela02_1():
    clear()
    print("Meu nome é Perséfone, tenho 15 anos e eu morova em Atenas na Grecia")

    print("\n[ 1 ] Como está conseguindo me mandar mensagens? \n[ 2 ] Não vou cair nessa, vai passar trote para outro. (Desligar) \n[ 3 ] Como é o sequestrador?")

    escolha = int(input("\nEnviar: "))
    
    if escolha == 1:
        sleep(2)
        tela02_1_1()
    elif escolha == 2:
        print("FIM DE JOGO")
    else:
        print("Ele é alto e veste um sobretudo, ele usa um tipo de capacete que não da para ver o rosto")
        sleep(3)
        tela02_1_2()


def tela02_1_1():
    clear()
    print("Não me pergunte como, mas consegui roubar o celular do sequestrador.")
    print("Ele não faz ligações, no entanto dei um jeito de conseguir se conectar a servidores próximos.")
    sleep(4)
    tela02_3()


def tela02_1_2():
    clear()
    print("[ 1 ] Então, Perséfone, como está conseguindo se comunicar comigo?")
    print("[ 2 ] A brincadeira está boa Perséfone, mas tenho mais o que fazer. (Desligar)")

    escolha = int(input("\nEnviar: "))

    if escolha == 1:
        sleep(2)
        tela02_1_1()
    else:
        print("FIM DE JOGO")


def tela02_2():
    clear()
    print("Conseguir roubar o celular do sequestrador! ")
    sleep(1)
    print("Não me pergunte como, só sei que não tenho muito tempo até ele perceber.")
    print("\n")

    print("[ 1 ] Já que está com um celular, ligue para a polícia! Eles vão te achar.")
    print("[ 2 ] Como conseguiu se comunicar comigo?")
    print("[ 3 ] Não vou cair nessa, vai passar trote para outro. (Desligar)")

    escolha = int(input("\nEnviar: "))

    if escolha == 1:
        print("Eu já tentei, mas não tive sucesso. Acho que esse aparelho não faz ligações")
        sleep(2)
        tela02_2_1()
    elif escolha == 2:
        sleep(2)
        tela02_2_2()
    else:
        print("FIM DE JOGO")


def tela02_2_1():
    clear()
    print("[ 1 ] Então, como conseguiu se comunicar comigo?")
    print("[ 2 ] Então irei ligar para a polícia e informar, só aguarde um momento. (Sair e ligar para a polícia)")
    print("[ 3 ] Não acredito, vai passar trote para outro. (Desligar)")

    escolha = int(input("\nEnviar: "))

    if escolha == 1:
        sleep(2)
        tela02_2_2()
    elif escolha == 2:
        sleep(2)
        tela02_2_3()
    else:
        print("FIM DE JOGO")


def tela02_2_2():
    clear()
    print("Uma vez vi um amigo meu se conectar a um servidor próximo, apenas de zueira para mandar uma mensagem,um trote")
    print("Nunca pensei que usaria esse conhecimento assim. Com esse aparelho, ele é velho.")
    print("Só consegui me comunicar com você é apenas por mensagem, enviando a servidores próximos e só você respondeu.")
    print("\n")

    print("[ 1 ] Então, quem é você?")
    print("[ 2 ] Como é o sequestrador?")
    print("[ 3 ] Chega, vou parar por aqui. (Desligar)")

    escolha = int(input("\nEnviar: "))

    if escolha == 1:
        print("Meu nome é Perséfone, tenho 15 anos e moro em Atenas")
        sleep(2)
        tela02_3()
    elif escolha == 2:
        print("Ele é alto e veste um sobretudo marrom, seu rosto é coberto.")
        print("usa um chapéu com abas longas (que lembra o chapéu que meu tio usava para pescar).")
        sleep(2)
        tela02_2_4()
    else:
        print("FIM DE JOGO")


def tela02_2_3():
    clear()
    print("Ei, e o que faço? O sequestrador vai voltar a qualquer momento.")
    sleep(2)
    print("Diga alguma coisa, se ele chegar não sei o que vai acontecer comigo.")
    sleep(2)
    print("Me ajuda, por favor!!!")
    print("...")
    sleep(3)
    print("VOU TE ENCONTRAR!")


    print("\n")
    print("")
    print("""Algum tempo depois…
A polícia demorou quase dois dias para rastrear as mensagens e quando encontrou o local já era tarde demais, a garota já estava morta e o assassino tinha fugido sem deixar pistas.
Agora, uma semana após o crime, as suspeitas estão caindo sobre mim. Não os culpo, já que é muito estranho a forma como tudo aconteceu, mas o que realmente me preocupa é a última mensagem enviada. Isso sim está mexendo comigo, me dá calafrios pensar que posso ser a próxima vítima.
""")


def tela02_2_4():
    clear()
    print("[ 1 ] Então quem é você? ")
    print("[ 2 ] Chega, vou parar por aqui. (Desligar)")

    escolha = int(input("\nEnviar: "))

    if escolha == 1:
        print("Meu nome é Perséfone, tenho 15 anos e moro em Atenas")
        sleep(2)
        tela02_3()
    elif escolha == 2:
        print("Ele é alto e veste um sobretudo marrom, seu rosto é coberto.")
        print("usa um chapéu com abas longas (que lembra o chapéu que meu tio usava para pescar).")
        sleep(2)
        tela02_2_4()
    else:
        print("FIM DE JOGO")


def tela02_3():
    clear()
    print("[ 1 ] Como posso te ajudar?")
    print("[ 2 ] Descreva o local onde está.")
    print("[ 3 ] Não acredito em nada que você me disse. Tchau. (Desligar)")

    escolha = int(input("\nEnviar: "))

    if escolha == 1:
        print("""Estou presa em um quarto, talvez se você pudesse me dar alguma idéia de como posso 
sair daqui, ou sei lá, se você soubesse alguma forma rápida de rastrear as mensagens que 
estou te enviando para chegar até aqui.""")
    elif escolha == 2:
        sleep(2)
        tela03()
    else:
        print("FIM DE JOGO")


def tela03():
    clear()
    print("""
Estou em algum tipo de bunker, tem pouca luz,luz apenas de lampadas amareladas, 
não há janelas, apenas uma porta grande e que parece grossa...
Eu estou ouvindo passo não tenho muito tempo, por favor me ajude!!! 
vou tentar me esconder em baixo da cama que eu estava presa...



CONTINUA...
""")

tela01()
input()