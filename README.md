# Automação de Consulta de Notas no SIEPE

Este projeto consiste em um script Python para automatizar a consulta das notas dos alunos no sistema SIEPE (Sistema Integrado de Educação de Pernambuco). O script utiliza a biblioteca Selenium para realizar a automação do navegador Chrome.

## Pré-requisitos

- Python 3.x instalado no sistema.
- Biblioteca Selenium instalada. Você pode instalar utilizando o seguinte comando: pip install selenium
- Driver do Chrome compatível com a versão do seu navegador. Certifique-se de baixar o driver adequado para sua versão do Chrome [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads) e garantir que o diretório do driver esteja no PATH do sistema.

## Funcionalidades

- Automatiza o processo de login no SIEPE.
- Extrai as notas dos alunos em disciplinas específicas.
- Exibe as notas dos quatro bimestres em disciplinas como Biologia, Física, Geografia, História, Inglês, Português, Matemática e Química.

## Como Usar

1. Clone este repositório: git clone https://github.com/Elieverton6/consultarMediaEscolarSiepe

2. Navegue até o diretório do projeto:

3. Execute o script Python: mediasEscolar.py
   
4. Siga as instruções no terminal para inserir suas credenciais do SIEPE.

5. Após a autenticação bem-sucedida, o script exibirá as notas disponíveis para cada disciplina.

## Observações

- Certifique-se de inserir suas credenciais do SIEPE corretamente para evitar falhas na autenticação.
- O script foi projetado para funcionar no modo Headless, o que significa que não exibirá a interface do navegador durante a execução. Se desejar visualizar a interface, remova a opção "--headless" das configurações do Chrome no script.

## Autor

Elieverton Gomes - https://github.com/Elieverton6
