import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    result = ft.Text(value="0", size=40)

    def button_click(e):
        if e.control.data == "C":
            result.value = "0"
        elif e.control.data == "=":
            try:
                result.value = str(eval(result.value))
            except:
                result.value = "Error"
        else:
            if result.value == "0" or result.value == "Error":
                result.value = e.control.data
            else:
                result.value += e.control.data
        page.update()

    def btn(text):
        return ft.ElevatedButton(text, on_click=button_click, data=text, width=70, height=70)

    page.add(
        result,
        ft.Row([btn("7"), btn("8"), btn("9"), btn("/")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn("4"), btn("5"), btn("6"), btn("*")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn("1"), btn("2"), btn("3"), btn("-")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn("C"), btn("0"), btn("="), btn("+")], alignment=ft.MainAxisAlignment.CENTER),
    )

ft.app(target=main)
