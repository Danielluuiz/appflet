import flet as ft

def main(page: ft.Page):
    page.title = "Pedido de Namoro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Função de resposta ao pedido
    def on_accept(e):
        page.clean()  # Limpa a página
        page.add(ft.Text("🎉 Já que concordou agora já era, só casando ❤️", size=30, color="green"))

    def on_decline(e):
        page.clean()  # Limpa a página
        page.add(ft.Text("😢 Que pena, você recusou. Pena que não tem outra opção", size=30, color="red"))

    # Texto do pedido
    text = ft.Text("Já podemos casar Júllia? ❤️", size=30, color="blue", weight=ft.FontWeight.BOLD)

    # Botões de Aceitar e Recusar
    accept_button = ft.ElevatedButton("Aceitar", on_click=on_accept, bgcolor="green", color="white")
    decline_button = ft.ElevatedButton("Recusar", on_click=on_decline, bgcolor="red", color="white")

    # Adiciona os elementos na página
    page.add(
        text,
        ft.Row([accept_button, decline_button], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main, view=ft.WebView)  # Certificação para rodar no navegador
