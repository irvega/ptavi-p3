#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

if len(sys.argv) != 2:
    sys.exit("  Usage: python3 karaoke.py file.smil")

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    
    parser.parse(open(sys.argv[1]))     
    lista = sHandler.get_tags()
#    print(lista)
    for etiqueta in lista:
        print(etiqueta['name'])
        for atributo in etiqueta:
            print(atributo)
