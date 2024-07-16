import PySimpleGUI as sg
import random

Layoyt= [
[sg.Text("vamos ver se consegue adivinhar o numero q estou pensando entre 1 e 50. ")],
[sg.Text('digite o seu numero :')],
[sg.Input(key='digite o seu numero :')],
[sg.Button('verificar')],
[sg.Text('',key='mensagem')],
]
Window = sg.Window('jogo de adivinhar',layout=Layoyt)
comp=random.randint(1,50)
cont=0
while True:
    cont+=1
    evente,values = Window.read()
    if evente == sg.WIN_CLOSED:
        break
    elif evente== 'verificar':
        verdade=int(values['digite o seu numero :'])
        if comp== verdade:
            Window['mensagem'].update(f'parabens vc conseguiu acertar com {cont} tentativas')
        else:
            sg.Input('')
            if verdade>comp:
                Window['mensagem'].Update('digite um numero menor')
            elif verdade<comp:
                Window['mensagem'].Update('digite um numero maior')

                
    