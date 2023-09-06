#!/usr/bin/env python
# coding: utf-8

# # Aula - Python
# 
# ## Fundamentos Básicos

# ### -----
# ### 1. Atribuição e impressão na tela
# ### -----

# In[1]:


a = 51;
print(f"Valor de {a}")
a = 5.1
print(f"Valor de {a}")
a = "teste"
print(f"Valor de {a}")
a = 'teste'
print(f"Valor de {a}")


# In[2]:


# outro exemplo de print
b = 10
print(f"Valor de {a} {b}")
print("Valor de", a, b)


# ### -----
# ### 2. Operações matemáticas básicas
# ### -----

# In[3]:


b = 17
c = 5
print(f"Valor de {c+b}")
print(f"Valor de {c-b}")
print(f"Valor de {c*b}")
print(f"Valor de {b/c}")
print(f"Valor de {round(b/c, ndigits=2)}")
print(f"Valor de {b/c} {b%c}  {b//c}")
print(f"Valor de {4**(0.5)}")


# ### -----
# ### 3. Expressões lógicas
# ### -----

# In[4]:


print(f"Valor de {c == b}")
print(f"Valor de {c > b}")
print(f"Valor de {c >= b}")
print(f"Valor de {c < b}")
print(f"Valor de {c <= b}")
print(f"Valor de {c != b}")
print(f"Valor de {not (c != b)}")

print(f"Valor de {c != b and c < b}")
print(f"Valor de {c != b and c > b}")
print(f"Valor de {c != b or c > b}")


# ### -----
# ### 4. if/else
# ### -----

# In[6]:


c = 5
b = 5

if (c > b):
    d = c + b
    print(f"Resultado: {d}")
elif c == b:
    d = c ** b
    print(f"Resultado {d}")
else:
    d = c - b
    print(f"Resultado: {d}")


# ### -----
# ### 5. Usando bibliotecas do Python
# ### -----

# In[9]:


# biblioteca básica para operações matemáticas
import math as m

print(f"{4**0.5}")
print(f"{m.sqrt(4)}")


# In[11]:


from math import sqrt as raiz
print(f"{raiz(4)}")


# ### -----
# ### 6. Vetores
# ### -----

# In[1]:


### vetores --> numpy
import numpy as np

v1 = np.zeros(3)
print(v1)

v2 = np.ones(3)
print(v2)

v3 = np.arange(5)
print(v3)

v4 = np.arange(2,5)
print(v4)

v5 = np.repeat("teste", 10)
print(v5)


# In[21]:


# cria um vetor entre 0 e 1 com '0.1 saltos'

np.arange(0, 1, 0.1)


# In[10]:


# cria um vetor entre 0 e 10 com incremento de 2
np.arange(0, 10, 2)


# In[4]:


# gerando vetores aleatórios
np.random.randint(1,50,3)


# In[5]:


np.array([1,2,3,4])


# ### -----
# ### 7. Laços
# ### -----

# In[26]:


# estruturas de controle

for i in v4:
    print(f"Valor: {i}")


# In[28]:


for i in np.arange(len(v4)): 
    print(f"Indice: {i} | Valor: {v4[i]}")


# In[12]:


[print(i) for i in v3]


# In[30]:


i = 0
while i < len(v4):
    print(v4[i])
    i += 1


# ### -----
# ### 8. Funções
# ### -----

# In[36]:


# criação de funções
# usando parametros default
def nova_funcao(a, b=1, c=1):
  return (a+b)*c


# In[37]:


print(f"{nova_funcao(5)}")
print(f"{nova_funcao(7,10,7)}")
print(f"{nova_funcao(a = 8, c = 9)}")
print(f"{nova_funcao(a = 7, b = 10, c = 7)}")
#print(f"{nova_funcao(b = 10, c = 7)}")


# In[19]:


# como verificar a utilização de funções: help

help(print)
# ou
get_ipython().run_line_magic('pinfo', 'print')


# In[40]:


# como importar funções de um arquivo

from teste import *

print(f"{soma(5,6)}")
print(f"{subtrai(5,6)}")


# ### -----
# ### 9. Matrizes
# ### -----

# In[27]:


# criando matrizes
# a função reshape transforma um vetor (1xT) em uma matriz (M, N)
np.arange(12) #1x12


# In[8]:


np.arange(12).reshape(4,3) #4x3


# In[11]:


np.arange(12).reshape(4,3).astype(float) #4x3


# In[47]:


m1 = np.zeros(12).reshape(4,3)
print(m1)

m2 = np.arange(12).reshape(4,3)
print(m2)


# In[30]:


# acessando valores na linha 2 e coluna 2
# lembrem-se que o índice começa do valor 0
m2[2,2]


# In[48]:


# recuperando apenas a 1a linha
m2[0, :]


# In[32]:


# recuperando apenas os valores da 1a linha e das 2 primeiras colunas
m2[0, 0:2]


# In[33]:


# recuperando apenas os valores da 1a coluna
m2[:, 0]


# In[51]:


print(m1)
print("----")
print(m2)


# In[53]:


# concatenando duas matrizes
m3 = np.append(m1, m2, axis=1)
m3


# In[43]:


print(f"m1 = {m1.shape}")
print(f"m2 = {m2.shape}")
print(f"m3 = {m3.shape}")


# ### -----
# ### 13. Salvando em arquivos 
# ### -----

# In[54]:


#salvando em arquivo
np.savetxt("teste.csv", m3, delimiter=",")


# In[55]:


#lendo de um arquivo
np.genfromtxt("teste.csv", delimiter=',')


# In[ ]:




