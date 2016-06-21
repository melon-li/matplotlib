#!/usr/bin/python
#coding:utf-8
'''
Created on 2016年6月17日

@author: Melon Li
'''
import xlrd
import os
import sys
import fnmatch
import numpy as np
from decimal import  Decimal
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.font_manager
from  matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.font_manager import FontProperties
from matplotlib.lines import lineStyles
from matplotlib.pyplot import gca


# fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 9))
fig, axes = plt.subplots(nrows=1, ncols=1)
data_path = "./data/writecache-usage.txt"


def main():
    wc_list = []
    avg = []
    with open(data_path, 'r') as wcf:
        buf = wcf.readline()
        while(buf != ""):
            avg.append(int(buf))
            if len(avg) == 20000:
                wc_list.append(sum(avg)/len(avg))
                avg = []
            buf = wcf.readline()
    
    x = range(0, len(wc_list))
    axes.plot(x, wc_list, '-o',  color='lightgreen',linewidth=1.5)
#     axes[0].plot(x, y2, '>', color='lightblue',linewidth=2, label='When CPU is Busy')
    axes.set_xlabel('Time')
    axes.set_ylabel('Number of Writecache used')
#     axes.set_xlim(0, x[len(x)-1])
#     max_y = max(bf_sram[len(bf_sram)-1], opc_sram[len(opc_sram)-1])
#     axes.set_ylim(0,max_y)
#     axes.set_xticks(range(0, int(x[len(x)-1]), int(x[len(x)-1]))/10)
#     axes.set_yticks(range(0, int(max_y), 100))
    axes.legend(loc=9, fontsize=10)
    axes.grid(True)
    
# 
    plt.show()

if __name__ == "__main__":
    sys.exit(main())