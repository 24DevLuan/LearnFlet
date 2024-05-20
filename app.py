import flet as ft

#Função que cria a página inical do do nosso aplicativo.
def main(page: ft.Page):

    def cadastrar(e):
        lista = [1000, "Luan"]
        porcentagem = int(txt_porcentagem.value)
        calculo = porcentagem + lista[0]
        resultado = calculo

        print(resultado)

    #Paramêtro que cria o título do aplicativo.
    page.title = "Cadastro APP"
    
    #Paramêtro que cria uma linha de texto na tela do aplicativo.
    txt_titulo = ft.Text('Relatório :', size=30)
    #Paramêtro que cria uma caixa de txt que captura o nome do usuário.
    txt_nome = ft.TextField(label = "Informe o nome do usuário:")
    #Paramêtro que cria uma caixa de txt que captura o lucro percentual mensal.
    txt_porcentagem = ft.TextField(label = "Informe a porcentagem aplicada a carteira:")
    #Paramêtro que cria uma caixa de txt que captura o valor retirado pelo cliente.
    txt_retirada = ft.TextField(label = "Informe o valor que o cliente deseja retirar:")

    btn_captura = ft.ElevatedButton('Gerar', on_click=cadastrar)

    page.add(
        txt_titulo,
        txt_nome,
        txt_porcentagem,
        txt_retirada,
        btn_captura
    )

# Executa o aplicativo

ft.app(target=main)