#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import re

argvs = sys.argv
argc = len(argvs)

def convert_decimal(rop3_int):
    if rop3_int == 0:
        return chr(rop3_int)
    tmp = rop3_int
    rtn = ''
    while tmp > 0:
        rtn =  str(tmp % 10) + rtn
        tmp = tmp/10
    return rtn


##
# infile[in]:    hpgl2/pcl file(Note:file should have rop3 command!!)
# outfile[out]:  converted file
# rop3[in]:      rop3 which is used for convert
##
def convert_ROP3(infile,outfile,rop3):
    pattern = "\x1B[\x2A]" + "\d{1,3}" + "\x6F\x6C\x4F"
    infp = open(infile, 'rb')
    outfp = open(outfile, 'wb')
    line = infp.readline()
    changed_rop3 = "\x1B\x2A" + convert_decimal(int(rop3)) + "\x6F\x6C\x4F"
    while line:
        changed_line = re.sub(pattern, changed_rop3, line)
        outfp.write(changed_line)
        line = infp.readline()
    infp.close()
    outfp.close()

if __name__ == '__main__':
    convert_ROP3(argvs[1], argvs[2], argvs[3])
