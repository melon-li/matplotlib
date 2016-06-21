#!/usr/bin/env python
"""
Draw a network topology 
inputdata:(n1, n2) show the n1 connects n2
Artist                      Melon Li
"""
import networkx as nx
import matplotlib.pyplot as plt
import sys

TP_FILE = './data/topologies/scale-free-50-1.txt'
GROUP_SIZE = 25
G = nx.Graph()

def parse_topology():
    x = []
    y = []
    cnt = 0
    with open(TP_FILE, 'r') as tpf:
        line = tpf.readline()
        cnt = cnt + 1
        while(line !=""):
            if len(line.split('_')) < 3:
                print "line:%s format is error!" % cnt
                line = tpf.readline()
                cnt = cnt + 1
                continue
            n1 = line.split('\t')[0]
            n2 = line.split('_')[2]
            start = n2.find('<')
            while(start > 0):
                end = n2.find('>')
                if end < 1: print "The %s form has error"
                n1_t = int(n1)
                n2_t = int(n2[start+1:end])
#                 if n2_t > n1_t:
                x.append(n1_t)
                y.append(n2_t)
                n2 = n2[end+1:]
                start = n2.find('<')
            line = tpf.readline() 
            cnt = cnt + 1
    print x
    print y
    print "Parse %d lines" % (cnt-1)
    return (x, y)

def add_access_nodes(_x_l, _y_l):
    start = min(min(_x_l), min(_y_l))
    end = max(max(_y_l), max(_x_l))
    x_l = [elem for elem in _x_l]
    y_l = [elem for elem in _y_l]
    access_nodes = set()  
    for i in range(start, end+1):
        if _x_l.count(i) == 1:
            access_nodes.add(i)
            for j in range(0, GROUP_SIZE):
                x_l.append(i)
                y_l.append(len(y_l))
        if _x_l.count(i) == 0 and _y_l.count(i) == 1:
            access_nodes.add(i)
            for j in range(0, GROUP_SIZE):
                x_l.append(i)
                y_l.append(len(y_l))
    print "Access nodes(%d) = %s" % (len(access_nodes),access_nodes)
    return (x_l, y_l)

t = parse_topology()
x_l = t[0]
y_l = t[1]

t2 = add_access_nodes(x_l, y_l)
x_l = t2[0]
y_l = t2[1]

# print "node number = %d" % len(set(x_l).union(set(y_l))) 
# print set(x_l).union(set(y_l))

access_nodes = set()      
for i in range(0, len(x_l)):
    G.add_edge(x_l[i],y_l[i], {})



nx.draw(G, with_labels=True)
plt.show()

