# cs_binary

Este repositório contem o código Client-Server desenvolvido para disciplina de Redes de Computadores, do Mestrado em Ciência da Computação - Universidade Federal de São João del Rei 


## Requirements

* [Python](http://www.python.org/download/) (tested with v2.7)
* Tkinter (tested with 8.6)
* [py-game](https://www.pygame.org/wiki/GettingStarted) (v3.6.1)


## Installation

### Windows

1. Install python 2.7.
2. Download pip then [compile](https://bootstrap.pypa.io/get-pip.py) and install.
3. Install package Pygame `py -m pip install -U pygame --user`

### Ubuntu 16.10

1. Install packages: `sudo apt-get install python2.7 python3-pygame`


## Usage

There are three ways to use this script:

1. Drag your `.*` file(s) onto `client.py`.
2. Drag your directory onto `client.py`.
3. Using the command line which also offers more advanced options.


### Command Line Help

    usage: client.py [-h] [--port PORT] [--command "STR"] [--directory DIR]
                  [--file filename] 
    

    Split client binary book by chapters.

    positional arguments:
      filename              .* file(s) to be played

    optional arguments:
      -h, --help            show this help message and exit.
      -p PORT, --port PORT
                            port number to listen up
      --directory BIN       path to binary file(s)
      --command "STR"       customize chapter command (see README)
  

#### Chapter command

You can customize the chapter command with `--command STR` where `STR` is a valid python [format string](http://docs.python.org/library/stdtypes.html#string-formatting-operations).