Feature: Visualizar Histórico de pagamentos

    Scenario: Visualizar pagamentos
        Given que acesso o site Iterasys Learnworlds
        When clico em Entrar
        And preencho os campos de login
        And clico no botão Entrar
        Then sou direcionado para página Home
        When acesso ao Perfil através do botao Visit profile
        And clico em Edit profile
        And clico no botao Pagamentos
        Then o histórico de pagamentos é apresentado para consulta