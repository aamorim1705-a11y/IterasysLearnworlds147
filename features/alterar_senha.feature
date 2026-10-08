Feature: Alterar senha

    Scenario: Alterar senha com dados válidos
        Given que acesso o site Iterasys Learnworlds
        When clico em Entrar
        And preencho os campos de login
        And clico no botão Entrar
        Then sou direcionado para página Home
        When acesso ao Perfil através do botao Visit profile
        And clico em Edit profile
        And clico no botao Editar na secçao Segurança da conta
        And preencho os campos senha atual, nova senha e confirmação da nova senha
        And clico no botao Salvar da Segurança da conta
        Then senha é atualizada com sucesso