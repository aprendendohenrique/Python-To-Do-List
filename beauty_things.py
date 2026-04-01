colors = {'none': '\033[m', 'white': '\033[30m', 'red': '\033[31m',
          'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
          'purple': '\033[35m', 'cyan': '\033[36m', 'gray': '\033[37m'}

def text_color(txt='', color='\033[m'):
    """
    -> It colors the text
    :param txt: the str to be colored
    :param color: the color
    :return: the colored text string
    """
    return f'{color}{txt}{colors['none']}'

def title(txt='', char='-'):
    """
    -> It makes the title
    :param txt: the title text
    :param char: the character surrounding the title
    :return: the title string
    """

    return f'{char * 38}\n{txt.center(38)}\n{char * 38}'

def list_enumerate(txt_list):
    """
    -> It enumerate your phrases
    :param txt_list: is the list of your phrases, e.g. ['Add', 'Exit', 'Stop', 'Wait']
    :return: the enumerated list string:
    1 - Add
    2 - Exit
    3 - Stop
    4 - Wait
    """
    return_txt = ''
    for c, l in enumerate(txt_list):
        if c < len(txt_list)-1:
            return_txt += f'{c+1} - {l}\n'
        else:
            return_txt += f'{c + 1} - {l}'
    return return_txt