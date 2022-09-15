#Projeto 7 e 8 - Jogo de Aventura
#Um jogo de decição onde chego a finais diferentes da minha hisporia de acordo com as reposta que envio para o programa.


import PySimpleGUI as sg
class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você  nasceu no Norte ou no Sul? (N ou S)' #norte é Lado A  e Sul lado B
        self.pergunta2 = 'Você prefere a espada ou o escudo? (Espada ou Escudo)' #Espada = lado Norte. Escudo la Sul
        self.pergunta3 = 'Qual sua especialidade? (Tatico ou Linha de Frente)!' #Atague lado Norte, Devfesa lado Sul
        # Lado 2
        self.finaldaHistoria1 = 'Voce será u heroi n alinha de frente!'
        self.finaldaHistoria2 = 'Você seá u heroi protegendo todos as nossas tropas'
        self.finaldaHistoria3 = 'Você ira se sacrificar na batalha!'
        self.finaldaHistoria4 = 'Você não é capaz de lutat nessa batalha!'

    def Iniciar(Self):
        #Layout
        layout = [
            [sg.Output(size=(55,10))],
            [sg.Input(size=(35,0),key='escolha')],
            [sg.Button('Iniciar o Jogo'), sg.Button('RESPONDER A PERGUNTA')],

        ]

        #criar a janela

        Self.janela =sg.Window('JOGO DE AVENTURA, (A BATANHA', layout=layout)

        while True:
            #ler os dados
            Self.LerValores()
            #Fazer algo com os dados coletados
            if Self.evento == 'Iniciar':
                print(Self.pergunta1)
                Self.LerValores()
                if Self.valores['escoha'] == 'N':
                    print(Self.pergunta2)
                    Self.LerValores()
                    if Self.valores['escolha'] == 'Espada':
                        print(Self.finaldaHistoria1)
                    if Self.valores['escolha'] == 'Escudo':
                        print(Self.finaldaHistoria2)
                if Self.valores['escolha'] == 'S':
                    print(Self.pergunta3)
                    Self.LerValores()
                    if Self.valores['escolha'] == 'Linha de Frente':
                        print(Self.finaldaHistoria3)
                    if Self.valores['escolha'] == 'Tatico':
                        print(Self.finaldaHistoria4)

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()

