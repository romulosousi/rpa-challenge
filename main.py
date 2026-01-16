from fill_form import fill_form_from_excel
if __name__ == "__main__":
    URL_DO_ARQUIVO_EXCEL = "https://www.rpachallenge.com/assets/downloadFiles/challenge.xlsx"
    URL_DO_FORMULARIO_WEB = "https://www.rpachallenge.com/"

    fill_form_from_excel(URL_DO_ARQUIVO_EXCEL, URL_DO_FORMULARIO_WEB)