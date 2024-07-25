#titulo hashzap
import flet as ft
def main(pagina):
    chat=ft.Column()
    
    def enviar_mensagem_tunel(mensagem):# função para criar o tunel de comunicação para as mensagens serem enviadas para todo usuario simutaneamente.
        campo_conversa=ft.Text(mensagem)
        chat.controls.append(campo_conversa)
        pagina.update()
    def enviar_mensagem(evento):
        nome_usuario=campo_de_usuario.value
        mensagem_usuario=campo_mensagem.value
        mensagem = f"{nome_usuario}: {mensagem_usuario}"
        pagina.pubsub.send_all(mensagem)#comando para colocar a mensagem acima no chat global
        campo_mensagem.value=""
        pagina.update()
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open=False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem=f"{campo_de_usuario.value}: entrou no chat."
        pagina.pubsub.send_all(mensagem)#comando para colocar o nome da pessoa q entrou no chat global.
        pagina.update()
    def iniciar_chat(evento):  #popup (janela na frente da tela)
        pagina.dialog= janela
        janela.open = True
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel) #comando para colocar a função do tunel para aparecer para todos os usuarios.
    titulo_janela=ft.Text('bem vindo ao chat')
    campo_de_usuario= ft.TextField(label="escreva seu nome no chat",on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("entrar no chat",on_click=entrar_chat)
    janela=ft.AlertDialog(title=titulo_janela,content=campo_de_usuario,actions=[botao_entrar])
    titulo=ft.text("aperte o botão para iniciar o chat")
    pagina.add(titulo)
    botao_iniciar = ft.ElevatedButton('iniciar chat',on_click=iniciar_chat)
    pagina.add(botao_iniciar)
    campo_mensagem=ft.TextField(label="digite sua mensagem",on_submit=enviar_mensagem)
    botao_enviar=ft.ElevatedButton('enviar',on_click=enviar_mensagem)
    linha_mensagem=ft.Row([campo_mensagem,botao_enviar])

ft.app(main,view=ft.WEB_BROWSER)