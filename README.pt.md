# cs_binary

Este repositório cliente-servidor de reprodução musical foi desenvolvido para a disciplina de Redes de Computadores da Universidade Federal de São João del Rei.

*Leia a versão deste documento em outro idioma: [Inglês](README.md)*


## Índice
  - [CS](#cs_binary)
    - [Licença](#licenca)
    - [Requisitos](#requisitos)
    - [Instalação](#instalacao)
      - [Clonar Repositório](#clonar-repositorio)
      - [Windows](#windows)
      - [Ubuntu 18.04](#ubuntu-18.04)
        - [Instalação Manual](#instalacao-manual)
        - [Instalação Automática](#instalacao-automatica)
        - [Pacotes Binários Unix](#pacotes-binarios-unix)
    - [Cliente](#cliente)
      - [Linha de Comando](#linha-de-comando)
        - [Comandos](#comandos)
      - [Exemplos](#exemplos)   
    - [Servidor](#servidor)
      - [Linha de Comando](#linha-de-comando-1)
      - [Exemplos](#exemplos-1)


## Licença

Você está livre para usar este pacote, mas se ele chegar ao seu ambiente de produção, agradecemos muito que você nos envie um cartão postal de sua cidade natal, mencionando qual de nossos pacotes você está usando.

Endereço: 

    Universidade Federal de São João del-Rei – UFSJ
    Campus Tancredo de Almeida Neves – CTAN
    Prédio do Curso de Ciência da Computação, 3° andar/Sala nº 3.01A
    Av. Visconde do Rio Preto, s/nº, Colônia do Bengo,
    São João del-Rei, MG, CEP 36301-360



## Requisitos

* [Python](http://www.python.org/download/) (testado com v2.7)
* [Pillow](https://pillow.readthedocs.io/en/latest/) (testado com pillow >= 5.0.0)*
* [Tkinter](http://www.tkdocs.com/tutorial/install.html) (testado com 8.6)*
* [py-game](https://www.pygame.org/wiki/GettingStarted) (v3.6.1)*

`* necessário apenas ao executar o servidor`

## Instalação


### Clonar Repositório

Ao clonar um repositório, o `.git` pode ser deixado fora do final.

```bash
$ git clone --depth 1 https://github.com/thiagomides/cs_binary.git
```


### Windows

1. Instalar python 2.7.
2. Download pip então [compilar](https://bootstrap.pypa.io/get-pip.py) e instalar.
3. Instalar pacote Pygame `py -m pip install -U pygame --user`
4. Tutorial para instalar o python-tk [tutorial](http://www.tkdocs.com/tutorial/install.html#installwin)
5. Instalar pacote Pillow `pip install Pillow`

### Ubuntu 18.04

#### Instalação Manual

1. Instalar pacotes: `sudo apt-get install python2.7 python-pygame python-tk python-pip`
2. Instalar pacote Pillow `pip install Pillow`

#### Instalação Automática

```bash
    sudo chmod +X setup.sh && ./setup.sh
```


#### Pacotes Binários Unix

| Distribuição | Python 3 pacote | Python 2 pacote |
| ----- | ---- | ---- |
| Debian/Ubuntu | python3-pygame |  python-pygame |
| Fedora/Ubuntu | python3-pygame |  pygame |

## Cliente

Existem três maneiras de usar este script:

1. Arraste seu arquivo(s) `.*` para `client.py`.
2. Arraste seu diretório para `client.py`.
3. Usando a linha de comando que também oferece opções mais avançadas.


### Linha de Comando

    uso: client.py [-h] [--port PORT] [--address IP] [--command CMD] [--directory DIR]
                  [--file DOF] [--no-keep-alive]
    

    Split client binary book by chapters.

    argumentos posicionais:
      (filename or directory)               .* arquivo (s) a ser reproduzido.

    argumentos opcionais:
      -h,      --help             mostre esta mensagem de ajuda e saia.
      -p PORT, --port       PORT  o número da porta PORT para escutar (padrão: 3030)
      -a IP,   --address    IP    número do endereço para ouvir (padrão: 127.0.0.1)
      -f DOF,  --file       DOF   diretório dos arquivo(s) binário(s) ou arquivo binário.
      -c STR,  --command    CMD   personalizar o comandos (consulte o README)
      -e EXT,  --extension  EXT   definir extensão de arquivos (padrão: /*.mp3)
      --no-keep-alive             as conexões são consideradas persistentes a menos que um --no-keep-alive esteja incluído

  

#### Comandos
Você pode personalizar o comando chapter com `--command CMD`, onde `CMD` é um python [format string] válido (http://docs.python.org/library/stdtypes.html#string-formatting-operations).

    command arguments:
      list                devolver playlist agora
      next                começar uma nova reprodução de som
      play                começar a reprodução do som
      stop                parar temporariamente a reprodução de todos os canais de som
      noow                devolve o nome da musica atual
      rewind              reiniciar música
      play_music          tocar música pelo identificador

  

### Exemplos

Reproduzir arquivo (arrastar um arquivo .* Para o `client.py`):

    python client.py -f  Led_Zeppelin-Stairway_To_Heaven.mp3

Reproduzir arquivo(s) da pasta sem conexões persistentes:

    python client.py -f ~/Music/Beatles/The_White_Album/ --no-keep-alive

Obter a lista de reprodução do servidor:

    python client.py -c list

Escolher porta do servidor e enviar vários arquivos:

    python client.py -d ~/Music/Beatles/The_White_Album/ -p 3035


## Servidor

Existe uma maneira de usar este script:

1. Usando a linha de comando que também oferece opções mais avançadas.

### Linha de Comando

    uso: server.py [-h] [--port PORT] [--directory DIR]
    
    argumentos opcionais:
      -h, --help                       show this help message and exit.
      -p PORT, --port            PORT  port number to listen up
      -d DIR,  --directory       DIR   binary(s) storage folder (default: ../arquivos/)



### Exemplos

Default:

    python server.py

Alteração do soquete do servidor, modificar pasta de armazenamento:

    python server -p 3030 -d ../arquivos/


