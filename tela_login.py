
import PySimpleGUI as sg
Layout=[
        [sg.Text('usuario')],
        [sg.Input(key='usuario')],
        [sg.Text('senha')],
        [sg.Input(key='senha')],
        [sg.Button('login')],
        [sg.Text('',key='mensagem')],
        ]
window = sg.Window('login',layout=Layout)
while True:
    event, Values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta='123456'
        usuario_correto='sherlon'
        usuario = Values['usuario']
        senha = Values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('olá {} o seu login foi feito com sucesso! '.format(usuario_correto))
        else:
            window['mensagem'].update('senha ou usuario incorreto.')