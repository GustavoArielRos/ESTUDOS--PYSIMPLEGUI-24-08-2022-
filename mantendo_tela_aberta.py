# MANTENDO TELA ABERTA

# É necessário fazer um loop
# É necessário colocar a "janela" no escopo do "self" (meio que tu colocar a janela para ser acessada em todo o escopo que tenha "self")

import PySimpleGUI as sg

class TelaPython:
    def __init__(self):

        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],      
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key = 'idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],      
            [sg.Checkbox('Gmail',key = 'gmail'),sg.Checkbox('Outlook', key = 'outlook'),sg.Checkbox('Yahoo', key = 'yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartoes',key = 'aceitaCartao'),sg.Radio('Não','cartoes',key = 'naoAceitaCartao')],
            [sg.Button('Enviar Dados')]         
        ]

        # Janela(colocando o self)
        self.janela = sg.Window("Dados do Usuário").layout(layout) 
        
        # Extrair os dados da tela(essa informação que era lida uma vez só agora vai para dentro do loop)
        #self.button, self.values = janela.Read() 

    # Criando o loop aqui
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read() 
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartão_sim = self.values['aceitaCartao']
            nao_aceita_cartão= self.values['naoAceitaCartao']

            print(f'nome: {nome}') 
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita cartão:{aceita_cartão_sim}')
            print(f'não aceita cartão:{nao_aceita_cartão}')
         
        
        

tela = TelaPython()
tela.Iniciar()