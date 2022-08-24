
#CUSTOMIZAÇÃO DE CAMPO

# Altera o tamanho da letra, butão, campo de escrita

import PySimpleGUI as sg

class TelaPython:
    def __init__(self):

        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0))],       # size(5,0)-> vai ocupar 5 letras naquela linha, O size no "input" é o tamanho do espaço para digitação
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0))],      
            [sg.Button('Enviar Dados')]         #row 3
        ]

        # Janela
        janela = sg.Window("Dados do Usuário").layout(layout) 
        
        # Extrair os dados da tela
        self.button, self.values = janela.Read() 

    
    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()
