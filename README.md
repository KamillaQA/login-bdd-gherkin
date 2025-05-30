# Projeto BDD com Gherkin usando Behave e Selenium

Este projeto exemplifica a implementação de testes automatizados no estilo BDD (Behavior Driven Development) utilizando a linguagem Gherkin para descrever cenários e a ferramenta [Behave](https://behave.readthedocs.io/en/latest/) para executar esses cenários. Os testes automatizados simulam o comportamento de um usuário real usando Selenium WebDriver para interação com a interface web.

---

## Descrição

O objetivo do projeto é demonstrar a escrita de cenários claros e legíveis em Gherkin, separando a especificação do comportamento (arquivos `.feature`) da implementação técnica dos testes (steps em Python). O exemplo cobre um fluxo básico de login em uma página web mockada localmente.

---

## Estrutura do projeto

- `features/` - Contém os arquivos de especificação `.feature` escritos em Gherkin.  
- `features/steps/` - Implementação dos passos de teste em Python usando Selenium.  
- `login.html` - Página HTML local usada para simular o sistema web de login.  

---

## Pré-requisitos

- Python 3.7+  
- Navegador Google Chrome instalado  
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatível com sua versão do Chrome (deve estar no PATH ou na mesma pasta do script)  
- Instalar dependências via pip:

```bash
pip install behave selenium
Como executar os testes
Clone este repositório:

bash
Copiar
Editar
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
Verifique se o arquivo login.html está presente na raiz do projeto.

Execute os testes com Behave:

bash
Copiar
Editar
behave
O navegador será aberto, o teste será executado no mock local, e o resultado aparecerá no console.

Personalização
Para alterar a página de teste, modifique o arquivo login.html.

Os testes podem ser adaptados para URLs reais ajustando o código dos passos (steps).
