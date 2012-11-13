from sys import exit
import networkx as nx
from random import choice

"""A program to find a Eulerian path through a directed graph"""

# Construct Graph from input (G)

# Uncomment for cut-and-paste input:
# input=eval(raw_input("enter your graph"))
input=G
Graph=nx.DiGraph()
for edge in input:
	Graph.add_edge(edge[0],edge[1], label=edge[2])

n = 0

def in_out_balance(node):
	balance=Graph.in_degree(node) - Graph.out_degree(node)
	return balance
	
def set_semibalanced(node):
	global unbalanced
	global n
	Graph.node[node]['semibalanced'] = 1
	unbalanced = 1
	n = n + 1

def none():
	print "None"
	return None
	exit()

def find_balance(Graph):
	global start
	global finish
	global unbalanced
	unbalanced = 0
	n = 0
	for node in Graph:
		balance = in_out_balance(node)
		if abs(balance) > 1:
			none()
		if abs(balance) == 1:
			set_semibalanced(node)
			if balance == 1:
				finish=node	
			else:
				start=node
		if n > 2:
			none()
	# Connect start and finish if unbalanced
	# Otherwise, pick a random starting point	
	if unbalanced==1:
		Graph.add_edge(finish,start, label=None)
	else:
		start=choice(Graph.nodes())

def euler(Graph):
	global start
	global finish
	find_balance(Graph)
	path=[]
	if nx.is_eulerian(Graph):
		circuit=list(nx.eulerian_circuit(Graph, start))
		for edge in circuit:
			current=Graph.edge[edge[0]][edge[1]]['label']
			if current != None:
				path.append(current)
		if unbalanced==0:
			finish=circuit.pop()[1]
		answer=start, path, finish
		print answer
		
	else: 
		none()

euler(Graph)

# [("a","b",1), ("b","c",2), ("c","a",3)]  - eulerian
# [("a","b",1), ("b","c",2), ("c","a",3), ("c","d",4)] - eulerian +1
# [("a","b",1), ("b","c",2), ("c","a",3), ("c","d",4), ("z","c",5)]
# [("a","b",1), ("b","c",2), ("c","a",3), ("c","d",4), ("d","c",5)] - eulerian
# [("a","b",1), ("b","c",2), ("c","a",3), ("c","d",4), ("x","z",5)] 