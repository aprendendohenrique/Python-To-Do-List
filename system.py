from beauty_things import text_color
from beauty_things import title
from beauty_things import colors
from beauty_things import list_enumerate
import data
import checkers
import menu

tasks = data.loading()

print(text_color(title('To-Do List', '='), colors['cyan']))
options = ['Add task', 'List tasks', 'Mark as done', 'Remove task', 'Exit']

while True:
    print(title(list_enumerate(options)))
    option = checkers.int_checker('Your option: ')
    if checkers.list_bound(options, option):
        if option == 5:
            data.saving(tasks)
            break
        elif option == 1:
            print(title(options[option - 1], '='))
            task = str(input('Task: '))
            print(menu.add(tasks, task))
        elif option == 2:
            if checkers.list_bound(tasks):
                print(title(options[option - 1], '='))
                print(menu.task_list(tasks))
            else:
                print(text_color('Add at least one task first!', colors['yellow']))
        elif option == 3:
            if checkers.list_bound(tasks):
                print(title(options[option - 1], '='))
                task_opt = checkers.int_checker('Your option: ')
                if checkers.list_bound(tasks, task_opt):
                    print(menu.mark_as_done(tasks, task_opt))
                else:
                    print(text_color('Please, type a valid option!', colors['yellow']))
            else:
                print(text_color('Add at least one task first!', colors['yellow']))
        elif option == 4:
            if checkers.list_bound(tasks):
                print(title(options[option - 1], '='))
                task_opt = checkers.int_checker('Your option: ')
                if checkers.list_bound(tasks, task_opt):
                    print(menu.remove(tasks, task_opt))
                else:
                    print(text_color('Please, type a valid option!', colors['yellow']))
            else:
                print(text_color('Add at least one task first!', colors['yellow']))
    else:
        print(text_color('Please, type a valid option', colors['yellow']))