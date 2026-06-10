# Trabalho AV2 - Teoria da Computabilidade
CESUPA
Curso: Ciencia da Computacao CC5NA
Professor: Daniel Leal Souza

## Integrantes da Equipe
* Davi Correa
* Gabriel Alencar
* Alberto Acosta

---

## Modelos Escolhidos e Problemas Desenvolvidos

1. Maquina de Turing com Multiplas Fitas (Opcao 3)
* Problema: Sincronizador e Auditor de Integridade de Fluxos Binarios.
* Descricao: O modelo recebe dois fluxos de dados independentes (Fitas 1 e 2). Ele valida a presenca dos marcadores de cabecalho 'HD' e rodape 'FN'. Caso os dados entre os marcadores sejam perfeitamente identicos bit a bit, a maquina consolida as informacoes escrevendo o resultado na Fita 3 e finaliza com o caractere de validacao 'V'. Possui 10 estados logicos e atende aos criterios de nao-trivialidade.

2. Automato de Pilha (Opcao 9)
* Problema: Validador Sintatico de Blocos de Comando 'RAIOS'.
* Descricao: Um analisador sintatico customizado que exige o disparo obrigatorio pelo prefixo 'RAIOS', seguido por um miolo contendo delimitadores de escopo de parenteses '()' e colchetes '[]' que devem estar perfeitamente aninhados e balanceados atraves do controle da pilha. O bloco deve obrigatoriamente encerrar com o sufixo 'END'. A maquina possui 10 estados para cobrir toda a esteira de tokens e escopos.

---

## Estrutura do Repositorio
* /implementacoes : Codigos-fonte desenvolvidos em Python.
* /testes : Relatorios detalhados de rastreamento e configuracoes formais de execucao.
* uso_ia.md : Declaracao de uso e rastreabilidade de ferramentas de IA.

---

## Instrucoes de Execucao

As duas aplicacoes foram construidas utilizando Python 3 nativo, sem necessidade de instalacao de dependencias de terceiros.

Para executar o Sincronizador (Maquina de Turing de 3 Fitas):
$ python implementacoes/mt_multifita.py

Para executar o Validador de Sintaxe (Automato de Pilha):
$ python implementacoes/pda_validador.py