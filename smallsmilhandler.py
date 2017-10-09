#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.list = []

    def startElement(self, name, attrs):
        dic = {}

        if name == 'root-layout':
            dic['name'] = name
            dic['width'] = attrs.get('width')
            dic['height'] = attrs.get('height')
            dic['background-color'] = attrs.get('background-color')
            self.list.append(dic)
        if name == 'region':
            dic['name'] = name
            dic['id'] = attrs.get('id', "")
            dic['top'] = attrs.get('top', "")
            dic['bottom'] = attrs.get('bottom', "")
            dic['left'] = attrs.get('left', "")
            dic['right'] = attrs.get('right', "")
            self.list.append(dic)
        elif name == 'img':
            dic['name'] = name
            dic['src'] = attrs.get('src', "")
            dic['region'] = attrs.get('region', "")
            dic['begin'] = attrs.get('begin', "")
            dic['dur'] = attrs.get('dur', "")
            self.list.append(dic)
        elif name == 'audio':
            dic['name'] = name
            dic['src'] = attrs.get('src', "")
            dic['begin'] = attrs.get('begin', "")
            dic['dur'] = attrs.get('dur', "")
            self.list.append(dic)
        elif name == 'textstream':
            dic['name'] = name
            dic['src'] = attrs.get('src', "")
            dic['region'] = attrs.get('region', "")
            self.list.append(dic)

    def get_tags(self):
        return(self.list)

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.list)
