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
from matplotlib.offsetbox import bbox_artist


fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))
xlsx_path_tc = "./data/tc.xls"
xlsx_path_iptables = "./data/iptables.xls"


def main():
    x_max_len = 2000
    gar_xlsx_tc = xlrd.open_workbook(xlsx_path_tc)
    wave_sheet_tc = gar_xlsx_tc.sheet_by_index(4)
 
    #first picture
    #get 0th col data, from 3th row to end    
    x = wave_sheet_tc.col_values(0, 3, x_max_len)
#     x = [elem for elem in x if not elem%50]
    x = np.array(x)

#     #get 3th col data, from 2th row to end, cpu usage is 1.8%, cpu is idle 
    y1 = wave_sheet_tc.col_values(1, 3, x_max_len)
#     y1 = [elem for i,elem in enumerate(y1) if not i%5]
    
    y1 = np.array(y1)
#     print(y1)
    #get 4th col data, from 2th row to end , cpu usage is 14.2% cpu is busy?   
    y2 = wave_sheet_tc.col_values(3, 3, x_max_len)
#     y2 = [elem for i,elem in enumerate(y2) if not i%5]
    y2 = np.array(y2)
#     print(y2)
    
    y3 = wave_sheet_tc.col_values(5, 3, x_max_len)
    y3 = np.array(y3)
    y4 = wave_sheet_tc.col_values(7, 3, x_max_len)
    y4 = np.array(y4)
    y5 = wave_sheet_tc.col_values(9, 3, x_max_len)
    y5 = np.array(y5)
    y6 = wave_sheet_tc.col_values(11, 3, x_max_len)
    y6 = np.array(y6)
#     axes[0].plot(x, f1)
#     axes[0].plot(x, f2, color='lightgreen',
#                 linestyle='--', linewidth=1.5, label='y = ax + bx')
#     axes[0].plot(x, y1, 'o', color='pink', linewidth=2, label='measured value')
    axes[0].plot(x, y1, '-', color='pink', linewidth=2, label='10 ports')
    axes[0].plot(x, y2, '-', color='lightblue',linewidth=2, label='20 ports')
    axes[0].plot(x, y3, '-', color='red',linewidth=2, label='30 ports')
    axes[0].plot(x, y4, '-', color='black',linewidth=2, label='40 ports')
    axes[0].plot(x, y5, '-', color='blue',linewidth=2, label='50 ports')
    axes[0].plot(x, y6, '-', color='g',linewidth=2, label='60 ports')
#     axes[0].plot(x, y2, '>', color='lightblue',linewidth=2, label='When CPU is Busy')
#     axes[0].set_xlabel('The number of TC entries')
    axes[0].set_xlabel('Link Characteristics Experiment Number')
    axes[0].set_ylabel('Processing delay(ms)')
#     axes[0].legend(loc=9, fontsize=10)
    axes[0].legend(loc='upper center', bbox_to_anchor=(0.22, 0.95), fontsize=10)
    axes[0].grid(True)
    
    #Second Picure
    gar_xlsx_iptables = xlrd.open_workbook(xlsx_path_iptables)
    wave_sheet_iptables = gar_xlsx_iptables.sheet_by_index(3)
    
    x = wave_sheet_iptables.col_values(0, 3, x_max_len)
    x = np.array(x)
    
    y1 = wave_sheet_iptables.col_values(1, 3, x_max_len)
#     y1 = [elem for i,elem in enumerate(y1) if not i%5]
    
    y1 = np.array(y1)
#     print(y1)
    #get 4th col data, from 2th row to end , cpu usage is 14.2% cpu is busy?   
    y2 = wave_sheet_iptables.col_values(3, 3, x_max_len)
#     y2 = [elem for i,elem in enumerate(y2) if not i%5]
    y2 = np.array(y2)
