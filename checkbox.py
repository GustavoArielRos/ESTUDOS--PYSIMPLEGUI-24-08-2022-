
#CHECKBOX 

#Checkbox -> aquele quadradinho de marcar com 'x'


import PySimpleGUI as sg

class TelaPython:
    def __init__(self):

        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0))],      
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0))],
            [sg.Text('Quais provedores de e-mail são aceitos?')],      
            [sg.Checkbox('Gmail'),sg.Checkbox('Outlook'),sg.Checkbox('Yahoo')],
            [sg.Button('Enviar Dados')]         
        ]

        # Janela
        janela = sg.Window("Dados do Usuário").layout(layout) 
        
        # Extrair os dados da tela
        self.button, self.values = janela.Read() 

    
    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()