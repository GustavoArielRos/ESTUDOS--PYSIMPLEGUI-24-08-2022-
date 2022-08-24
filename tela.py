import PySimpleGUI as sg

# Para contruir uma tela:
#   1- Layout
#   2- Janela
#   3- Extrair os dados da tela

class TelaPython:
    def __init__(self):
        
        # Layout
        layout = [
            [sg.Text('Nome'),sg.Input()],       #row 1
            [sg.Text('Idade'),sg.Input()],      #row 2
            [sg.Button('Enviar Dados')]         #row 3
        ]

        # Janela
        janela = sg.Window("Dados do Usuário").layout(layout) # Nome da Janela e pegando o layout criado acima
        
        # Extrair os dados da tela
        self.button, self.values = janela.Read() # Transferindos as informações da janela para esses atributos

    
    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()




