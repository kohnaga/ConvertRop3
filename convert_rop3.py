#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import re

##
# infile[in]:    hpgl2/pcl file(Note:file should have rop3 command!!)
# rop3[in]:      rop3 which is used for convert
# outfile[out]:  converted file
##ß
def convert_ROP3(infile, rop3, outfile):
    pattern = "\x1B" + "\*" + ".\x6C\x6F"
    infp = open(infile, 'rb')
    outfp = open(outfile, 'wb')
    line = infp.readline()
    while line:
        changed_rop3 = "\x1B\x2A" + chr(rop3) + "\x6C\x6F"
        changed_line = re.sub(pattern, changed_rop3, line)
        outfp.write(changed_line)
        line = infp.readline()
    infp.close()
    outfp.close()