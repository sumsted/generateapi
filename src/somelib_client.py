import requests

host = 'http://0.0.0.0:8080'


def g(action, *args):
    url = host+'/'+action
    for arg in args:
        url += '/'+str(arg)
    r = requests.get(url)
    return r.json()


def mouse(cheese, trap, cat):
    return g('mouse', cheese, trap, cat)['return_value']


def dog(bone):
    return g('dog', bone)['return_value']


if __name__ == '__main__':
    pass
