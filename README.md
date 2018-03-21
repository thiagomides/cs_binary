# cs_binary

Este repositório contem o código Client-Server desenvolvido para disciplina de Redes de Computadores, do Mestrado em Ciência da Computação - Universidade Federal de São João del Rei 


## Requirements

* [Python](http://www.python.org/download/) (tested with v2.7)
* [Tkinter](http://www.tkdocs.com/tutorial/install.html) (tested with 8.6)
* [py-game](https://www.pygame.org/wiki/GettingStarted) (v3.6.1)


## Installation

### Windows

1. Install python 2.7.
2. Download pip then [compile](https://bootstrap.pypa.io/get-pip.py) and install.
3. Install package Pygame `py -m pip install -U pygame --user`

### Ubuntu 16.10

1. Install packages: `sudo apt-get install python2.7 python3-pygame`


## Client usage

There are three ways to use this script:

1. Drag your `.*` file(s) onto `client.py`.
2. Drag your directory onto `client.py`.
3. Using the command line which also offers more advanced options.


### Command Line Help

    usage: client.py [-h] [--port PORT] [--address IP] [--command CMD] [--directory DIR]
                  [--file filename] 
    

    Split client binary book by chapters.

    positional arguments:
      filename              .* file(s) to be played

    optional arguments:
      -h, --help            show this help message and exit.
      -p PORT, --port PORT  port number to listen up
      -a IP, --address 		address number to listen up
      --no-keep-alive       connections are  considered persistent unless a --no-keep-alive header is included
      --directory BIN       path to binary file(s)
      --command   STR       customize chapter command (see README)
  

#### Chapter command

You can customize the chapter command with `--command CMD` where `CMD` is a valid python [format string](http://docs.python.org/library/stdtypes.html#string-formatting-operations).

    command arguments:
      list                return playlist now
      next                begin a new sound playback
      play                begin sound playback
      stop                temporarily stop playback of all sound channels
      noow                return the music name
      rewind              restart music

  

### Examples

Play file (you can also drag one .* files onto `client.py`):

    python client.py -f  Led_Zeppelin-Stairway_To_Heaven.mp3

Play folder file(s):

    python client.py -d ~/Music/Beatles/The_White_Album/

Get attually server playlist:

    python client.py -c list

Force server port and submit multiple file(s):

    python client.py -d ~/Music/Beatles/The_White_Album/ -p 3030


## Server usage

There is a way to use this script:

1. Using the command line which also offers a port options.

### Command Line Help

    usage: server.py [-h] [--port PORT] [--address IP] 
    
    optional arguments:
      -h, --help            show this help message and exit.
      -p PORT, --port PORT  port number to listen up
      -a IP, --address 		address number to Listen Up


### Examples

Default:

    python server.py

Server change socket:

    python server -p 3030


