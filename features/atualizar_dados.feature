Feature: Atualizar dados

    Scenario: Dados validos
        Given que acesso o site Iterasys Learnworlds
        When clico em Entrar
        And preencho os campos de login
        And clico no botão Entrar
        Then sou direcionado para página Home
        When acesso ao Perfil através do botao Visit profile
        And clico em Edit profile
        And clico no botao Editar na secçao Dados pessoais
        And preencho os campos Nome Andréa Souza e E-mail aamorim1705@gmail.com 
        And clico no botão Salvar
        Then os dados pessoais sao atualizados com sucesso

    Scenario Outline: Dados negativos
        Given que acesso o site Iterasys Learnworlds
        When clico em Entrar
        And preencho os campos de login
        And clico no botão Entrar
        Then sou direcionado para página Home
        When acesso ao Perfil através do botao Visit profile
        And clico em Edit profile
        And clico no botao Editar na secçao Dados pessoais
        And preencho os campos Nome <Nome> e E-mail <Email> 
        And clico no botão Salvar
        Then exibe a <mensagem> de erro

        Examples:
        | id | Nome         | Email                 | mensagem             |
        | 01 |              | aamorim1705@gmail.com | Username is required |
        | 02 | Andréa Souza |                       | Email is required    |
        | 03 | Andréa Souza | aamorim1705@gmail     | Invalid email        |
        



        



