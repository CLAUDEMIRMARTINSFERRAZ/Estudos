
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_mimimo = 1
        self.valor_maximo = 6

         #Layout
       self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button ('Sim'),sg.Button ('Não')]
        ]
        
    def Iniciar(self):
        #Criar uma janela
        self.janela = sg.Window ('Simulador De Dado', Layout=self.layout)

        #Ler os valores da Tela
        self.eventos, self.valores = self.janela.Read()

        #Fazer alguma coisa com esses valores
            try:
                if self.eventos =='Sim' or self.eventos == 's':
                    self.GerarValorDoDado()
                elif self.eventos == 'Não' or self.eventos == 'n':
                    print ('Agradecemos sua participação!')
                else:
                    print ('Favor digite Sim ou Não !!!')
            except:
                print('Ocoreu um erro ao receber  sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_mimimo,self.valor_maximo))

    
simulador = SimuladorDeDado()
simulador.Iniciar()
