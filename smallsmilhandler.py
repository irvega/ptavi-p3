#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        self.dicroot = {'width':"", 'height':"", 'background-color':""}
        self.dicregion = {'id':"", 'top':"", 'bottom':"", 'left':"", 'right':""}
        self.dicimg = {'src': "", 'region':"", 'begin':"", 'dur':""}
        self.dicaudio = {'src': "",'begin':"",'dur':""}
        self.dictextstream = {'src': "",'region':""}
        self.list = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.dicroot['width'] = attrs.get('width')
            self.dicroot['height'] = attrs.get('height')
            self.dicroot['background-color'] = attrs.get('background-color')
            self.list.append(self.dicroot) 
#            print(self.dicroot)
        if name == 'region':
            self.dicregion['id'] = attrs.get('id', "")
            self.dicregion['top'] = attrs.get('top',"")
            self.dicregion['bottom'] = attrs.get('bottom', "")
            self.dicregion['left'] = attrs.get('left',"")
            self.dicregion['right'] = attrs.get('right',"")
            self.list.append(self.dicregion)
#            print(self.dicregion)
        elif name == 'img':
            self.dicimg['src'] = attrs.get('src', "")
            self.dicimg['region'] = attrs.get('region',"")
            self.dicimg['begin'] = attrs.get('begin', "")
            self.dicimg['dur'] = attrs.get('dur',"")
            self.list.append(self.dicimg)
#            print(self.dicimg)
        elif name == 'audio':
            self.dicaudio['src'] = attrs.get('src', "")
            self.dicaudio['begin'] = attrs.get('begin',"")
            self.dicaudio['dur'] = attrs.get('dur', "")
            self.list.append(self.dicaudio)
#            print(self.dicaudio)
        elif name == 'textstream':
            self.dictextstream['src'] = attrs.get('src', "")
            self.dictextstream['region'] = attrs.get('region',"")
            self.list.append(self.dictextstream)
#            print(self.dictextstream)

    def get_tags(self):
        return(self.list)

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.list)
