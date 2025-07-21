def lines():
    """
    - Linhas divisórias // Dividing lines
    """
    print('-' * 30)

def menu():
    """
    - Menu do programa // Program menu
    """
    print('Enter 1 to add a task')
    print('Enter 2 to change the status of a task')
    print('Enter 3 to delete a task')
    print('Enter 4 to print task list')
    print('Enter 5 to exit the program')


def status(cod):
    """
    - Adiciona o status pendente ou completo // Adds pending or complete status
    """
    if cod == 1:
        return 'pending'
    elif cod == 2:
        return 'completed'


def void_list(lista):
    """
    - Verifica se a lista está vazia. Caso esteja, irá informar ao usuário.
      // Checks if the list is empty. If it is, informs the user.
    """
    if not lista:
        print('Void list')
        return True   
    return False