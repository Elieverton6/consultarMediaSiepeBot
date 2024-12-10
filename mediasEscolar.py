from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import time

def configuration():
    # Configurações do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Desabilita a visualização do navegador após a iniciar o script.
    chrome_options.add_argument("--disable-gpu") # Desabilita a aceleração por GPU.
    chrome_options.add_argument("--no-sandbox") # Desativa o modo "sandbox" (segurança) do navegador.
    chrome_options.add_argument("--log-level=3")  # Minimiza logs do ChromeDriver
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Remove mensagens DevTools

    # Configuração do ChromeDriver para desativar logs
    chrome_driver_path = r"c:\chromedriver\chromedriver.exe"
    service = Service(chrome_driver_path, log_path="NUL")  # Suprime logs do Selenium

    # Criação do driver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1366, 1080)
    driver.get("https://www.siepe.educacao.pe.gov.br/")

    return driver

def account_siepe():
    # Suas credenciais pra acessar a conta
    print("Digite suas credenciais do SIEPE abaixo.")
    # inputLogin = input("Seu Login: ") # Seu Login
    # inputPassword = input("Sua Senha: ") # Sua Senha
    inputLogin = input("Login: ") # Seu Login
    inputPassword = input("Senha: ") # Sua Senha

    return inputLogin, inputPassword

def generating_pdf(medias, primeiroNomeEstudante, somaPercentualFalta, resultado_final_biologia,
    resultado_final_fisica, resultado_final_geografia, resultado_final_historia, resultado_final_ingles,
    resultado_final_portugues, resultado_final_matematica, resultado_final_quimica):

    print("Aguarde, estamos gerando seu PDF com suas notas...")

    pdfAluno = canvas.Canvas(f"Medias_{primeiroNomeEstudante}.pdf", pagesize=A4)
    pdfAluno.drawString(30, 800, "Escola: Erundina Negreiros de Arújo")
    pdfAluno.drawString(30, 780, f"Estudante: {primeiroNomeEstudante}")
    pdfAluno.drawString(30, 760, "Confira suas notas:")

    # Biologia
    pdfAluno.drawString(30, 730, "Biologia:")

    # 1 Bimestre
    if not isinstance(medias["Biologia"]["1Bimestre"], int):
        pdfAluno.drawString(40, 710, f"1° Bimestre: {medias["Biologia"]["1Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 710, f"1° Bimestre: {medias["Biologia"]["1Bimestre"]}")
        
    # 2 Bimestre
    if not isinstance(medias["Biologia"]["2Bimestre"], int):
        pdfAluno.drawString(40, 690, f"2° Bimestre: {medias["Biologia"]["2Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 690, f"2° Bimestre: {medias["Biologia"]["2Bimestre"]}")

    # 3 Bimestre
    if not isinstance(medias["Biologia"]["3Bimestre"], int):
        pdfAluno.drawString(40, 670, f"3° Bimestre: {medias["Biologia"]["3Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 670, f"3° Bimestre: {medias["Biologia"]["3Bimestre"]}")

    # 4 Bimestre
    if not isinstance(medias["Biologia"]["4Bimestre"], int):
        pdfAluno.drawString(40, 650, f"4° Bimestre: {medias["Biologia"]["4Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 650, f"4° Bimestre: {medias["Biologia"]["4Bimestre"]}")

    pdfAluno.drawString(40, 630, f"Média Anual: {medias["Biologia"]["mediaAnual"]}")
    pdfAluno.drawString(40, 610, f"Resultado Final: {resultado_final_biologia["resultado"]}")

    # Fisica
    pdfAluno.drawString(30, 580, "Física:")

    # 1 Bimestre
    if not isinstance(medias["Fisica"]["1Bimestre"], int):
        pdfAluno.drawString(40, 560, f"1° Bimestre: {medias["Fisica"]["1Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 560, f"1° Bimestre: {medias["Fisica"]["1Bimestre"]}")

    # 2 Bimestre
    if not isinstance(medias["Fisica"]["2Bimestre"], int):
        pdfAluno.drawString(40, 540, f"2° Bimestre: {medias["Fisica"]["2Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 540, f"2° Bimestre: {medias["Fisica"]["2Bimestre"]}")

    # 3 Bimestre
    if not isinstance(medias["Fisica"]["3Bimestre"], int):
        pdfAluno.drawString(40, 520, f"3° Bimestre: {medias["Fisica"]["3Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 520, f"3° Bimestre: {medias["Fisica"]["3Bimestre"]}")

    # 4 Bimestre
    if not isinstance(medias["Fisica"]["4Bimestre"], int):
        pdfAluno.drawString(40, 500, f"4° Bimestre: {medias["Fisica"]["4Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 500, f"4° Bimestre: {medias["Fisica"]["4Bimestre"]}")
        
    pdfAluno.drawString(40, 480, f"Média Anual: {medias["Fisica"]["mediaAnual"]}")
    pdfAluno.drawString(40, 460, f"Resultado Final: {resultado_final_fisica["resultado"]}")

    # Geografia
    pdfAluno.drawString(30, 430, "Geografia:")

    # 1 Bimestre
    if not isinstance(medias["Geografia"]["1Bimestre"], int):
        pdfAluno.drawString(40, 410, f"1° Bimestre: {medias["Geografia"]["1Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 410, f"1° Bimestre: {medias["Geografia"]["1Bimestre"]}")

    # 2 Bimestre
    if not isinstance(medias["Geografia"]["2Bimestre"], int):
        pdfAluno.drawString(40, 390, f"2° Bimestre: {medias["Geografia"]["2Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 390, f"2° Bimestre: {medias["Geografia"]["2Bimestre"]}")

    # 3 Bimestre
    if not isinstance(medias["Geografia"]["3Bimestre"], int):
        pdfAluno.drawString(40, 370, f"3° Bimestre: {medias["Geografia"]["3Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 370, f"3° Bimestre: {medias["Geografia"]["3Bimestre"]}")

    # 4 Bimestre
    if not isinstance(medias["Geografia"]["4Bimestre"], int):
        pdfAluno.drawString(40, 350, f"4° Bimestre: {medias["Geografia"]["4Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 350, f"4° Bimestre: {medias["Geografia"]["4Bimestre"]}")

    pdfAluno.drawString(40, 330, f"Média Anual: {medias["Geografia"]["mediaAnual"]}")
    pdfAluno.drawString(40, 310, f"Resultado Final: {resultado_final_geografia["resultado"]}")

    # Historia
    pdfAluno.drawString(30, 280, "História:")

    # 1 Bimestre
    if not isinstance(medias["Historia"]["1Bimestre"], int):
        pdfAluno.drawString(40, 260, f"1° Bimestre: {medias["Historia"]["1Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 260, f"1° Bimestre: {medias["Historia"]["1Bimestre"]}")

    # 2 Bimestre
    if not isinstance(medias["Historia"]["2Bimestre"], int):
        pdfAluno.drawString(40, 240, f"2° Bimestre: {medias["Historia"]["2Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 240, f"2° Bimestre: {medias["Historia"]["2Bimestre"]}")

    # 3 Bimestre
    if not isinstance(medias["Historia"]["3Bimestre"], int):
        pdfAluno.drawString(40, 220, f"3° Bimestre: {medias["Historia"]["3Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 220, f"3° Bimestre: {medias["Historia"]["3Bimestre"]}")

    # 4 Bimestre
    if not isinstance(medias["Historia"]["4Bimestre"], int):
        pdfAluno.drawString(40, 200, f"4° Bimestre: {medias["Historia"]["4Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 200, f"4° Bimestre: {medias["Historia"]["4Bimestre"]}")
        
    pdfAluno.drawString(40, 180, f"Média Anual: {medias["Historia"]["mediaAnual"]}")
    pdfAluno.drawString(40, 160, f"Resultado Final: {resultado_final_historia["resultado"]}")

    # Inglês
    pdfAluno.drawString(30, 130, "Inglês:")

    # 1 Bimestre
    if not isinstance(medias["Ingles"]["1Bimestre"], int):
        pdfAluno.drawString(40, 110, f"1° Bimestre: {medias["Ingles"]["1Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 110, f"1° Bimestre: {medias["Ingles"]["1Bimestre"]}")

    # 2 Bimestre
    if not isinstance(medias["Ingles"]["2Bimestre"], int):
        pdfAluno.drawString(40, 90, f"2° Bimestre: {medias["Ingles"]["2Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 90, f"2° Bimestre: {medias["Ingles"]["2Bimestre"]}")

    # 3 Bimestre
    if not isinstance(medias["Ingles"]["3Bimestre"], int):
        pdfAluno.drawString(40, 70, f"3° Bimestre: {medias["Ingles"]["3Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 70, f"3° Bimestre: {medias["Ingles"]["3Bimestre"]}")

    # 4 Bimestre
    if not isinstance(medias["Ingles"]["4Bimestre"], int):
        pdfAluno.drawString(40, 50, f"4° Bimestre: {medias["Ingles"]["4Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 50, f"4° Bimestre: {medias["Ingles"]["4Bimestre"]}")

    pdfAluno.showPage()
    pdfAluno.drawString(40, 800, f"Média Anual: {medias["Ingles"]["mediaAnual"]}")
    pdfAluno.drawString(40, 780, f"Resultado Final: {resultado_final_historia["resultado"]}")

    # # Portugues
    pdfAluno.drawString(30, 750, "Português:")

    # 1 Bimestre
    if not isinstance(medias["Portugues"]["1Bimestre"], int):
        pdfAluno.drawString(40, 730, f"1° Bimestre: {medias["Portugues"]["1Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 730, f"1° Bimestre: {medias["Portugues"]["1Bimestre"]}")

    # 2 Bimestre
    if not isinstance(medias["Portugues"]["2Bimestre"], int):
        pdfAluno.drawString(40, 710, f"2° Bimestre: {medias["Portugues"]["2Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 710, f"2° Bimestre: {medias["Portugues"]["2Bimestre"]}")

    # 3 Bimestre
    if not isinstance(medias["Portugues"]["3Bimestre"], int):
        pdfAluno.drawString(40, 690, f"3° Bimestre: {medias["Portugues"]["3Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 690, f"3° Bimestre: {medias["Portugues"]["3Bimestre"]}")

    # 4 Bimestre
    if not isinstance(medias["Portugues"]["4Bimestre"], int):
        pdfAluno.drawString(40, 670, f"4° Bimestre: {medias["Portugues"]["4Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 670, f"4° Bimestre: {medias["Portugues"]["4Bimestre"]}")

    pdfAluno.drawString(40, 650, f"Média Anual: {medias["Portugues"]["mediaAnual"]}")
    pdfAluno.drawString(40, 630, f"Resultado Final: {resultado_final_portugues["resultado"]}")
    
    # Matematica
    pdfAluno.drawString(30, 600, "Matemática:")

    # 1 Bimestre
    if not isinstance(medias["Matematica"]["1Bimestre"], int):
        pdfAluno.drawString(40, 580, f"1° Bimestre: {medias["Matematica"]["1Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 580, f"1° Bimestre: {medias["Matematica"]["1Bimestre"]}")

    # 2 Bimestre
    if not isinstance(medias["Matematica"]["2Bimestre"], int):
        pdfAluno.drawString(40, 560, f"2° Bimestre: {medias["Matematica"]["2Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 560, f"2° Bimestre: {medias["Matematica"]["2Bimestre"]}")

    # 3 Bimestre
    if not isinstance(medias["Matematica"]["3Bimestre"], int):
        pdfAluno.drawString(40, 540, f"3° Bimestre: {medias["Matematica"]["3Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 540, f"3° Bimestre: {medias["Matematica"]["3Bimestre"]}")

    # 4 Bimestre
    if not isinstance(medias["Matematica"]["4Bimestre"], int):
        pdfAluno.drawString(40, 520, f"4° Bimestre: {medias["Matematica"]["4Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 520, f"4° Bimestre: {medias["Matematica"]["4Bimestre"]}")

    pdfAluno.drawString(40, 500, f"Média Anual: {medias["Matematica"]["mediaAnual"]}")
    pdfAluno.drawString(40, 480, f"Resultado Final: {resultado_final_matematica["resultado"]}")

    # Quimica
    pdfAluno.drawString(30, 450, "Quimica:")

    # 1 Bimestre
    if not isinstance(medias["Quimica"]["1Bimestre"], int):
        pdfAluno.drawString(40, 430, f"1° Bimestre: {medias["Quimica"]["1Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 430, f"1° Bimestre: {medias["Quimica"]["1Bimestre"]}")

    # 2 Bimestre
    if not isinstance(medias["Quimica"]["2Bimestre"], int):
        pdfAluno.drawString(40, 410, f"2° Bimestre: {medias["Quimica"]["2Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 410, f"2° Bimestre: {medias["Quimica"]["2Bimestre"]}")

    # 3 Bimestre
    if not isinstance(medias["Quimica"]["3Bimestre"], int):
        pdfAluno.drawString(40, 390, f"3° Bimestre: {medias["Quimica"]["3Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 390, f"3° Bimestre: {medias["Quimica"]["3Bimestre"]}")

    # 4 Bimestre
    if not isinstance(medias["Quimica"]["4Bimestre"], int):
        pdfAluno.drawString(40, 370, f"4° Bimestre: {medias["Quimica"]["4Bimestre"].replace(".", ",")}")
    else:
        pdfAluno.drawString(40, 370, f"4° Bimestre: {medias["Quimica"]["4Bimestre"]}")

    pdfAluno.drawString(40, 350, f"Média Anual: {medias["Quimica"]["mediaAnual"]}")
    pdfAluno.drawString(40, 330, f"Resultado Final: {resultado_final_quimica["resultado"]}")

    # Percentual de Faltas
    pdfAluno.drawString(40, 300, f"Percentual total de faltas no ano: {str(somaPercentualFalta)[0:5].replace(".", ",")}" + "%")
    pdfAluno.save()
    print("PDF das suas notas gerado com sucesso!")

