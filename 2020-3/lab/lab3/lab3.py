import qiskit
import numpy as np

def inv_media(vetor):
    mean = np.mean(vetor)
    inv_media = [2*mean - elem for elem in vetor]
    return inv_media

def qinv_media(n):
  
    q = qiskit.QuantumRegister(n, name = 'q')
    circuito = qiskit.QuantumCircuit(q)

    for qu in range(n):
        circuito.h(qu)

    for qu in range(n):
        circuito.x(qu)
    
    circuito.h(n-1)
    circuito.mct(list(range(n-1)), n-1)
    circuito.h(n-1)

    for qu in range(n):
        circuito.x(qu)

    for qu in range(n):
        circuito.h(qu)
    return circuito

def oraculo_trivial(n, k):
    circuito_oraculo = {}
    return circuito_oraculo

def grover(oraculo):
    k = {}
    return k
