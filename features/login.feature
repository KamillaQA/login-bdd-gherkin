Feature: Login do usuário

  Scenario: Usuário faz login com sucesso
    Given que o usuário está na página de login
    When ele insere o email "usuario@teste.com" e a senha "senha123"
    And clica no botão entrar
    Then ele deve ver o painel inicial
