#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import json
from urllib.request import urlretrieve

if len(sys.argv) != 2:
    sys.exit("  Usage: python3 karaoke.py file.smil")
try:
    open(sys.argv[1])
except FileNotFoundError:
    sys.exit('  This file not found, try again')


class KaraokeLocal(SmallSMILHandler):
    def __init__(self):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(sys.argv[1]))
        self.lista = sHandler.get_tags()

    def __str__(self):
        liststr = ''
        for etiquetasD in self.lista:
            liststr += etiquetasD['name']
            for atribt in etiquetasD:
                if etiquetasD[atribt] != "" and atribt != 'name':
                    liststr += "\t" + atribt + '="' + etiquetasD[atribt] + '"'
            liststr += "\n"
        return(liststr)

    def to_json(self, fichsmil, fichjson=''):
        if fichjson == '':
            fichjson = fichsmil.split('.')[0] + '.json'
        with open(fichjson, 'w') as fijson:
            json.dump(self.lista, fijson)

    def do_local(self):
        for etiquetasD in self.lista:
            for atribt in etiquetasD:
                if etiquetasD[atribt][0:7] == 'http://':
                    long_atrib = etiquetasD[atribt]
                    short_atrib = etiquetasD[atribt].split('/')[-1]
                    urlretrieve(long_atrib, short_atrib)
                    etiquetasD[atribt] = short_atrib

if __name__ == "__main__":
    objeto = KaraokeLocal()
    print(objeto)
    objeto.to_json(sys.argv[1])
    objeto.do_local()
    objeto.to_json(sys.argv[1], 'local.json')
    print(objeto)
