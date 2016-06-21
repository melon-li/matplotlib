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


# fig, left_axe = plt.subplots(nrows=1, ncols=1, figsize=(12, 9))
fig, left_axe = plt.subplots(nrows=1, ncols=1)
right_axe = left_axe.twinx()
xlsx_path = "./data/sram-filesize.xls"


def main():
    x_max_len = 100
    gar_xlsx = xlrd.open_workbook(xlsx_path)
    oneeth_sheet = gar_xlsx.sheet_by_index(0)
 
    #first picture
    #get 0th col data, from 2th row to end    
    x = oneeth_sheet.col_values(0, 2, x_max_len)
#     x = np.array(x)
#     print x

 
    sram_size = oneeth_sheet.col_values(1, 2, x_max_len)
    sinet_rate = oneeth_sheet.col_values(2, 2, x_max_len)
    opc_rate = oneeth_sheet.col_values(3, 2, x_max_len)
    

    left_axe.plot(x, sinet_rate, '-o', color='pink', linewidth=2, label='SINET_Rate')
    left_axe.plot(x, opc_rate, '-<', color='red', linewidth=2, label='OPC_Rate')
    right_axe.plot(x, sram_size, '->', color='lightgreen', linewidth=2, label='SINET_SRAM Size')
    
    left_axe.set_xlabel('File Size(packet number)')
    left_axe.set_ylabel('Router Rate(GB/s)')
    right_axe.set_ylabel('SRAM Size(MB)')
    left_axe.set_xlim(1, x[len(x)-1])
    right_axe.set_xlim(1, x[len(x)-1])
#     left_axe.set_yticks(ra0, int(rate[len(rate)-1])))
    left_axe.set_xticks(range(1, int(x[len(x)-1]), 2))

    left_axe.legend(loc=2, fontsize=10)
    right_axe.legend(loc=9, fontsize=10)
    left_axe.grid(True)
    
# 
    plt.show()

if __name__ == "__main__":
    sys.exit(main())