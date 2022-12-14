# Compilador simulador da linguagem de terminal do jogo Minecraft

**Trabalho 6 da Disciplina de Construção de Compiladores**

**Professor: Daniel Lucrédio**

## Integrantes ##

- Lucas Vinícius Domingues 769699
- Rafael Yoshio Yamawaki Murata 769681

## Descrição

Para o vídeo de descrição [clique aqui](https://www.youtube.com/watch?v=nDYnn3Xw2I4)

A linguagem elaborada consiste em uma simulação do terminal do jogo Minecraft, cujos comandos forma adaptados para servir aos própositos da disciplina de compiladores.

Neste trabalho, são implementados os comandos summon,give,kill, gamemode, time set, weather,tp e difficulty. Os comandos devem ser passados em um arquivo como uma lista de comandos. Todo comando deve ser precedido com um '/'.

- Summon invoca Players ou Mobs (inimigos), serve como uma "declaração de variável" para a linguagem. É possível invocar um Player passando seu nome (que deve ser um identificador único) e o tipo Player. Para invocar um Mob, deve-se passar seu nome (também é um identificador único) e o tipo de Mob. Os tipos de Mob disponíveis são: Creeper, Skeleton, Spider, Slime, Enderman e Zombie.

- Give da um item a um Player (dar itens a Mobs não é permitido), para isso, é necessário especificar o nome do Player para quem se quer dar os itens ou utilizar o '@a' para dar o item a todos o Players, também é necessário especificar o item que se quer dar e a quantidade. Os itens disponíveis são: Sword, Axe, Pickaxe, Bow, Arrow, Helmet, Chestplate, Leggings e Boots. Pode-se especificar os tipos  Wooden, Stone, Iron, Golden, Diamond para os itens a serem dados. Estes itens ficaram armazenados no inventário do Player, que possuíra um limite de 41 slots de items .

- Kill elimina um Player ou um Mob. Para utilizar o comando, basta passar como seu parâmetro o nome da entidade a ser eliminada.

- Gamemode muda o modo de jogo. Os modos de jogo disponíveis são 0 (Survival), 1 (Creative), 2 (Adventure), 3 (Spectator).

- Time set muda o horário do jogo. Para determinar o novo horário, pode-se passar um número inteiro de 0 a 23000, ou uma String contendo horários pré-definidos do dia.
Os horários pré-defindos são: day (7:00am ou 10000) , noon/midday (12:00pm ou 6000), sunset/dusk (6:00pm ou 12000), midnight (12:00am ou 18000) e sunrise/dawn (5:00am ou 23000).

- Weather muda o clima do jogo. Os climas disponíveis são: clear, rain, snow, thunder.

- Tp teleporta um jogador ou todos os jogadores para uma determinada posição. Para isto, basta indicar o nome do jogador a ser teleportado, ou utilizar '@a' para todos os jogadores, e indicadar as coordenadas da nova posição com 3 números reais para os eixos x, y e z.

- Difficulty muda a dificuldade, as dificuldades disponíveis são: peaceful, easy, normal e hard.

As sequências de comandos devem ser passadas a partir de um arquivo txt. Caso os comando passados passem nas verificações léxicas, sintáticas e semânticas, os resultados simulados dos comandos serão impressos no terminal, e será gerado um arquivo Python com o nome generated_file.py que quando executado também imprimirá as saídas esperadas caso estes comandos tivessem sido inseridos no terminal no Minecraft (com as devidas adaptações realizadas para o contexto do trabalho).
## Dependências

- Java
- Python 3
- Pip
- Venv
- Antlr4


## Ubuntu

Crie um novo ambiente virtual na raiz do projeto

```
 virtualenv .venv
```

Ainda na raiz do projeto, abra um novo terminal e ative o novo ambiente criado utilizando

```
 source .venv/bin/activate
```

Instale o arquivo de dependências no ambiente
```
 pip install -r requirements.txt
```

Instale o Java:

```
sudo apt install default-jdk
```

Baixe a [versão 4.11.1 do antlr](https://www.antlr.org/download.html)

Compile o arquivo ```Commands.g4```
```
 java -jar <caminho para o antlr-4.11.1-complete.jar> -Dlanguage=Python3 Commands.g4 -visitor -o visitorFiles
```

Execute o arquivo principal
```
 python main.py .\casos_de_teste\<tipo_do_caso>\testes\<teste_escolhido>
```

Alternativamente, você pode instalar definer o antlr4 como um comando. Após instalar o Java, execute os seguintes passos: 

No terminal, execute os comandos descritos na [seção de instalação do site oficial](https://www.antlr.org/) 
```
$ cd /usr/local/lib
$ sudo curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'
```

Então, para compilar a gramática Commands.g4:
```
antlr4 -Dlanguage=Python3 Commands.g4 -visitor -o dist
```

## Windows
Crie um novo ambiente virtual na raiz do projeto

```
 virtualenv .venv
```
Ainda na raiz do projeto, abra um novo terminal e ative o novo ambiente criado utilizando

```
 .venv/Scripts/activate
```

Instale o arquivo de dependências no ambiente
```
 pip install -r requirements.txt
```

Baixe a [versão 4.11.1 do antlr](https://www.antlr.org/download.html)

Compile o arquivo ```Commands.g4```
```
 java -jar <caminho para o antlr-4.11.1-complete.jar> -Dlanguage=Python3 Commands.g4 -visitor -o visitorFiles
```

Execute o arquivo principal
```
 python main.py .\casos_de_teste\<tipo_do_caso>\testes\<teste_escolhido>
```
