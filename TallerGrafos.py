import networkx as nx #Para usar grafos
import matplotlib.pyplot as plt
import numpy as np #Para uso de matrices
Grafo = nx.DiGraph() #Grafo dirigido
Grafo.add_node(1) #Defino los nodos
Grafo.add_node(2)
Grafo.add_node(3)
Grafo.add_node(4)
Grafo.add_node(5)
Grafo.add_edge(1,2) #Defino los arcos
Grafo.add_edge(1,4)
Grafo.add_edge(1,5)
Grafo.add_edge(3,1)
Grafo.add_edge(3,3)
Grafo.add_edge(4,3)
Grafo.add_edge(5,1)
def MostrarMatAdy():
    Matriz = nx.to_numpy_matrix(Grafo)
    print("Matriz de adyacencia\n---------------------")
    print(Matriz)
MostrarMatAdy()
def menu():
    print("\tMENU\n\t----")
    print("1) Agregar arco")
    print("2) Eliminar arco")
    print("3) Consultar arco")
    print("4) Listar arcos")
    print("5) Salir")
    resp = int(input("Elija una opción: "))
    return resp
def AgregarArco():
    print("Ingrese el vértice inicial del arco a agregar:")
    vert_ini=int(input())
    print("Ingrese el vértice final del arco a agregar:")
    vert_fin=int(input())
    if vert_ini>=1 and vert_fin>=1 and vert_ini<=5 and vert_fin<=5:
        Grafo.add_edge(vert_ini,vert_fin)
        MostrarMatAdy()
    else:
        print("Los vértices ingresados no pertenecen al grafo")
        AgregarArco()
def EliminarArco():
    print("Ingrese el vértice inicial del arco a eliminar:")
    vert_ini=int(input())
    print("Ingrese el vértice final del arco a eliminar:")
    vert_fin=int(input())
    if vert_ini>=1 and vert_fin>=1 and vert_ini<=5 and vert_fin<=5:
        Grafo.remove_edge(vert_ini,vert_fin)
        MostrarMatAdy()
    else:
        print("Los vértices ingresados no pertenecen al grafo")
        EliminarArco()
def ConsultarArco():
    print("Ingrese el vértice inicial del arco a consultar:")
    vert_ini=int(input())
    print("Ingrese el vértice final del arco a consultar:")
    vert_fin=int(input())
    arcos = Grafo.edges() #Lista de arcos del grafo
    if vert_ini>=1 and vert_fin>=1 and vert_ini<=5 and vert_fin<=5:
        if (vert_ini,vert_fin) in arcos:
            print("Existe arco")
        else:
            print("No existe arco")
    else:
        print("Los vértices ingresados no pertenecen al grafo")
        ConsultarArco()
def ListarArco():
    print(Grafo.edges())
while True:
    opc = menu()
    if opc==1:
        AgregarArco()
    elif opc==2:
        EliminarArco()
    elif opc==3:
        ConsultarArco()
    elif opc==4:
        ListarArco()
    elif opc==5:
        break
    else:
        print("No has seleccionado una opción correcta.")
