Feature: Editar Detalhes de faturamento

    Scenario Outline: Editar detalhes de faturamento com dados válidos
        Given que acesso o site Iterasys Learnworlds
        When clico em Entrar
        And preencho os campos de login
        And clico no botão Entrar
        Then sou direcionado para página Home
        When acesso ao Perfil através do botao Visit profile
        And clico em Edit profile
        And clico no botao Detalhes de faturamento
        And clico em Editar na secçao Detalhes de faturamento
        And preencho os campos Name <Name>, Address <Address>, City <City>, Postal Code <Postal code> e Country <Country> com dados válidos
        And clico em Salvar na secçao Detalhes de faturamento
        Then a <mensagem> é exibida

        Examples:
        | id | Name         | Address          | City    | Postal code | Country |  mensagem                    |
        | 01 | Juliana Cruz | Rua Ernesto Melo | Coimbra | 3200400     | Portugal | Dados de faturamento salvos |