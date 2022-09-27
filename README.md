# Compilador simulador da linguagem de terminal do jogo Minecraft

**Trabalho 6 da Disciplina de Construção de Compiladores**

**Professor: Daniel Lucrédio**

## Integrantes ##

- Lucas Vinícius Domingues 769699
- Rafael Yoshio Yamawaki Murata 769681

## Descrição

A linguagem elaborada consiste em uma simulação do terminal do jogo Minecraft, cujos comandos forma adaptados para servir aos própositos da disciplina de compiladores.

Neste trabalho, são implementados os comandos summon,give,kill, gamemode, time set, weather,tp e difficulty. Os comandos devem ser passados em um arquivo como uma lista de comandos. Todo comando deve ser precedido com um '/'.

- Summon invoca Players ou Mobs (inimigos), serve como uma "declaração de variável" para a linguagem. É possível invocar um Player passando seu nome (que deve ser um identificador único) e o tipo Player. Para invocar um Mob, deve-se passar seu nome (também é um identificador único) e o tipo de Mob. Os tipos de Mob disponíveis são: Creeper, Skeleton, Spider, Slime, Enderman e Zombie.

- Give da um item a um Player (dar itens a Mobs não é permitido), para isso, é necessário especificar o nome do Player para quem se quer dar os itens ou utilizar o '@a' para dar o item a todos o Players, também é necessário especificar o item que se quer dar e a quantidade. Os itens disponíveis são: Sword, Axe, Pickaxe, Bow, Arrow, Helmet, Chestplate, Leggings e Boots. Pode-se especificar os tipos  Wooden, Stone, Iron, Golden, Diamond para os itens a serem dados. Estes itens ficaram armazenados no inventário do Player.

- Kill elimina um Player ou um Mob. Para utilizar o comando, basta passar como seu parâmetro o nome da entidade a ser eliminada.

- Gamemode muda o modo de jogo. Os modos de jogo disponíveis são 0 (Survival), 1 (Creative), 2 (Adventure), 3 (Spectator).

- Time set muda o horário do jogo. Para determinar o novo horário, pode-se passar um número inteiro de 0 a 23000, ou uma String contendo horários pré-definidos do dia.
Os horários pré-defindos são: day (7:00am ou 10000) , noon/midday (12:00pm ou 6000), sunset/dusk (6:00pm ou 12000), midnight (12:00am ou 18000) e sunrise/dawn (5:00am ou 23000).

- Weather muda o clima do jogo. Os climas disponíveis são: clear, rain, snow, thunder.

- Tp teleporta um jogador ou todos os jogadores para uma determinada posição. Para isto, basta indicar o nome do jogador a ser teleportado, ou utilizar '@a' para todos os jogadores, e indicadar as coordenadas da nova posição com 3 números reais para os eixos x, y e z.

- Difficulty muda a dificuldade, as dificuldades disponíveis são: peaceful, easy, normal e hard.


## Dependencias

- Python 3
- Atlr4
- Venv


## Ubuntu

É necessário instalar o pip:

```
 sudo apt-get install python3-pip
```
Instale o venv:

```
 sudo pip3 install virtualenv
```

Vá a pasta do projeto e ative o venv

```
 source .venv/bin/activate
```
Instale o antlr4
```
 pip install antlr4-python3-runtime
```
