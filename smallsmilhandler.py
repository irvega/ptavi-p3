#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.list = []
        self.etiquetas = {'root-layout': ['width', 'height', 'bgcol'],
                          'region':  ['id', 'top', 'bottom', 'left', 'right'],
                          'img': ['src', 'region', 'begin', 'dur'],
                          'audio': ['src', 'begin', 'dur'],
                          'textstream': ['src', 'region']
                         }
    def startElement(self, name, attrs):
        dic = {}

        if name in self.etiquetas:
            dic['name'] = name
            for atrib in self.etiquetas[name]:
                dic[atrib] = attrs.get(atrib, "")
            self.list.append(dic)

    def get_tags(self):
        return(self.list)

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.list)
