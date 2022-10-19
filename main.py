
from listaLigada import ListaLigada


def teste_adiciona_comeco(name):
    lista_ligada = ListaLigada()
    lista_ligada.adiciona_fim('Bruno')
    lista_ligada.adiciona_comeco('Bruno Lucas')
    lista_ligada.adiciona_posicao('Lucas',1)
    lista_ligada.adiciona_fim('Bruno')
    lista_ligada.remover_todos_elementos('Lucas')

  
    
    
    
   # lista_ligada.remover_comeco()
    print(lista_ligada)

if __name__ =='__main__':
    teste_adiciona_comeco('') 