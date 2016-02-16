#!/usr/bin/python
#coding:utf-8
'''
Created on 2016年1月28日

@author: melon
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


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
xlsx_path = "./data/tc.xls"


def main():
    x_max_len = 100
    gar_xlsx = xlrd.open_workbook(xlsx_path)
    oneeth_sheet = gar_xlsx.sheet_by_index(0)
    meth_sheet = gar_xlsx.sheet_by_index(1)
 
    #first picture
    #get 0th col data, from 2th row to end    
    x = oneeth_sheet.col_values(0, 2, x_max_len)
    x = [elem for elem in x if not elem%50]
    x = np.array(x)
# #     print(x)
#     #get 1th col data, from 2th row to end    
#     f1_t = oneeth_sheet.col_values(6, 2, x_max_len)
#     f1 = []
#     for elem in f1_t:
#         if type(elem) != float and  elem.replace(u'\u2212', '-'):
#             elem = Decimal(elem.replace(u'\u2212', '-').replace('$', ''))
# #             print elem
#         f1.append(elem)
#     f1 = np.array(f1)
# #     print(f1)
#     #get 2th col data, from 2th row to end    
    f2_t = oneeth_sheet.col_values(6, 2, x_max_len)
    f2 = []
    for elem in f2_t:
        if type(elem) != float and  elem.replace(u'\u2212', '-'):
            elem = Decimal(elem.replace(u'\u2212', '-').replace('$', ''))
#             print elem
        f2.append(elem)
    f2 = [elem for i,elem in enumerate(f2) if not i%5]
#     print(int(f2[3]))
#     f2 = [int(elem) for i,elem in enumerate(f2) if not i%5]
    f2 = np.array(f2)
# #     print(f2)
#     #get 3th col data, from 2th row to end, cpu usage is 1.8%, cpu is idle 
    y1 = oneeth_sheet.col_values(4, 2, x_max_len)
    y1 = [elem for i,elem in enumerate(y1) if not i%5]
    
    y1 = np.array(y1)
#     print(y1)
    #get 4th col data, from 2th row to end , cpu usage is 14.2% cpu is busy?   
#     y2 = oneeth_sheet.col_values(4, 2, x_max_len)
#     y2 = [elem for i,elem in enumerate(y2) if not i%5]
#     y2 = np.array(y2)
#     print(y2)
    
#     axes[0].plot(x, f1)
    axes[0].plot(x, f2, color='lightgreen',
                linestyle='--', linewidth=1.5, label='y = ax + bx')
    axes[0].plot(x, y1, 'o', color='pink', linewidth=2, label='measured value')
#     axes[0].plot(x, y2, '>', color='lightblue',linewidth=2, label='When CPU is Busy')
#     axes[0].set_xlabel('The number of TC entries')
    axes[0].set_xlabel('TC-HTB class number per emulation node')
    axes[0].set_ylabel('Processing delay(ms)')
    axes[0].legend(loc=9, fontsize=10)
    axes[0].grid(True)
    
    #Second Picure
    #0th col, nodes num
    x = meth_sheet.col_values(0, 13, x_max_len)
    #1th col, tc_fixed_num = 4
    num4_y = meth_sheet.col_values(1, 13, x_max_len)
    num4_f = meth_sheet.col_values(2, 13, x_max_len)
#     #2th col, tc_fixed_num = 5
#     num5_y = meth_sheet.col_values(2, 13, x_max_len)
    #3th col, tc_fixed_num = 10
    num10_y = meth_sheet.col_values(3, 13, x_max_len)
    #5th col, tc_fixed_num = 15
    num15_y = meth_sheet.col_values(5, 13, x_max_len)
    num15_f = meth_sheet.col_values(6, 13, x_max_len)
    #7th col, tc_fixed_num = 20
    num20_y = meth_sheet.col_values(7, 13, x_max_len)
#  
    #9th col, tc_fixed_num = 25
    num25_y = meth_sheet.col_values(9, 13, x_max_len)
    num25_f = meth_sheet.col_values(10, 13, x_max_len)
    #10th col, iptable fixed num = 30
    num30_y = meth_sheet.col_values(11, 13, x_max_len)
# 
    axes[1].plot(x, num4_f, color='k',
              linestyle='--', linewidth=1.0, label='y = ax + b')    
    axes[1].plot(x, num4_y, '8',color='magenta',
                  linewidth=1.5, label='TC-HTB class number per node = 4')
# #     axes[1].plot(x, num5_y, 'ro',color='lightgreen',
# #                   linewidth=1.5, label='inserted entries = 4')
#     axes[1].plot(x, num10_y, 'ro',color='lightgreen',
#                   linewidth=1.5, label='inserted entries = 10')
    axes[1].plot(x, num15_y, '>',color='g',
                  linewidth=1.5, label='TC-HTB class number per node = 15')
    axes[1].plot(x, num15_f, color='k',
                    linestyle='--', linewidth=1)
#     axes[1].plot(x, num20_y, 'ro',color='lightgreen',
#                   linewidth=1.5, label='inserted entries = 20')
    axes[1].plot(x, num25_y, '*',color='r',
                  linewidth=1.5, label='TC-HTB class number per node = 25')
    axes[1].plot(x, num25_f, color='k',
                linestyle='--', linewidth=1)
#     axes[1].plot(x, num30_y, '*',color='r',
#                   linewidth=1.5, label='inserted entries = 30')
    axes[1].set_xlabel('Emualtion nodes number per physical node')
#     axes[1].set_ylabel('Updating link characteristics delay(ms)')
    axes[1].set_ylabel('Processing delay(ms)')
    axes[1].legend(loc=9, fontsize=10)
    axes[1].set_xticks(range(0, 110, 10))
    axes[1].set_xlim(0, 40)
    axes[1].set_ylim(0,1100)
    axes[1].grid(True)

# fill with colors
# colors = ['pink', 'lightblue', 'lightgreen']
# for bplot in (bplot1, bplot2):
#     for patch, color in zip(bplot['boxes'], colors):
#         patch.set_facecolor(color)
#  
# # adding horizontal grid lines
# for ax in axes:
#     ax.yaxis.grid(True)
#     ax.set_xticks([y+1 for y in range(len(all_data))], )
#     ax.set_xlabel('xlabel')
#     ax.set_ylabel('ylabel')
# 
# # add x-tick labels
# plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
#          xticklabels=['x1', 'x2', 'x3', 'x4'])
# 
    plt.show()

if __name__ == "__main__":
    sys.exit(main())