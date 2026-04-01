def int_checker(txt=''):
    """
    -> Check if the typed number is integer
    :param txt: is the str that will be used in the input
    :return: the integer number
    """
    num = None
    while True:
        try:
            num = int(input(txt).strip())
        except KeyboardInterrupt:
            print('\033[33m\nThe user chose to not answer\033[m')
            num = 5
            break
        except:
            print('\033[31mPlease type a valid integer number\033[m')
        else:
            break
    return num

def list_bound(lst, opt=1):
    if len(lst) >= opt  > 0:
        return True
    else:
        return False