def structure():
    try:
        # Obtendo o driver configurado
        driver = configuration()

        login, password = account_siepe()

        # Espera ate que o elemento de Login esteja presente na pagina e seleciona ele
        elementLogin = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/form/div[1]/input[1]"))
        )

        elementLogin.send_keys(login) # Insere o texto no campo de Login

        # Espera ate que o elemento de Senha esteja presente na pagina e seleciona ele
        elementSenha = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/form/div[1]/input[2]"))
        )

        elementSenha.send_keys(password) # Insere o texto no campo de Senha

        # Espera ate que o elemento de Botão esteja presente na pagina
        btnEntrar = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/form/div[1]/button/span"))
        )

        # Clica no elemento de botão
        btnEntrar.click()

        elementRememberMeModalEnem = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div/a"))
        )

        # Clica no elemento de botão
        elementRememberMeModalEnem.click()

        # Espera ate que o elemento PegarNomeEstudante esteja presente na pagina e seleciona ele
        elementPegarNomeEstudante = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header/div/div[2]/form/div/strong"))
        )

        nomeEstudanteCompleto = elementPegarNomeEstudante.text
        primeiroNomeEstudante = nomeEstudanteCompleto.split()[0] # Me retorna somente o primeiro nome.
        primeiroNomeEstudante = primeiroNomeEstudante.capitalize() # Primeira letra do nome maiuscula
        print("\nOlá " + primeiroNomeEstudante + ", confira suas notas: \n")


        # Espera ate que o elemento de Boletim esteja presente na pagina e seleciona ele
        elementCategoriaBoletim = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/div/div[2]/div/form/div/a"))
        )

        # Clica no elemento de Boletim
        elementCategoriaBoletim.click()

        # Espera ate que o elemento BoletimVisualizer esteja presente na pagina e seleciona ele
        elementBoletimVisualizar = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/form/div/div/ul/li/a"))
        )

        # Clica no elemento de Boletim
        elementBoletimVisualizar.click()

        # Espera ate que o elemento openBoletim esteja presente na pagina e seleciona ele
        elementAbrirBoletim = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/form/div/div/ul/li/ul/li[1]/a"))
        )

        # Clica no elemento de Boletim
        elementAbrirBoletim.click()

        # Espera até que a nova janela seja aberta
        nova_janela = WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))

        # Mude para a nova janela
        janelas = driver.window_handles
        driver.switch_to.window(janelas[1])

        # Pegando as médias de Biologia
        elementMedia1BimestreBiologia = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[2]/td[2]"))
        )
        elementMedia2BimestreBiologia = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[2]/td[5]"))
        )
        elementMedia3BimestreBiologia = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[2]/td[8]"))
        )
        elementMedia4BimestreBiologia = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[2]/td[11]"))
        )
        textMedia1BimestreBiologia = elementMedia1BimestreBiologia.text
        textMedia2BimestreBiologia = elementMedia2BimestreBiologia.text
        textMedia3BimestreBiologia = elementMedia3BimestreBiologia.text
        textMedia4BimestreBiologia = elementMedia4BimestreBiologia.text
        notMedia4BimestreBiologia = False

        print("Matéria: Biologia")
        print("1º Bimestre:", textMedia1BimestreBiologia)
        if (textMedia1BimestreBiologia == "-"):
            textMedia1BimestreBiologia = 0
        print("2º Bimestre:", textMedia2BimestreBiologia)
        if (textMedia2BimestreBiologia == "-"):
            textMedia2BimestreBiologia = 0
        print("3º Bimestre:", textMedia3BimestreBiologia)
        if (textMedia3BimestreBiologia == "-"):
            textMedia3BimestreBiologia = 0
        print("4º Bimestre:", textMedia4BimestreBiologia)
        if (textMedia4BimestreBiologia == "-"):
            textMedia4BimestreBiologia = 0
            notMedia4BimestreFisica = True

        if not isinstance(textMedia1BimestreBiologia, int):
            textMedia1BimestreBiologia = textMedia1BimestreBiologia.replace(",", ".")

        if not isinstance(textMedia2BimestreBiologia, int):
            textMedia2BimestreBiologia = textMedia2BimestreBiologia.replace(",", ".")
        
        if not isinstance(textMedia3BimestreBiologia, int):
            textMedia3BimestreBiologia = textMedia3BimestreBiologia.replace(",", ".")

        if not isinstance(textMedia4BimestreBiologia, int):
            textMedia4BimestreBiologia = textMedia4BimestreBiologia.replace(",", ".")

        textMediaBiologia = (float(textMedia1BimestreBiologia) + float(textMedia2BimestreBiologia) + (float(textMedia3BimestreBiologia) + float(textMedia4BimestreBiologia))) / 4

        if (textMediaBiologia >= 0.1 and textMediaBiologia <= 0.4):
            textMediaBiologia = 0.5
        elif (textMediaBiologia >= 0.6 and textMediaBiologia <= 0.9):
            textMediaBiologia = 1.0
        elif (textMediaBiologia >= 1.1 and textMediaBiologia <= 1.4):
            textMediaBiologia = 1.5
        elif (textMediaBiologia >= 1.6 and textMediaBiologia <= 1.9):
            textMediaBiologia = 2.0
        elif (textMediaBiologia >= 2.1 and textMediaBiologia <= 2.4):
            textMediaBiologia = 2.5
        elif (textMediaBiologia >= 2.6 and textMediaBiologia <= 2.9):
            textMediaBiologia = 3.0
        elif (textMediaBiologia >= 3.1 and textMediaBiologia <= 3.4):
            textMediaBiologia = 3.5
        elif (textMediaBiologia >= 3.6 and textMediaBiologia <= 3.9):
            textMediaBiologia = 4.0
        elif (textMediaBiologia >= 4.1 and textMediaBiologia <= 4.4):
            textMediaBiologia = 4.5
        elif (textMediaBiologia >= 4.6 and textMediaBiologia <= 4.9):
            textMediaBiologia = 5.0
        elif (textMediaBiologia >= 5.1 and textMediaBiologia <= 5.4):
            textMediaBiologia = 5.5
        elif (textMediaBiologia >= 5.6 and textMediaBiologia <= 5.9):
            textMediaBiologia = 6.0
        elif (textMediaBiologia >= 6.1 and textMediaBiologia <= 6.4):
            textMediaBiologia = 6.5
        elif (textMediaBiologia >= 6.6 and textMediaBiologia <= 6.9):
            textMediaBiologia = 7.0
        elif (textMediaBiologia >= 7.1 and textMediaBiologia <= 7.4):
            textMediaBiologia = 7.5
        elif (textMediaBiologia >= 7.6 and textMediaBiologia <= 7.9):
            textMediaBiologia = 8.0
        elif (textMediaBiologia >= 8.1 and textMediaBiologia <= 8.4):
            textMediaBiologia = 8.5
        elif (textMediaBiologia >= 8.6 and textMediaBiologia <= 8.9):
            textMediaBiologia = 9.0
        elif (textMediaBiologia >= 9.1 and textMediaBiologia <= 9.4):
            textMediaBiologia = 9.5
        elif (textMediaBiologia >= 9.6 and textMediaBiologia <= 9.9):
            textMediaBiologia = 10.0

        resultadoTextMediaBiologia = str(textMediaBiologia).replace(".", ",")
        print("Média:", resultadoTextMediaBiologia[0:4])

        resultadoAprovacaoTextMediaBiologia = float(resultadoTextMediaBiologia.replace(",", "."))

        resultado_final_biologia = {}

        if (notMedia4BimestreBiologia is True) and (resultadoAprovacaoTextMediaBiologia < 6.0):
            resultado_final = "Falta nota para conclusão."
            print(f"Resultado Final: {resultado_final} 😬")

            resultado_final_biologia = {
                "nota_faltando": True,
                "resultado": resultado_final
            }
        elif (notMedia4BimestreBiologia is True) and (resultadoAprovacaoTextMediaBiologia >= 6.0):
            resultado_final = "Aprovado com antecedência!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_biologia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        elif (resultadoAprovacaoTextMediaBiologia >= 6.0):
            resultado_final = "Aprovado!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_biologia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        else:
            resultado_final = "Recuperação!"
            print(f"Resultado Final: {resultado_final} 😓")

            resultado_final_biologia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }

        print("\n----------------------------\n")

        # Pegando as médias de Fisica
        elementMedia1BimestreFisica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[2]"))
        )
        elementMedia2BimestreFisica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[5]"))
        )
        elementMedia3BimestreFisica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[8]"))
        )
        elementMedia4BimestreFisica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[11]"))
        )
        textMedia1BimestreFisica = elementMedia1BimestreFisica.text
        textMedia2BimestreFisica = elementMedia2BimestreFisica.text
        textMedia3BimestreFisica = elementMedia3BimestreFisica.text
        textMedia4BimestreFisica = elementMedia4BimestreFisica.text
        notMedia4BimestreFisica = False

        print("Matéria: Fisica")
        print("1º Bimestre:", textMedia1BimestreFisica)
        if (textMedia1BimestreFisica == "-"):
            textMedia1BimestreFisica = 0
        print("2º Bimestre:", textMedia2BimestreFisica)
        if (textMedia2BimestreFisica == "-"):
            textMedia2BimestreFisica = 0
        print("3º Bimestre:", textMedia3BimestreFisica)
        if (textMedia3BimestreFisica == "-"):
            textMedia3BimestreFisica = 0
        print("4º Bimestre:", textMedia4BimestreFisica)
        if (textMedia4BimestreFisica == "-"):
            textMedia4BimestreFisica = 0
            notMedia4BimestreFisica = True

        if not isinstance(textMedia1BimestreFisica, int):
            textMedia1BimestreFisica = textMedia1BimestreFisica.replace(",", ".")

        if not isinstance(textMedia2BimestreFisica, int):
            textMedia2BimestreFisica = textMedia2BimestreFisica.replace(",", ".")
        
        if not isinstance(textMedia3BimestreFisica, int):
            textMedia3BimestreFisica = textMedia3BimestreFisica.replace(",", ".")

        if not isinstance(textMedia4BimestreFisica, int):
            textMedia4BimestreFisica = textMedia4BimestreFisica.replace(",", ".")

        textMediaFisica = (float(textMedia1BimestreFisica) + float(textMedia2BimestreFisica) + (float(textMedia3BimestreFisica) + float(textMedia4BimestreFisica))) / 4

        if (textMediaFisica >= 0.1 and textMediaFisica <= 0.4):
            textMediaFisica = 0.5
        elif (textMediaFisica >= 0.6 and textMediaFisica <= 0.9):
            textMediaFisica = 1.0
        elif (textMediaFisica >= 1.1 and textMediaFisica <= 1.4):
            textMediaFisica = 1.5
        elif (textMediaFisica >= 1.6 and textMediaFisica <= 1.9):
            textMediaFisica = 2.0
        elif (textMediaFisica >= 2.1 and textMediaFisica <= 2.4):
            textMediaFisica = 2.5
        elif (textMediaFisica >= 2.6 and textMediaFisica <= 2.9):
            textMediaFisica = 3.0
        elif (textMediaFisica >= 3.1 and textMediaFisica <= 3.4):
            textMediaFisica = 3.5
        elif (textMediaFisica >= 3.6 and textMediaFisica <= 3.9):
            textMediaFisica = 4.0
        elif (textMediaFisica >= 4.1 and textMediaFisica <= 4.4):
            textMediaFisica = 4.5
        elif (textMediaFisica >= 4.6 and textMediaFisica <= 4.9):
            textMediaFisica = 5.0
        elif (textMediaFisica >= 5.1 and textMediaFisica <= 5.4):
            textMediaFisica = 5.5
        elif (textMediaFisica >= 5.6 and textMediaFisica <= 5.9):
            textMediaFisica = 6.0
        elif (textMediaFisica >= 6.1 and textMediaFisica <= 6.4):
            textMediaFisica = 6.5
        elif (textMediaFisica >= 6.6 and textMediaFisica <= 6.9):
            textMediaFisica = 7.0
        elif (textMediaFisica >= 7.1 and textMediaFisica <= 7.4):
            textMediaFisica = 7.5
        elif (textMediaFisica >= 7.6 and textMediaFisica <= 7.9):
            textMediaFisica = 8.0
        elif (textMediaFisica >= 8.1 and textMediaFisica <= 8.4):
            textMediaFisica = 8.5
        elif (textMediaFisica >= 8.6 and textMediaFisica <= 8.9):
            textMediaFisica = 9.0
        elif (textMediaFisica >= 9.1 and textMediaFisica <= 9.4):
            textMediaFisica = 9.5
        elif (textMediaFisica >= 9.6 and textMediaFisica <= 9.9):
            textMediaFisica = 10.0

        resultadoTextMediaFisica = str(textMediaFisica).replace(".", ",")
        print("Média:", resultadoTextMediaFisica[0:4])

        resultadoAprovacaoTextMediaFisica = float(resultadoTextMediaFisica.replace(",", "."))
        resultado_final_fisica = {}

        if (notMedia4BimestreFisica is True) and (resultadoAprovacaoTextMediaFisica < 6.0):
            resultado_final = "Falta nota para conclusão."
            print(f"Resultado Final: {resultado_final} 😬")

            resultado_final_fisica = {
                "nota_faltando": True,
                "resultado": resultado_final
            }
        elif (notMedia4BimestreFisica is True) and (resultadoAprovacaoTextMediaFisica >= 6.0):
            resultado_final = "Aprovado com antecedência!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_fisica = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        elif (resultadoAprovacaoTextMediaFisica >= 6.0):
            resultado_final = "Aprovado!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_fisica = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        else:
            resultado_final = "Recuperação!"
            print(f"Resultado Final: {resultado_final} 😓")

            resultado_final_fisica = {
                "nota_faltando": False,
                "resultado": resultado_final
            }

        print("\n---------------------------- \n")

        # Pegando as médias de Geografia
        elementMedia1BimestreGeografia = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[4]/td[2]"))
        )
        elementMedia2BimestreGeografia = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[4]/td[5]"))
        )
        elementMedia3BimestreGeografia = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[4]/td[8]"))
        )
        elementMedia4BimestreGeografia = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[4]/td[11]"))
        )
        textMedia1BimestreGeografia = elementMedia1BimestreGeografia.text
        textMedia2BimestreGeografia = elementMedia2BimestreGeografia.text
        textMedia3BimestreGeografia = elementMedia3BimestreGeografia.text
        textMedia4BimestreGeografia = elementMedia4BimestreGeografia.text
        notMedia4BimestreGeografia = False

        print("Matéria: Geografia")
        print("1º Bimestre:", textMedia1BimestreGeografia)
        if (textMedia1BimestreGeografia == "-"):
            textMedia1BimestreGeografia = 0
        print("2º Bimestre:", textMedia2BimestreGeografia)
        if (textMedia2BimestreGeografia == "-"):
            textMedia2BimestreGeografia = 0
        print("3º Bimestre:", textMedia3BimestreGeografia)
        if (textMedia3BimestreGeografia == "-"):
            textMedia3BimestreGeografia = 0
        print("4º Bimestre:", textMedia4BimestreGeografia)
        if (textMedia4BimestreGeografia == "-"):
            textMedia4BimestreGeografia = 0
            notMedia4BimestreGeografia = True

        if not isinstance(textMedia1BimestreGeografia, int):
            textMedia1BimestreGeografia = textMedia1BimestreGeografia.replace(",", ".")

        if not isinstance(textMedia2BimestreGeografia, int):
            textMedia2BimestreGeografia = textMedia2BimestreGeografia.replace(",", ".")
        
        if not isinstance(textMedia3BimestreGeografia, int):
            textMedia3BimestreGeografia = textMedia3BimestreGeografia.replace(",", ".")

        if not isinstance(textMedia4BimestreGeografia, int):
            textMedia4BimestreGeografia = textMedia4BimestreGeografia.replace(",", ".")

        textMediaGeografia = (float(textMedia1BimestreGeografia) + float(textMedia2BimestreGeografia) + (float(textMedia3BimestreGeografia) + float(textMedia4BimestreGeografia))) / 4
    
        if (textMediaGeografia >= 0.1 and textMediaGeografia <= 0.4):
            textMediaGeografia = 0.5
        elif (textMediaGeografia >= 0.6 and textMediaGeografia <= 0.9):
            textMediaGeografia = 1.0
        elif (textMediaGeografia >= 1.1 and textMediaGeografia <= 1.4):
            textMediaGeografia = 1.5
        elif (textMediaGeografia >= 1.6 and textMediaGeografia <= 1.9):
            textMediaGeografia = 2.0
        elif (textMediaGeografia >= 2.1 and textMediaGeografia <= 2.4):
            textMediaGeografia = 2.5
        elif (textMediaGeografia >= 2.6 and textMediaGeografia <= 2.9):
            textMediaGeografia = 3.0
        elif (textMediaGeografia >= 3.1 and textMediaGeografia <= 3.4):
            textMediaGeografia = 3.5
        elif (textMediaGeografia >= 3.6 and textMediaGeografia <= 3.9):
            textMediaGeografia = 4.0
        elif (textMediaGeografia >= 4.1 and textMediaGeografia <= 4.4):
            textMediaGeografia = 4.5
        elif (textMediaGeografia >= 4.6 and textMediaGeografia <= 4.9):
            textMediaGeografia = 5.0
        elif (textMediaGeografia >= 5.1 and textMediaGeografia <= 5.4):
            textMediaGeografia = 5.5
        elif (textMediaGeografia >= 5.6 and textMediaGeografia <= 5.9):
            textMediaGeografia = 6.0
        elif (textMediaGeografia >= 6.1 and textMediaGeografia <= 6.4):
            textMediaGeografia = 6.5
        elif (textMediaGeografia >= 6.6 and textMediaGeografia <= 6.9):
            textMediaGeografia = 7.0
        elif (textMediaGeografia >= 7.1 and textMediaGeografia <= 7.4):
            textMediaGeografia = 7.5
        elif (textMediaGeografia >= 7.6 and textMediaGeografia <= 7.9):
            textMediaGeografia = 8.0
        elif (textMediaGeografia >= 8.1 and textMediaGeografia <= 8.4):
            textMediaGeografia = 8.5
        elif (textMediaGeografia >= 8.6 and textMediaGeografia <= 8.9):
            textMediaGeografia = 9.0
        elif (textMediaGeografia >= 9.1 and textMediaGeografia <= 9.4):
            textMediaGeografia = 9.5
        elif (textMediaGeografia >= 9.6 and textMediaGeografia <= 9.9):
            textMediaGeografia = 10.0
    
        resultadoTextMediaGeografia = str(textMediaGeografia).replace(".", ",")
        print("Média:", resultadoTextMediaGeografia[0:4])

        resultadoAprovacaoTextMediaGeografia = float(resultadoTextMediaGeografia.replace(",", "."))
        resultado_final_geografia = {}

        if (notMedia4BimestreGeografia is True) and (resultadoAprovacaoTextMediaGeografia < 6.0):
            resultado_final = "Falta nota para conclusão."
            print(f"Resultado Final: {resultado_final} 😬")

            resultado_final_geografia = {
                "nota_faltando": True,
                "resultado": resultado_final
            }
        elif (notMedia4BimestreGeografia is True) and (resultadoAprovacaoTextMediaGeografia >= 6.0):
            resultado_final = "Aprovado com antecedência!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_geografia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        elif (resultadoAprovacaoTextMediaGeografia >= 6.0):
            resultado_final = "Aprovado!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_geografia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        else:
            resultado_final = "Recuperação!"
            print(f"Resultado Final: {resultado_final} 😓")

            resultado_final_geografia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }

        print("\n---------------------------- \n")

        # Pegando as média de Historia
        elementMedia1BimestreHistoria = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[5]/td[2]"))
        )
        elementMedia2BimestreHistoria = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[5]/td[5]"))
        )
        elementMedia3BimestreHistoria = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[5]/td[8]"))
        )
        elementMedia4BimestreHistoria = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[5]/td[11]"))
        )
        textMedia1BimestreHistoria = elementMedia1BimestreHistoria.text
        textMedia2BimestreHistoria = elementMedia2BimestreHistoria.text
        textMedia3BimestreHistoria = elementMedia3BimestreHistoria.text
        textMedia4BimestreHistoria = elementMedia4BimestreHistoria.text
        notMedia4BimestreHistoria = False

        print("Máteria: História")
        print("1º Bimestre:", textMedia1BimestreHistoria)
        if (textMedia1BimestreHistoria == "-"):
            textMedia1BimestreHistoria = 0
        print("2º Bimestre:", textMedia2BimestreHistoria)
        if (textMedia2BimestreHistoria == "-"):
            textMedia2BimestreHistoria = 0
        print("3º Bimestre:", textMedia3BimestreHistoria)
        if (textMedia3BimestreHistoria == "-"):
            textMedia3BimestreHistoria = 0
        print("4º Bimestre:", textMedia4BimestreHistoria)
        if (textMedia4BimestreHistoria == "-"):
            textMedia4BimestreHistoria = 0
            notMedia4BimestreHistoria = True

        if not isinstance(textMedia1BimestreHistoria, int):
            textMedia1BimestreHistoria = textMedia1BimestreHistoria.replace(",", ".")

        if not isinstance(textMedia2BimestreHistoria, int):
            textMedia2BimestreHistoria = textMedia2BimestreHistoria.replace(",", ".")
        
        if not isinstance(textMedia3BimestreHistoria, int):
            textMedia3BimestreHistoria = textMedia3BimestreHistoria.replace(",", ".")

        if not isinstance(textMedia4BimestreHistoria, int):
            textMedia4BimestreHistoria = textMedia4BimestreHistoria.replace(",", ".")

        textMediaHistoria = (float(textMedia1BimestreHistoria) + float(textMedia2BimestreHistoria) + (float(textMedia3BimestreHistoria) + float(textMedia4BimestreHistoria))) / 4
        
        if (textMediaHistoria >= 0.1 and textMediaHistoria <= 0.4):
            textMediaHistoria = 0.5
        elif (textMediaHistoria >= 0.6 and textMediaHistoria <= 0.9):
            textMediaHistoria = 1.0
        elif (textMediaHistoria >= 1.1 and textMediaHistoria <= 1.4):
            textMediaHistoria = 1.5
        elif (textMediaHistoria >= 1.6 and textMediaHistoria <= 1.9):
            textMediaHistoria = 2.0
        elif (textMediaHistoria >= 2.1 and textMediaHistoria <= 2.4):
            textMediaHistoria = 2.5
        elif (textMediaHistoria >= 2.6 and textMediaHistoria <= 2.9):
            textMediaHistoria = 3.0
        elif (textMediaHistoria >= 3.1 and textMediaHistoria <= 3.4):
            textMediaHistoria = 3.5
        elif (textMediaHistoria >= 3.6 and textMediaHistoria <= 3.9):
            textMediaHistoria = 4.0
        elif (textMediaHistoria >= 4.1 and textMediaHistoria <= 4.4):
            textMediaHistoria = 4.5
        elif (textMediaHistoria >= 4.6 and textMediaHistoria <= 4.9):
            textMediaHistoria = 5.0
        elif (textMediaHistoria >= 5.1 and textMediaHistoria <= 5.4):
            textMediaHistoria = 5.5
        elif (textMediaHistoria >= 5.6 and textMediaHistoria <= 5.9):
            textMediaHistoria = 6.0
        elif (textMediaHistoria >= 6.1 and textMediaHistoria <= 6.4):
            textMediaHistoria = 6.5
        elif (textMediaHistoria >= 6.6 and textMediaHistoria <= 6.9):
            textMediaHistoria = 7.0
        elif (textMediaHistoria >= 7.1 and textMediaHistoria <= 7.4):
            textMediaHistoria = 7.5
        elif (textMediaHistoria >= 7.6 and textMediaHistoria <= 7.9):
            textMediaHistoria = 8.0
        elif (textMediaHistoria >= 8.1 and textMediaHistoria <= 8.4):
            textMediaHistoria = 8.5
        elif (textMediaHistoria >= 8.6 and textMediaHistoria <= 8.9):
            textMediaHistoria = 9.0
        elif (textMediaHistoria >= 9.1 and textMediaHistoria <= 9.4):
            textMediaHistoria = 9.5
        elif (textMediaHistoria >= 9.6 and textMediaHistoria <= 9.9):
            textMediaHistoria = 10.0

        resultadoTextMediaHistoria = str(textMediaHistoria).replace(".", ",")
        print("Média:", resultadoTextMediaHistoria[0:4])

        resultadoAprovacaoTextMediaHistoria = float(resultadoTextMediaHistoria.replace(",", "."))
        resultado_final_historia = {}

        if (notMedia4BimestreHistoria is True) and (resultadoAprovacaoTextMediaHistoria < 6.0):
            resultado_final = "Falta nota para conclusão."
            print(f"Resultado Final: {resultado_final} 😬")

            resultado_final_historia = {
                "nota_faltando": True,
                "resultado": resultado_final
            }
        elif (notMedia4BimestreHistoria is True) and (resultadoAprovacaoTextMediaHistoria >= 6.0):
            resultado_final = "Aprovado com antecedência!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_historia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        elif (resultadoAprovacaoTextMediaHistoria >= 6.0):
            resultado_final = "Aprovado!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_historia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        else:
            resultado_final = "Recuperação!"
            print(f"Resultado Final: {resultado_final} 😓")

            resultado_final_historia = {
                "nota_faltando": False,
                "resultado": resultado_final
            }

        print("\n---------------------------- \n")

        # Pegando as médias de Ingles
        elementMedia1BimestreIngles = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[6]/td[2]"))
        )
        elementMedia2BimestreIngles = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[6]/td[5]"))
        )
        elementMedia3BimestreIngles = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[6]/td[8]"))
        )
        elementMedia4BimestreIngles = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[6]/td[11]"))
        )
        textMedia1BimestreIngles = elementMedia1BimestreIngles.text
        textMedia2BimestreIngles = elementMedia2BimestreIngles.text
        textMedia3BimestreIngles = elementMedia3BimestreIngles.text
        textMedia4BimestreIngles = elementMedia4BimestreIngles.text
        notMedia4BimestreIngles = False

        print("Matéria: Inglês")
        print("1º Bimestre:", textMedia1BimestreIngles)
        if (textMedia1BimestreIngles == "-"):
            textMedia1BimestreIngles = 0
        print("2º Bimestre:", textMedia2BimestreIngles)
        if (textMedia2BimestreIngles == "-"):
            textMedia2BimestreIngles = 0
        print("3º Bimestre:", textMedia3BimestreIngles)
        if (textMedia3BimestreIngles == "-"):
            textMedia3BimestreIngles = 0
        print("4º Bimestre:", textMedia4BimestreIngles)
        if (textMedia4BimestreIngles == "-"):
            textMedia4BimestreIngles = 0
            notMedia4BimestreIngles = True

        if not isinstance(textMedia1BimestreIngles, int):
            textMedia1BimestreIngles = textMedia1BimestreIngles.replace(",", ".")

        if not isinstance(textMedia2BimestreIngles, int):
            textMedia2BimestreIngles = textMedia2BimestreIngles.replace(",", ".")
        
        if not isinstance(textMedia3BimestreIngles, int):
            textMedia3BimestreIngles = textMedia3BimestreIngles.replace(",", ".")

        if not isinstance(textMedia4BimestreIngles, int):
            textMedia4BimestreIngles = textMedia4BimestreIngles.replace(",", ".")

        textMediaIngles = (float(textMedia1BimestreIngles) + float(textMedia2BimestreIngles) + (float(textMedia3BimestreIngles) + float(textMedia4BimestreIngles))) / 4
        
        if (textMediaIngles >= 0.1 and textMediaIngles <= 0.4):
            textMediaIngles = 0.5
        elif (textMediaIngles >= 0.6 and textMediaIngles <= 0.9):
            textMediaIngles = 1.0
        elif (textMediaIngles >= 1.1 and textMediaIngles <= 1.4):
            textMediaIngles = 1.5
        elif (textMediaIngles >= 1.6 and textMediaIngles <= 1.9):
            textMediaIngles = 2.0
        elif (textMediaIngles >= 2.1 and textMediaIngles <= 2.4):
            textMediaIngles = 2.5
        elif (textMediaIngles >= 2.6 and textMediaIngles <= 2.9):
            textMediaIngles = 3.0
        elif (textMediaIngles >= 3.1 and textMediaIngles <= 3.4):
            textMediaIngles = 3.5
        elif (textMediaIngles >= 3.6 and textMediaIngles <= 3.9):
            textMediaIngles = 4.0
        elif (textMediaIngles >= 4.1 and textMediaIngles <= 4.4):
            textMediaIngles = 4.5
        elif (textMediaIngles >= 4.6 and textMediaIngles <= 4.9):
            textMediaIngles = 5.0
        elif (textMediaIngles >= 5.1 and textMediaIngles <= 5.4):
            textMediaIngles = 5.5
        elif (textMediaIngles >= 5.6 and textMediaIngles <= 5.9):
            textMediaIngles = 6.0
        elif (textMediaIngles >= 6.1 and textMediaIngles <= 6.4):
            textMediaIngles = 6.5
        elif (textMediaIngles >= 6.6 and textMediaIngles <= 6.9):
            textMediaIngles = 7.0
        elif (textMediaIngles >= 7.1 and textMediaIngles <= 7.4):
            textMediaIngles = 7.5
        elif (textMediaIngles >= 7.6 and textMediaIngles <= 7.9):
            textMediaIngles = 8.0
        elif (textMediaIngles >= 8.1 and textMediaIngles <= 8.4):
            textMediaIngles = 8.5
        elif (textMediaIngles >= 8.6 and textMediaIngles <= 8.9):
            textMediaIngles = 9.0
        elif (textMediaIngles >= 9.1 and textMediaIngles <= 9.4):
            textMediaIngles = 9.5
        elif (textMediaIngles >= 9.6 and textMediaIngles <= 9.9):
            textMediaIngles = 10.0
        
        resultadoTextMediaIngles = str(textMediaIngles).replace(".", ",")
        print("Média:", resultadoTextMediaIngles[0:4])

        resultadoAprovacaoTextMediaIngles = float(resultadoTextMediaIngles.replace(",", "."))
        resultado_final_ingles = {}

        if (notMedia4BimestreIngles is True) and (resultadoAprovacaoTextMediaIngles < 6.0):
            resultado_final = "Falta nota para conclusão."
            print(f"Resultado Final: {resultado_final} 😬")

            resultado_final_ingles = {
                "nota_faltando": True,
                "resultado": resultado_final
            }
        elif (notMedia4BimestreIngles is True) and (resultadoAprovacaoTextMediaIngles >= 6.0):
            resultado_final = "Aprovado com antecedência!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_ingles = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        elif (resultadoAprovacaoTextMediaIngles >= 6.0):
            resultado_final = "Aprovado!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_ingles = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        else:
            resultado_final = "Recuperação!"
            print(f"Resultado Final: {resultado_final} 😓")

            resultado_final_ingles = {
                "nota_faltando": False,
                "resultado": resultado_final
            }

        print("\n---------------------------- \n")

        # Pegando as média de Portugues
        elementMedia1BimestrePortugues = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[7]/td[2]"))
        )
        elementMedia2BimestrePortugues = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[7]/td[5]"))
        )
        elementMedia3BimestrePortugues = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[7]/td[8]"))
        )
        elementMedia4BimestrePortugues = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[7]/td[11]"))
        )
        textMedia1BimestrePortugues = elementMedia1BimestrePortugues.text
        textMedia2BimestrePortugues = elementMedia2BimestrePortugues.text
        textMedia3BimestrePortugues = elementMedia3BimestrePortugues.text
        textMedia4BimestrePortugues = elementMedia4BimestrePortugues.text
        notMedia4BimestrePortugues = False

        print("Matéria: Português")
        print("1º Bimestre:", textMedia1BimestrePortugues)
        if (textMedia1BimestrePortugues == "-"):
            textMedia1BimestrePortugues = 0
        print("2º Bimestre:", textMedia2BimestrePortugues)
        if (textMedia2BimestrePortugues == "-"):
            textMedia2BimestrePortugues = 0
        print("3º Bimestre:", textMedia3BimestrePortugues)
        if (textMedia3BimestrePortugues == "-"):
            textMedia3BimestrePortugues = 0
        print("4º Bimestre:", textMedia4BimestrePortugues)
        if (textMedia4BimestrePortugues == "-"):
            textMedia4BimestrePortugues = 0
            notMedia4BimestrePortugues = True

        if not isinstance(textMedia1BimestrePortugues, int):
            textMedia1BimestrePortugues = textMedia1BimestrePortugues.replace(",", ".")

        if not isinstance(textMedia2BimestrePortugues, int):
            textMedia2BimestrePortugues = textMedia2BimestrePortugues.replace(",", ".")
        
        if not isinstance(textMedia3BimestrePortugues, int):
            textMedia3BimestrePortugues = textMedia3BimestrePortugues.replace(",", ".")

        if not isinstance(textMedia4BimestrePortugues, int):
            textMedia4BimestrePortugues = textMedia4BimestrePortugues.replace(",", ".")

        textMediaPortugues = (float(textMedia1BimestrePortugues) + float(textMedia2BimestrePortugues) + (float(textMedia3BimestrePortugues) + float(textMedia4BimestrePortugues))) / 4
        
        if (textMediaPortugues >= 0.1 and textMediaPortugues <= 0.4):
            textMediaPortugues = 0.5
        elif (textMediaPortugues >= 0.6 and textMediaPortugues <= 0.9):
            textMediaPortugues = 1.0
        elif (textMediaPortugues >= 1.1 and textMediaPortugues <= 1.4):
            textMediaPortugues = 1.5
        elif (textMediaPortugues >= 1.6 and textMediaPortugues <= 1.9):
            textMediaPortugues = 2.0
        elif (textMediaPortugues >= 2.1 and textMediaPortugues <= 2.4):
            textMediaPortugues = 2.5
        elif (textMediaPortugues >= 2.6 and textMediaPortugues <= 2.9):
            textMediaPortugues = 3.0
        elif (textMediaPortugues >= 3.1 and textMediaPortugues <= 3.4):
            textMediaPortugues = 3.5
        elif (textMediaPortugues >= 3.6 and textMediaPortugues <= 3.9):
            textMediaPortugues = 4.0
        elif (textMediaPortugues >= 4.1 and textMediaPortugues <= 4.4):
            textMediaPortugues = 4.5
        elif (textMediaPortugues >= 4.6 and textMediaPortugues <= 4.9):
            textMediaPortugues = 5.0
        elif (textMediaPortugues >= 5.1 and textMediaPortugues <= 5.4):
            textMediaPortugues = 5.5
        elif (textMediaPortugues >= 5.6 and textMediaPortugues <= 5.9):
            textMediaPortugues = 6.0
        elif (textMediaPortugues >= 6.1 and textMediaPortugues <= 6.4):
            textMediaPortugues = 6.5
        elif (textMediaPortugues >= 6.6 and textMediaPortugues <= 6.9):
            textMediaPortugues = 7.0
        elif (textMediaPortugues >= 7.1 and textMediaPortugues <= 7.4):
            textMediaPortugues = 7.5
        elif (textMediaPortugues >= 7.6 and textMediaPortugues <= 7.9):
            textMediaPortugues = 8.0
        elif (textMediaPortugues >= 8.1 and textMediaPortugues <= 8.4):
            textMediaPortugues = 8.5
        elif (textMediaPortugues >= 8.6 and textMediaPortugues <= 8.9):
            textMediaPortugues = 9.0
        elif (textMediaPortugues >= 9.1 and textMediaPortugues <= 9.4):
            textMediaPortugues = 9.5
        elif (textMediaPortugues >= 9.6 and textMediaPortugues <= 9.9):
            textMediaPortugues = 10.0

        resultadoTextMediaPortugues = str(textMediaPortugues).replace(".", ",")
        print("Média:", resultadoTextMediaPortugues[0:4])

        resultadoAprovacaoTextMediaPortugues = float(resultadoTextMediaPortugues.replace(",", "."))

        resultado_final_portugues = {}

        if (notMedia4BimestrePortugues is True) and (resultadoAprovacaoTextMediaPortugues < 6.0):
            resultado_final = "Falta nota para conclusão."
            print(f"Resultado Final: {resultado_final} 😬")

            resultado_final_portugues = {
                "nota_faltando": True,
                "resultado": resultado_final
            }
        elif (notMedia4BimestrePortugues is True) and (resultadoAprovacaoTextMediaPortugues >= 6.0):
            resultado_final = "Aprovado com antecedência!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_portugues = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        elif (resultadoAprovacaoTextMediaPortugues >= 6.0):
            resultado_final = "Aprovado!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_portugues = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        else:
            resultado_final = "Recuperação!"
            print(f"Resultado Final: {resultado_final} 😓")

            resultado_final_portugues = {
                "nota_faltando": False,
                "resultado": resultado_final
            }

        print("\n---------------------------- \n")

        # Pegando as média de Matematica
        elementMedia1BimestreMatematica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[8]/td[2]"))
        )
        elementMedia2BimestreMatematica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[8]/td[5]"))
        )
        elementMedia3BimestreMatematica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[8]/td[8]"))
        )
        elementMedia4BimestreMatematica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[8]/td[11]"))
        )
        textMedia1BimestreMatematica = elementMedia1BimestreMatematica.text
        textMedia2BimestreMatematica = elementMedia2BimestreMatematica.text
        textMedia3BimestreMatematica = elementMedia3BimestreMatematica.text
        textMedia4BimestreMatematica = elementMedia4BimestreMatematica.text
        notMedia4BimestreMatematica = False

        print("Matéria: Matemática")
        print("1º Bimestre:", textMedia1BimestreMatematica)
        if (textMedia1BimestreMatematica == "-"):
            textMedia1BimestreMatematica = 0
        print("2º Bimestre:", textMedia2BimestreMatematica)
        if (textMedia2BimestreMatematica == "-"):
            textMedia2BimestreMatematica = 0
        print("3º Bimestre:", textMedia3BimestreMatematica)
        if (textMedia3BimestreMatematica == "-"):
            textMedia3BimestreMatematica = 0
        print("4º Bimestre:", textMedia4BimestreMatematica)
        if (textMedia4BimestreMatematica == "-"):
            textMedia4BimestreMatematica = 0
            notMedia4BimestreMatematica = True

        if not isinstance(textMedia1BimestreMatematica, int):
            textMedia1BimestreMatematica = textMedia1BimestreMatematica.replace(",", ".")

        if not isinstance(textMedia2BimestreMatematica, int):
            textMedia2BimestreMatematica = textMedia2BimestreMatematica.replace(",", ".")
        
        if not isinstance(textMedia3BimestreMatematica, int):
            textMedia3BimestreMatematica = textMedia3BimestreMatematica.replace(",", ".")

        if not isinstance(textMedia4BimestreMatematica, int):
            textMedia4BimestreMatematica = textMedia4BimestreMatematica.replace(",", ".")

        textMediaMatematica = (float(textMedia1BimestreMatematica) + float(textMedia2BimestreMatematica) + (float(textMedia3BimestreMatematica) + float(textMedia4BimestreMatematica))) / 4
        
        if (textMediaMatematica >= 0.1 and textMediaMatematica <= 0.4):
            textMediaMatematica = 0.5
        elif (textMediaMatematica >= 0.6 and textMediaMatematica <= 0.9):
            textMediaMatematica = 1.0
        elif (textMediaMatematica >= 1.1 and textMediaMatematica <= 1.4):
            textMediaMatematica = 1.5
        elif (textMediaMatematica >= 1.6 and textMediaMatematica <= 1.9):
            textMediaMatematica = 2.0
        elif (textMediaMatematica >= 2.1 and textMediaMatematica <= 2.4):
            textMediaMatematica = 2.5
        elif (textMediaMatematica >= 2.6 and textMediaMatematica <= 2.9):
            textMediaMatematica = 3.0
        elif (textMediaMatematica >= 3.1 and textMediaMatematica <= 3.4):
            textMediaMatematica = 3.5
        elif (textMediaMatematica >= 3.6 and textMediaMatematica <= 3.9):
            textMediaMatematica = 4.0
        elif (textMediaMatematica >= 4.1 and textMediaMatematica <= 4.4):
            textMediaMatematica = 4.5
        elif (textMediaMatematica >= 4.6 and textMediaMatematica <= 4.9):
            textMediaMatematica = 5.0
        elif (textMediaMatematica >= 5.1 and textMediaMatematica <= 5.4):
            textMediaMatematica = 5.5
        elif (textMediaMatematica >= 5.6 and textMediaMatematica <= 5.9):
            textMediaMatematica = 6.0
        elif (textMediaMatematica >= 6.1 and textMediaMatematica <= 6.4):
            textMediaMatematica = 6.5
        elif (textMediaMatematica >= 6.6 and textMediaMatematica <= 6.9):
            textMediaMatematica = 7.0
        elif (textMediaMatematica >= 7.1 and textMediaMatematica <= 7.4):
            textMediaMatematica = 7.5
        elif (textMediaMatematica >= 7.6 and textMediaMatematica <= 7.9):
            textMediaMatematica = 8.0
        elif (textMediaMatematica >= 8.1 and textMediaMatematica <= 8.4):
            textMediaMatematica = 8.5
        elif (textMediaMatematica >= 8.6 and textMediaMatematica <= 8.9):
            textMediaMatematica = 9.0
        elif (textMediaMatematica >= 9.1 and textMediaMatematica <= 9.4):
            textMediaMatematica = 9.5
        elif (textMediaMatematica >= 9.6 and textMediaMatematica <= 9.9):
            textMediaMatematica = 10.0

        resultadoTextMediaMatematica = str(textMediaMatematica).replace(".", ",")
        print("Média: ", resultadoTextMediaMatematica[0:4])

        resultadoAprovacaoTextMediaMatematica = float(resultadoTextMediaMatematica.replace(",", "."))
        resultado_final_matematica = {}

        if (notMedia4BimestreMatematica is True) and (resultadoAprovacaoTextMediaMatematica < 6.0):
            resultado_final = "Falta nota para conclusão."
            print(f"Resultado Final: {resultado_final} 😬")

            resultado_final_matematica = {
                "nota_faltando": True,
                "resultado": resultado_final
            }
        elif (notMedia4BimestreMatematica is True) and (resultadoAprovacaoTextMediaMatematica >= 6.0):
            resultado_final = "Aprovado com antecedência!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_matematica = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        elif (resultadoAprovacaoTextMediaMatematica >= 6.0):
            resultado_final = "Aprovado!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_matematica = {
                "nota_faltando": False,
                "resultado": resultado_final
            }
        else:
            resultado_final = "Recuperação!"
            print(f"Resultado Final: {resultado_final} 😓")

            resultado_final_matematica = {
                "nota_faltando": False,
                "resultado": resultado_final
            }

        print("\n---------------------------- \n")

        # Pegando as médias de Quimica
        elementMedia1BimestreQuimica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[9]/td[2]"))
        )
        elementMedia2BimestreQuimica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[9]/td[5]"))
        )
        elementMedia3BimestreQuimica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[9]/td[8]"))
        )
        elementMedia4BimestreQuimica = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[2]/tbody/tr[9]/td[11]"))
        )
        textMedia1BimestreQuimica = elementMedia1BimestreQuimica.text
        textMedia2BimestreQuimica = elementMedia2BimestreQuimica.text
        textMedia3BimestreQuimica = elementMedia3BimestreQuimica.text
        textMedia4BimestreQuimica = elementMedia4BimestreQuimica.text
        notMedia4BimestreQuimica = False

        print("Matéria: Quimica")
        print("1º Bimestre:", textMedia1BimestreQuimica)
        if (textMedia1BimestreQuimica == "-"):
            textMedia1BimestreQuimica = 0
        print("2º Bimestre:", textMedia2BimestreQuimica)
        if (textMedia2BimestreQuimica == "-"):
            textMedia2BimestreQuimica = 0
        print("3º Bimestre:", textMedia3BimestreQuimica)
        if (textMedia3BimestreQuimica == "-"):
            textMedia3BimestreQuimica = 0
        print("4º Bimestre:", textMedia4BimestreQuimica)
        if (textMedia4BimestreQuimica == "-"):
            textMedia4BimestreQuimica = 0
            notMedia4BimestreQuimica = True

        if not isinstance(textMedia1BimestreQuimica, int):
            textMedia1BimestreQuimica = textMedia1BimestreQuimica.replace(",", ".")

        if not isinstance(textMedia2BimestreQuimica, int):
            textMedia2BimestreQuimica = textMedia2BimestreQuimica.replace(",", ".")
        
        if not isinstance(textMedia3BimestreQuimica, int):
            textMedia3BimestreQuimica = textMedia3BimestreQuimica.replace(",", ".")

        if not isinstance(textMedia4BimestreQuimica, int):
            textMedia4BimestreQuimica = textMedia4BimestreQuimica.replace(",", ".")

        textMediaQuimica = (float(textMedia1BimestreQuimica) + float(textMedia2BimestreQuimica) + (float(textMedia3BimestreQuimica) + float(textMedia4BimestreQuimica))) / 4
    
        if (textMediaQuimica >= 0.1 and textMediaQuimica <= 0.4):
            textMediaQuimica = 0.5
        elif (textMediaQuimica >= 0.6 and textMediaQuimica <= 0.9):
            textMediaQuimica = 1.0
        elif (textMediaQuimica >= 1.1 and textMediaQuimica <= 1.4):
            textMediaQuimica = 1.5
        elif (textMediaQuimica >= 1.6 and textMediaQuimica <= 1.9):
            textMediaQuimica = 2.0
        elif (textMediaQuimica >= 2.1 and textMediaQuimica <= 2.4):
            textMediaQuimica = 2.5
        elif (textMediaQuimica >= 2.6 and textMediaQuimica <= 2.9):
            textMediaQuimica = 3.0
        elif (textMediaQuimica >= 3.1 and textMediaQuimica <= 3.4):
            textMediaQuimica = 3.5
        elif (textMediaQuimica >= 3.6 and textMediaQuimica <= 3.9):
            textMediaQuimica = 4.0
        elif (textMediaQuimica >= 4.1 and textMediaQuimica <= 4.4):
            textMediaQuimica = 4.5
        elif (textMediaQuimica >= 4.6 and textMediaQuimica <= 4.9):
            textMediaQuimica = 5.0
        elif (textMediaQuimica >= 5.1 and textMediaQuimica <= 5.4):
            textMediaQuimica = 5.5
        elif (textMediaQuimica >= 5.6 and textMediaQuimica <= 5.9):
            textMediaQuimica = 6.0
        elif (textMediaQuimica >= 6.1 and textMediaQuimica <= 6.4):
            textMediaQuimica = 6.5
        elif (textMediaQuimica >= 6.6 and textMediaQuimica <= 6.9):
            textMediaQuimica = 7.0
        elif (textMediaQuimica >= 7.1 and textMediaQuimica <= 7.4):
            textMediaQuimica = 7.5
        elif (textMediaQuimica >= 7.6 and textMediaQuimica <= 7.9):
            textMediaQuimica = 8.0
        elif (textMediaQuimica >= 8.1 and textMediaQuimica <= 8.4):
            textMediaQuimica = 8.5
        elif (textMediaQuimica >= 8.6 and textMediaQuimica <= 8.9):
            textMediaQuimica = 9.0
        elif (textMediaQuimica >= 9.1 and textMediaQuimica <= 9.4):
            textMediaQuimica = 9.5
        elif (textMediaQuimica >= 9.6 and textMediaQuimica <= 9.9):
            textMediaQuimica = 10.0

        resultadoTextMediaQuimica = str(textMediaQuimica).replace(".", ",")
        print("Média:", resultadoTextMediaQuimica[0:4])

        resultadoAprovacaoTextMediaQuimica = float(resultadoTextMediaQuimica.replace(",", "."))
        dados_resultado = {}

        if (notMedia4BimestreQuimica is True) and (resultadoAprovacaoTextMediaQuimica < 6.0):
            resultado_final = "Falta nota para conclusão."
            print(f"Resultado Final: {resultado_final} 😬")

            resultado_final_quimica = {
                "nota_faltando": True,
                "resultado": resultado_final 
            }
        elif (notMedia4BimestreQuimica is True) and (resultadoAprovacaoTextMediaQuimica >= 6.0):
            resultado_final = "Aprovado com antecedência!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_quimica = {
                "nota_faltando": False,
                "resultado": resultado_final 
            }
        elif (resultadoAprovacaoTextMediaQuimica >= 6.0):
            resultado_final = "Aprovado!"
            print(f"Resultado Final: {resultado_final} 🥳")

            resultado_final_quimica = {
                "nota_faltando": False,
                "resultado": resultado_final 
            }
        else:
            resultado_final = "Recuperação!"
            print(f"Resultado Final: {resultado_final} 😓")

            resultado_final_quimica = {
                "nota_faltando": False,
                "resultado": resultado_final 
            }

        print("\n---------------------------- \n")

        # Pegando o percentual de falta do 1º bimestre até o 4º bimestre
        elementPercentualFalta1Bi = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[20]/td[4]"))
        )
        elementPercentualFalta2Bi= WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[20]/td[7]"))
        )
        elementPercentualFalta3Bi = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[20]/td[10]"))
        )
        elementPercentualFalta4Bi = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[20]/td[13]"))
        )
        textPercentualFalta1Bi = elementPercentualFalta1Bi.text[0:5].replace(",", ".").replace("%", "")
        textPercentualFalta2Bi = elementPercentualFalta2Bi.text[0:5].replace(",", ".").replace("%", "")
        textPercentualFalta3Bi = elementPercentualFalta3Bi.text[0:5].replace(",", ".").replace("%", "")
        textPercentualFalta4Bi = elementPercentualFalta4Bi.text[0:5].replace(",", ".").replace("%", "")

        somaPercentualFalta = float(textPercentualFalta1Bi) + float(textPercentualFalta2Bi) + float(textPercentualFalta3Bi) + float(textPercentualFalta4Bi)
        print("Percentual Total de Faltas do ano:", str(somaPercentualFalta)[0:5] + "%")

        print("\n---------------------------- \n")
        print("Todas suas notas foram exibidas!")
        print("\n---------------------------- \n")

        medias = {
            "Biologia": {
                "1Bimestre": textMedia1BimestreBiologia,
                "2Bimestre": textMedia2BimestreBiologia,
                "3Bimestre": textMedia3BimestreBiologia,
                "4Bimestre": textMedia4BimestreBiologia,
                "mediaAnual": resultadoTextMediaBiologia
            },
            "Fisica": {
                "1Bimestre": textMedia1BimestreFisica,
                "2Bimestre": textMedia2BimestreFisica,
                "3Bimestre": textMedia3BimestreFisica,
                "4Bimestre": textMedia4BimestreFisica,
                "mediaAnual": resultadoTextMediaFisica
            },
            "Geografia": {
                "1Bimestre": textMedia1BimestreGeografia,
                "2Bimestre": textMedia2BimestreGeografia,
                "3Bimestre": textMedia3BimestreGeografia,
                "4Bimestre": textMedia4BimestreGeografia,
                "mediaAnual": resultadoTextMediaGeografia
            },
            "Historia": {
                "1Bimestre": textMedia1BimestreHistoria,
                "2Bimestre": textMedia2BimestreHistoria,
                "3Bimestre": textMedia3BimestreHistoria,
                "4Bimestre": textMedia4BimestreHistoria,
                "mediaAnual": resultadoTextMediaHistoria
            },
            "Ingles": {
                "1Bimestre": textMedia1BimestreIngles,
                "2Bimestre": textMedia2BimestreIngles,
                "3Bimestre": textMedia3BimestreIngles,
                "4Bimestre": textMedia4BimestreIngles,
                "mediaAnual": resultadoTextMediaIngles
            },
            "Portugues": {
                "1Bimestre": textMedia1BimestrePortugues,
                "2Bimestre": textMedia2BimestrePortugues,
                "3Bimestre": textMedia3BimestrePortugues,
                "4Bimestre": textMedia4BimestrePortugues,
                "mediaAnual": resultadoTextMediaPortugues
            },
            "Matematica": {
                "1Bimestre": textMedia1BimestreMatematica,
                "2Bimestre": textMedia2BimestreMatematica,
                "3Bimestre": textMedia3BimestreMatematica,
                "4Bimestre": textMedia4BimestreMatematica,
                "mediaAnual": resultadoTextMediaMatematica
            },
            "Quimica": {
                "1Bimestre": textMedia1BimestreQuimica,
                "2Bimestre": textMedia2BimestreQuimica,
                "3Bimestre": textMedia3BimestreQuimica,
                "4Bimestre": textMedia4BimestreQuimica,
                "mediaAnual": resultadoTextMediaQuimica
            },
            
        }

        generating_pdf(medias, primeiroNomeEstudante, somaPercentualFalta, resultado_final_biologia,
        resultado_final_fisica, resultado_final_geografia, resultado_final_historia, resultado_final_ingles,
        resultado_final_portugues, resultado_final_matematica, resultado_final_quimica)

        # Deixa o prompt 10 segundos aberto.
        time.sleep(10)

        # Fecha o navegador
        driver.quit()

    except TimeoutException:
        time.sleep(10) # Deixa o prompt 10 segundos aberto.
        print("\nFalha ao entrar na conta, login ou senha incorreta :(")

        # Dev do Projeto: Elieverton Gomes
        # Ultima Atualização: 28/05 as 13:36h

structure()