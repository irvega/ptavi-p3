#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)

    if len(sys.argv) != 2:
        sys.exit("  Usage: python3 karaoke.py file.smil")

    parser.parse(open('karaoke.smil'))
    print(sHandler.list)