#     print(y2)
    
    y3 = wave_sheet_iptables.col_values(5, 3, x_max_len)
    y3 = np.array(y3)
    y4 = wave_sheet_iptables.col_values(7, 3, x_max_len)
    y4 = np.array(y4)
    y5 = wave_sheet_iptables.col_values(9, 3, x_max_len)
    y5 = np.array(y5)
    y6 = wave_sheet_iptables.col_values(11, 3, x_max_len)
    y6 = np.array(y6)
    
    axes[1].plot(x, y1, '-', color='pink', linewidth=2, label='10 ports')
    axes[1].plot(x, y2, '-', color='lightblue',linewidth=2, label='20 ports')
    axes[1].plot(x, y3, '-', color='red',linewidth=2, label='30 ports')
    axes[1].plot(x, y4, '-', color='black',linewidth=2, label='40 ports')
    axes[1].plot(x, y5, '-', color='blue',linewidth=2, label='50 ports')
    axes[1].plot(x, y6, '-', color='g',linewidth=2, label='60 ports')
#     axes[0].plot(x, y2, '>', color='lightblue',linewidth=2, label='When CPU is Busy')
#     axes[0].set_xlabel('The number of TC entries')
    axes[1].set_xlabel('Topology Experiments Number')
    axes[1].set_ylabel('Processing delay(ms)')
    axes[1].legend(loc='upper center', bbox_to_anchor=(0.22, 0.95), fontsize=10)
    axes[1].grid(True)
#     #0th col, nodes num
#     x = meth_sheet.col_values(0, 13, x_max_len)
#     #1th col, tc_fixed_num = 4
#     num4_y = meth_sheet.col_values(1, 13, x_max_len)
#     num4_f = meth_sheet.col_values(2, 13, x_max_len)
# #     #2th col, tc_fixed_num = 5
# #     num5_y = meth_sheet.col_values(2, 13, x_max_len)
#     #3th col, tc_fixed_num = 10
#     num10_y = meth_sheet.col_values(3, 13, x_max_len)
#     #5th col, tc_fixed_num = 15
#     num15_y = meth_sheet.col_values(5, 13, x_max_len)
#     num15_f = meth_sheet.col_values(6, 13, x_max_len)
#     #7th col, tc_fixed_num = 20
#     num20_y = meth_sheet.col_values(7, 13, x_max_len)
# #  
#     #9th col, tc_fixed_num = 25
#     num25_y = meth_sheet.col_values(9, 13, x_max_len)
#     num25_f = meth_sheet.col_values(10, 13, x_max_len)
#     #10th col, iptable fixed num = 30
#     num30_y = meth_sheet.col_values(11, 13, x_max_len)
# # 
#     axes[1].plot(x, num4_f, color='k',
#               linestyle='--', linewidth=1.0, label='y = ax + b')    
#     axes[1].plot(x, num4_y, '8',color='magenta',
#                   linewidth=1.5, label='TC-HTB class number per node = 4')
# # #     axes[1].plot(x, num5_y, 'ro',color='lightgreen',
# # #                   linewidth=1.5, label='inserted entries = 4')
# #     axes[1].plot(x, num10_y, 'ro',color='lightgreen',
# #                   linewidth=1.5, label='inserted entries = 10')
#     axes[1].plot(x, num15_y, '>',color='g',
#                   linewidth=1.5, label='TC-HTB class number per node = 15')
#     axes[1].plot(x, num15_f, color='k',
#                     linestyle='--', linewidth=1)
# #     axes[1].plot(x, num20_y, 'ro',color='lightgreen',
# #                   linewidth=1.5, label='inserted entries = 20')
#     axes[1].plot(x, num25_y, '*',color='r',
#                   linewidth=1.5, label='TC-HTB class number per node = 25')
#     axes[1].plot(x, num25_f, color='k',
#                 linestyle='--', linewidth=1)
# #     axes[1].plot(x, num30_y, '*',color='r',
# #                   linewidth=1.5, label='inserted entries = 30')
#     axes[1].set_xlabel('Emualtion nodes number per physical node')
# #     axes[1].set_ylabel('Updating link characteristics delay(ms)')
#     axes[1].set_ylabel('Processing delay(ms)')
#     axes[1].legend(loc=9, fontsize=10)
#     axes[1].set_xticks(range(0, 110, 10))
#     axes[1].set_xlim(0, 40)
#     axes[1].set_ylim(0,1100)
#     axes[1].grid(True)

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