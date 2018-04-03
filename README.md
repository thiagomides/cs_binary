# cs_binary

This music play Client-Server repository a developed for Computer Networks discipline of Federal São João del Rei University.

*Read this in other languages: [Portuguese](README.md)*


## Table of Contents
  - [CS](#cs_binary)
    - [License](#license)
    - [Requirements](#requirements)
    - [Installation](#installation)
      - [Cloning a Repository](#cloning-a-repository)
      - [Windows](#windows)
      - [Ubuntu 16.10](#ubuntu-16.10)
        - [Unix Binary Packages](#unix-binary-packages)
    - [Client](#client-usage)
      - [Command Line Help](#command-line-help)
        - [Chapter command](#chapter-command)
      - [Examples](#examples)   
    - [Server](#server-usage)
      - [Command Line Help](#command-line-help-1)
      - [Examples](#examples-1)


## License

You're free to use this package, but if it makes it to your production environment we highly appreciate you sending us a postcard from your hometown, mentioning which of our package(s) you are using.

Our address is: 

    Universidade Federal de São João del-Rei – UFSJ
    Campus Tancredo de Almeida Neves – CTAN
    Prédio do Curso de Ciência da Computação, 3° andar/Sala nº 3.01A
    Av. Visconde do Rio Preto, s/nº, Colônia do Bengo,
    São João del-Rei, MG, CEP 36301-360



## Requirements

* [Python](http://www.python.org/download/) (tested with v2.7)
* [Pillow](https://pillow.readthedocs.io/en/latest/)(tested with pillow >= 5.0.0)*
* [Tkinter](http://www.tkdocs.com/tutorial/install.html) (tested with 8.6)*
* [py-game](https://www.pygame.org/wiki/GettingStarted) (v3.6.1)*

`* required only when running the server`
## Installation


### Cloning a Repository

When cloning a repository the `.git` can be left off the end.

```bash
$ git clone --depth 1 https://github.com/thiagomides/cs_binary.git
```


### Windows

1. Install python 2.7.
2. Download pip then [compile](https://bootstrap.pypa.io/get-pip.py) and install.
3. Install package Pygame `py -m pip install -U pygame --user`
4. Tutorial for install python-tk [tutorial](http://www.tkdocs.com/tutorial/install.html#installwin)
5. Install package Pillow `pip install Pillow`

### Ubuntu 18.04

#### Manual Installation

1. Install packages: `sudo apt-get install python2.7 python-pygame python-tk python-pip`
2. Install package Pillow `pip install Pillow`

#### Automatic Installation

```bash
    sudo chmod +X setup.sh && ./setup.sh
```


#### Unix Binary Packages

| Distribution | Python 3 package | Python 2 package |
| ----- | ---- | ---- |
| Debian/Ubuntu | python3-pygame |  python-pygame |
| Fedora/Ubuntu | python3-pygame |  pygame |

## Client usage

There are three ways to use this script:

1. Drag your `.*` file(s) onto `client.py`.
2. Drag your directory onto `client.py`.
3. Using the command line which also offers more advanced options.


### Command Line Help

    usage: client.py [-h] [--port PORT] [--address IP] [--command CMD] [--directory DIR]
                  [--file DOF] [--no-keep-alive]
    

    Split client binary book by chapters.

    positional arguments:
    	(filename or directory)               .* file(s) to be played

    optional arguments:
      -h,      --help        	    show this help message and exit.
      -p PORT, --port       PORT  port number to listen up (default: 3030)
      -a IP,   --address    IP	  address number to listen up (default: 127.0.0.1)
      -f DOF,  --file       DOF   directory to binary file(s) or binary file
      -c STR,  --command    CMD   customize chapter command (see README)
      -e EXT,  --extension  EXT   define files extension (default: /*.mp3)
      --no-keep-alive             connections are considered persistent unless a --no-keep-alive is included

  

#### Chapter command

You can customize the chapter command with `--command CMD` where `CMD` is a valid python [format string](http://docs.python.org/library/stdtypes.html#string-formatting-operations).

    command arguments:
      list                return playlist now
      next                begin a new sound playback
      play                begin sound playback
      stop                temporarily stop playback of all sound channels
      noow                return the music name
      rewind              restart music
      play_music          play music by identificator

  

### Examples

Play file (you can also drag one .* files onto `client.py`):

    python client.py -f  Led_Zeppelin-Stairway_To_Heaven.mp3

Play folder file(s) no persistent connections:

    python client.py -f ~/Music/Beatles/The_White_Album/ --no-keep-alive

Get attually server playlist:

    python client.py -c list

Force server port and submit multiple file(s):

    python client.py -d ~/Music/Beatles/The_White_Album/ -p 3035


## Server usage

There is a way to use this script:

1. Using the command line which also offers a port options.

### Command Line Help

    usage: server.py [-h] [--port PORT] [--directory DIR]
    
    optional arguments:
      -h, --help                       show this help message and exit.
      -p PORT, --port            PORT  port number to listen up
      -d DIR,  --directory       DIR   binary(s) storage folder (default: ../arquivos/)



### Examples

Default:

    python server.py

Server socket change, modify storage folder:

    python server -p 3030 -d ../arquivos/


