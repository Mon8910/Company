#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cal


# In[2]:


cal.call()


# In[3]:


d={'name': 'ahmed'
    , 'gender' : 'male'
    , 'age' : 18 
}
print(d)
print(sorted(d.items()))


print(sorted(d))


# In[4]:


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'A': set(['B', 'C','D']),
         'B': set(['E']),
         'C': set(['D','E']),
         'D': set([ ]),
         'E': set([ ])}

dfs(graph, 'A')


# In[6]:


graph = {'A': set(['B', 'C','D']),
         'B': set(['E']),
         'C': set(['D','E']),
         'D': set([ ]),
         'E': set([ ])}
v=[]
q=[]

def BFS(v,graph,root) :
    v.append(root)
    q.append(root)
    while q :
        R=q.pop(0)
        print(R,end=' ')
        for i in graph[R] :
            if i not in v :
                v.append(i)
                q.append(i)
BFS(v, graph, 'A')                
                
        


# In[20]:


class Myclass :
    def __init__(self):
        print("the class is very good")
    def __del__(self):
        print("the class is deleted")
t1=Myclass()
del t1

