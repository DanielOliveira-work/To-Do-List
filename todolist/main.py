import defs

lista = []
task = {}

defs.lines()
print('To Do List'.center(30)) #CENTRALIZAR
defs.lines()

loop = True
while loop:
    defs.menu()
    defs.lines()
    while True:
        try:
            option = int(input('Select the desired option: '))
            break
        except ValueError:
            print('Please, enter a valid value in the menu!')
    match option:
        case 1: #Add task
            add_task = True
            while add_task:
                name = input('Enter the name of the desired task: ').title().strip()
                status = 'Pending'
                for index, value in enumerate(lista):
                    if value["task_name"] == name:
                        print('A task with this name already exists. If you want to change the status, select option 3 from the menu.')
                        defs.lines()
                        add_task = False
                        break
                else:
                    task = {
                        "task_name": name,
                        "status": status
                    }
                    lista.append(task)
                    last = lista[-1]
                    print(f'Task {last["task_name"]} with status {last["status"]} added successfully')
                    defs.lines()
                    add_task = False
        case 2: #Change Status
            if defs.void_list(lista):
                defs.lines()
                continue
            else:
                defs.void_list(lista)
                while_2 = True
                while while_2:
                    names = [itens["task_name"] for itens in lista]
                    print('->', ",".join(names))
                    select_task = input('Which task do you want to change the status of? ').title()
                    for name_tasks in lista:
                        if name_tasks['task_name'] == select_task:
                            while True:
                                option_status = int(input('For pending task, type "1" \nFor complete task, type "2" \n-> '))
                                if option_status not in [1, 2]:
                                    print('Invalid option')
                                else:
                                    break
                            name_tasks['status'] = defs.status(option_status)
                            print(f'The status of task {name_tasks["task_name"]} updated to {name_tasks["status"]} successfully!')
                            defs.lines()
                            while_2 = False
                            break
                    else:
                        print(f'Task {select_task} does not exist in you taks list.')
                        while True:
                            return_menu = input('Do you want to return to the main menu? \nYes or No: ').upper()[0]
                            if return_menu == 'Y':
                                while_2 = False
                                break
                            elif return_menu == 'N':              
                                break
                            else:
                                print('Invalid option!!!')
        case 3: #Delete task
            if defs.void_list(lista):
                defs.lines()
                continue
            else:
                print("Task list \n-> ", ",".join([itens["task_name"] for itens in lista]))
                option_delete = input('Enter the name of the task you want to delete:').title()
                for index, value in enumerate(lista):
                    if value["task_name"] == option_delete:
                        del lista[index]
                        print('Deleted task')
                        defs.lines()
                        break
                    else:
                        print(f"There is no taks {option_delete} in your list.")
                        defs.lines()
        case 4: #print task list
            if defs.void_list(lista):
                defs.lines()
                continue
            else:
                print(f'Here is your complete to-do list \n-> {",".join([tasks["task_name"] for tasks in lista])}')
                defs.lines()
        case 5: #Close program
            print('Closing program...')
            loop = False
            break   
        case _:
            print('Invalid option')
            defs.lines()     