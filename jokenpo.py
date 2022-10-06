import random

pontuação = {
    'jogador':0,
    'bot':0
}
 
class bot:
    opcB = 0
    def opcBot(self):
        self.opcB = random.randint(1, 3)
        return self.opcB

b = bot()


def menu():
    while True:
        print('-'*20)
        print('     JOKENPO     ')
        print('1 - Jogar;\n2 - Mostrar pontuação;\n3 - Reiniciar o jogo;\n4 - Sair;')
        print('-'*20)

        while True:
            try:
                opc = int(input('Escolha uma opção: '))
                if(opc < 1 or opc > 4):
                    print('Valor inválido!')
                    opc = int(input('Escolha uma opção válida: '))
                break
            except:
                print('Apenas valores númericos')
        if opc == 1:
            jogar()
        elif opc == 2:
            pontuacao()
        elif opc == 3:
            reiniciar()
        else:
            print('-'*20)
            print('Até a proxima!!')
            print('-'*20)
            exit()

def jogar():
    print('Opções:\n1 - Tesoura\n2 - Mão\n3 - Pedra')
    while True:
        try:
            opcj = int(input('Escolha uma opção: '))
            if(opcj < 1 or opcj > 3):
                print('Valor inválido!')
                opcj = int(input('Escolha uma opção válida: '))
            break
        except:
            print('Apenas valores númericos')
    print('-'*20)

    
    if opcj == 1:
        print('Você escolheu: Tesoura')
    elif opcj == 2:
        print('Você escolheu: Mão')
    else:
        print('Você escolheu: Pedra')

    opcB = b.opcBot()
    
    if opcB == 1:
        print('Bot escolheu: Tesoura')

    elif opcB == 2:
        print('Bot escolheu: Mão')
    else:
        print('Bot escolheu: Pedra')


    if(opcj == 1 and opcB == 1):
        print('-'*20)
        print('Houve um empate')
    elif(opcj == 1 and opcB == 2):
        print('-'*20)
        print('Você ganhou!')
        pontuação['jogador'] += 1

    elif(opcj == 1 and opcB == 3):
        print('-'*20)
        print('Você perdeu!')
        pontuação['bot'] += 1

    elif(opcj == 2 and opcB == 1):
        print('-'*20)
        print('Você perdeu!')
        pontuação['bot'] += 1

    elif(opcj == 2 and opcB == 2):
        print('-'*20)
        print('Houve um empate!')
    elif(opcj == 2 and opcB == 3):
        print('-'*20)
        print('Você ganhou!')
        pontuação['jogador'] += 1

    elif(opcj == 3 and opcB == 1):
        print('-'*20)
        print('Você ganhou!')
        pontuação['jogador'] += 1

    elif(opcj == 3 and opcB == 2):
        print('-'*20)
        print('você perdeu!')
        pontuação['bot'] += 1

    elif(opcj == 3 and opcB == 3):
        print('-'*20)
        print('houve um empate!')
    else:
        pass

def pontuacao():
    jogador = pontuação['jogador']
    bot = pontuação['bot']
    print('-'*20)
    print(f'Jogador: {jogador}\nBot: {bot}')

def reiniciar():
    print('-'*20)
    print('O jogo foi reiniciado')
    pontuação['jogador'] = 0
    pontuação['bot'] = 0
    

menu()