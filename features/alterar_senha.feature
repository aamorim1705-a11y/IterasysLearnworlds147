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

    Scenario Outline: Alterar senha com dados inválidos
        Given que acesso o site Iterasys Learnworlds
        When clico em Entrar
        And preencho os campos de login
        And clico no botão Entrar
        Then sou direcionado para página Home
        When acesso ao Perfil através do botao Visit profile
        And clico em Edit profile
        And clico no botao Editar na secçao Segurança da conta
        And preencho os campos senha atual <senha atual>, nova senha <nova senha> e confirmação da nova senha <confirmação da nova senha>
        And clico no botao Salvar da Segurança da conta
        Then exibe a <mensagem> com erro

        Examples:
        | id | senha atual  | nova senha     | confirmação da nova senha | mensagem                              |
        | 01 |              | VALIDA         | VALIDA                    | Current password is required          |
        | 02 | VALIDA       |                | VALIDA                    | New password is required              |
        | 03 | VALIDA       | VALIDA         |                           | New password confirmation is required |                             
                                     