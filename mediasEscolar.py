from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time

try:
    # Configurações do Chrome para ativar o modo Headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Define o tamanho da janela
    driver.set_window_size(1366, 1080)

    # Abre a URL no navegador
    driver.get("https://www.siepe.educacao.pe.gov.br/")

    # Suas credenciais pra acessar a conta
    print("Digite suas credenciais do SIEPE abaixo. \n")
    login = input("Digite seu Login: ") # Seu Login
    password = input("Digite sua Senha: ") # Sua Senha

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

    # Espera ate que o elemento PegarNomeEstudante esteja presente na pagina e seleciona ele
    elementPegarNomeEstudante = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/form/div/strong"))
    )
    nomeEstudanteCompleto = elementPegarNomeEstudante.text
    primeiroNomeEstudante = nomeEstudanteCompleto.split()[0] # Me retorna somente o primeiro nome.
    primeiroNomeEstudante = primeiroNomeEstudante.capitalize() # Primeira letra do nome maiuscula
    print("\nOlá " + primeiroNomeEstudante + ", confira suas notas: \n")


    # Espera ate que o elemento de Boletim esteja presente na pagina e seleciona ele
    elementCategoriaBoletim = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/form/div/a"))
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
    print("Nota 1 Bimestre de Biologia: ", textMedia1BimestreBiologia)
    print("Nota 2 Bimestre de Biologia: ", textMedia2BimestreBiologia)
    print("Nota 3 Bimestre de Biologia: ", textMedia3BimestreBiologia)
    print("Nota 4 Bimestre de Biologia: ", textMedia4BimestreBiologia)
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
    print("Nota 1 Bimestre de Fisica: ", textMedia1BimestreFisica)
    print("Nota 2 Bimestre de Fisica: ", textMedia2BimestreFisica)
    print("Nota 3 Bimestre de Fisica: ", textMedia3BimestreFisica)
    print("Nota 4 Bimestre de Fisica: ", textMedia4BimestreFisica)
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
    print("Nota 1 Bimestre de Geografia: ", textMedia1BimestreGeografia)
    print("Nota 2 Bimestre de Geografia: ", textMedia2BimestreGeografia)
    print("Nota 3 Bimestre de Geografia: ", textMedia3BimestreGeografia)
    print("Nota 4 Bimestre de Geografia: ", textMedia4BimestreGeografia)
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
    print("Nota 1 Bimestre de Historia: ", textMedia1BimestreHistoria)
    print("Nota 2 Bimestre de Historia: ", textMedia2BimestreHistoria)
    print("Nota 3 Bimestre de Historia: ", textMedia3BimestreHistoria)
    print("Nota 4 Bimestre de Historia: ", textMedia4BimestreHistoria)
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
    print("Nota 1 Bimestre de Ingles: ", textMedia1BimestreIngles)
    print("Nota 2 Bimestre de Ingles: ", textMedia2BimestreIngles)
    print("Nota 3 Bimestre de Ingles: ", textMedia3BimestreIngles)
    print("Nota 4 Bimestre de Ingles: ", textMedia4BimestreIngles)
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
    print("Nota 1 Bimestre de Português: ", textMedia1BimestrePortugues)
    print("Nota 2 Bimestre de Português: ", textMedia2BimestrePortugues)
    print("Nota 3 Bimestre de Português: ", textMedia3BimestrePortugues)
    print("Nota 4 Bimestre de Português: ", textMedia4BimestrePortugues)
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
    print("Nota 1 Bimestre de Matemática: ", textMedia1BimestreMatematica)
    print("Nota 2 Bimestre de Matemática: ", textMedia2BimestreMatematica)
    print("Nota 3 Bimestre de Matemática: ", textMedia3BimestreMatematica)
    print("Nota 4 Bimestre de Matemática: ", textMedia4BimestreMatematica)
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
    print("Nota 1 Bimestre de Quimica: ", textMedia1BimestreQuimica)
    print("Nota 2 Bimestre de Quimica: ", textMedia2BimestreQuimica)
    print("Nota 3 Bimestre de Quimica: ", textMedia3BimestreQuimica)
    print("Nota 4 Bimestre de Quimica: ", textMedia4BimestreQuimica)
    print("\n---------------------------- \n")

    # Pegando o percentual de falta do 1º bimestre até o 4º bimestre
    elementPercentualFalta1Bi = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[11]/td[4]"))
    )
    elementPercentualFalta2Bi= WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[11]/td[7]"))
    )
    elementPercentualFalta3Bi = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[11]/td[10]"))
    )
    elementPercentualFalta4Bi = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[11]/td[13]"))
    )
    textPercentualFalta1Bi = elementPercentualFalta1Bi.text[0:3].replace(",", ".")
    textPercentualFalta2Bi = elementPercentualFalta2Bi.text[0:3].replace(",", ".")
    textPercentualFalta3Bi = elementPercentualFalta3Bi.text[0:3].replace(",", ".")
    textPercentualFalta4Bi = elementPercentualFalta4Bi.text[0:3].replace(",", ".")

    somaPercentualFalta = float(textPercentualFalta1Bi) + float(textPercentualFalta2Bi) + float(textPercentualFalta3Bi) + float(textPercentualFalta4Bi)
    print("Percentual Total de Faltas do ano:", str(somaPercentualFalta) + "%")
    print("\n---------------------------- \n")
    print("Todas suas notas foram exibidas, script finalizado!")

    # Deixa o prompt 1 minuto aberto.
    time.sleep(60)

    # Fecha o navegador
    driver.quit()
except TimeoutException:
    time.sleep(10) # Deixa o prompt 10 segundos aberto.
    
    print("\nFalha ao entrar na conta, login ou senha incorreta :(")
