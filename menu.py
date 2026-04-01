from beauty_things import text_color
from beauty_things import colors


def add(tasks, task):
    tasks.append({'task': task, 'done': False})
    return text_color('Task successfully added!', colors['green'])

def task_list(tasks):
    txt = ''
    for c, t in enumerate(tasks):
        txt += f'{c + 1} - {t['task']:<25}'
        if t['done']:
            txt += text_color('done', colors['green'])
        else:
            txt += text_color('undone', colors['gray'])
        if c < len(tasks) - 1:
            txt += '\n'
    return txt

def mark_as_done(tasks, opt):
    tasks[opt - 1]['done'] = True
    return text_color(f'{tasks[opt-1]['task']} is done!', colors['green'])

def remove(tasks, opt):
    t = text_color(f'{tasks[opt-1]['task']} was removed!', colors['red'])
    del tasks[opt - 1]
    return t