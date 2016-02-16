#coding:utf-8
'''
Created on 2015年8月13日

@author: melon
'''
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from  matplotlib.ticker import MultipleLocator, FormatStrFormatter
import os
import fnmatch
from matplotlib.font_manager import FontProperties
from matplotlib.lines import lineStyles
from matplotlib.pyplot import gca
from pprint import pprint
xlsx_path = "./data/packet_loss.xls"

def trim_blank(x, y):
    index = index_old = 0
    while index < len(y):
        try:
            float(y[index])
            float(x[index])
            index_old = index
            index += 1
        except ValueError: 
            x.pop(index)
            y.pop(index)
            index = index_old
    return (x, y)

if __name__ == '__main__':
    x_max_len = 105
    gar_xlsx = xlrd.open_workbook(xlsx_path)
    gar_sheet0 = gar_xlsx.sheet_by_index(0)
     
    x = gar_sheet0.col_values(1, 1, x_max_len)
    x = [int(v[:-1]) for v in x if v]
    x = [(v*8)/1000.0 for v in x]
    y = gar_sheet0.col_values(2, 1, len(x)+1)
    (data_1kbps_x, data_1kbps_y) = trim_blank(x, y)
    data_1kbps_y =[v*100 for v in data_1kbps_y]
    data_1kbps_x = np.array(data_1kbps_x)
    data_1kbps_y = np.array(data_1kbps_y)
#     print len(data_1kbps_x), len(data_1kbps_y)

#     
    x = gar_sheet0.col_values(5, 1, x_max_len)
    x = [int(v[:-1]) for v in x if v]
    x = [(v*8)/10000.0 for v in x]
    y = gar_sheet0.col_values(6, 1, len(x)+1)
    (data_10kbps_x, data_10kbps_y) = trim_blank(x, y)
    data_10kbps_y =[v*100 for v in data_10kbps_y]
    data_10kbps_x = np.array(data_10kbps_x)
    data_10kbps_y = np.array(data_10kbps_y)
     
    x = gar_sheet0.col_values(9, 1, x_max_len)
    x = [int(v[:-2]) for v in x if v]
    x = [(v*8)/100.0 for v in x]
    y = gar_sheet0.col_values(10, 1, len(x)+1)
    (data_100kbps_x, data_100kbps_y) = trim_blank(x, y)
    data_100kbps_y =[v*100 for v in data_100kbps_y]
    data_100kbps_x = np.array(data_100kbps_x)
    data_100kbps_y = np.array(data_100kbps_y)
#     print(data_100kbps_x)
#     print(data_100kbps_y)
     
    x = gar_sheet0.col_values(13, 1, x_max_len)
    x = [int(v[:-2]) for v in x if v]
    x = [(v*8)/1000.0 for v in x]
    y = gar_sheet0.col_values(14, 1, len(x)+1)
    (data_1mbps_x, data_1mbps_y) = trim_blank(x, y)
    data_1mbps_y =[v*100 for v in data_1mbps_y]
    data_1mbps_x = np.array(data_1mbps_x)
    data_1mbps_y = np.array(data_1mbps_y)
#     print(data_1mbps_x)
#     print(data_1mbps_y)
     
    x = gar_sheet0.col_values(17, 1, x_max_len)
    x = [int(v[:-2]) for v in x if v]
    x = [(v*8)/10000.0 for v in x]
    y = gar_sheet0.col_values(18, 1, len(x)+1)
    (data_10mbps_x, data_10mbps_y) = trim_blank(x, y)
    data_10mbps_y =[v*100 for v in data_10mbps_y]
    data_10mbps_x = np.array(data_10mbps_x)
    data_10mbps_y = np.array(data_10mbps_y)

    # the main axes is subplot(111) by default
    plt.plot(data_1kbps_x, data_1kbps_y, color='#1f77b4', linestyle='-', linewidth=1.5, label='1Kbps')
    plt.plot(data_10kbps_x, data_10kbps_y, color='#aec7e8', linestyle='-.', linewidth=2, label='10Kbps')
    plt.plot(data_100kbps_x, data_100kbps_y, color='#ff7f0e', linestyle='--', linewidth=2, label='100Kbps')
    plt.plot(data_1mbps_x, data_1mbps_y, color='red', linestyle=':', linewidth=2, label='1Mbps')
    plt.plot(data_10mbps_x, data_10mbps_y, color='#2ca02c', linestyle='-', marker='.', linewidth=2, label='10Mbps' )
#     plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
    plt.xlim(0,9)
    plt.ylim(0,90)
    plt.xlabel('Send Rate (Times)')
    plt.ylabel('Packet Loss Rate (%)')
    plt.legend(loc=5, fontsize=10)
#     plt.title('Gaussian colored noise')
    
    
    # this is another inset axes over the main axes
    a = plt.axes([0.42, 0.4, .2, .2], axisbg='w')
    plt.plot(data_1kbps_x, data_1kbps_y, color='#1f77b4', linestyle='-', linewidth=1.5)
    plt.plot(data_10kbps_x, data_10kbps_y, color='#aec7e8', linestyle='-.', linewidth=2)
    plt.plot(data_100kbps_x, data_100kbps_y, color='#ff7f0e', linestyle='--', linewidth=1.5)
    plt.plot(data_1mbps_x, data_1mbps_y, color='red', linestyle=':', linewidth=2)
    plt.plot(data_10mbps_x, data_10mbps_y, color='#2ca02c', linestyle='-', marker='.', linewidth=1.5 )
#     plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
    plt.xlim(2.01,2.11)
    plt.ylim(42.5,45.5)
    plt.title('Zoom to rectangle', fontsize=10)
#     plt.xlim(0, 0.2)
    plt.xticks([])
    plt.yticks([])
    
    plt.show()    
