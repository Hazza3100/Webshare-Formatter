from functools import cache

class Formatter:
    def __init__(self) -> None:
        pass

    @staticmethod
    @cache
    def format(value):
        for proxy in open(value, 'r').read().splitlines():
            data     = proxy.split(':')
            ip       = data[0]
            port     = data[1]
            username = data[2]
            password = data[3]
            with open('formatted.txt', 'a') as f:
                f.write(f'{username}:{password}@{ip}:{port}\n')

Formatter().format('proxy.txt')
