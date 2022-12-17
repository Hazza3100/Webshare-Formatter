

class Formatter:
    def __init__(self) -> None:
        pass

    @staticmethod
    def format(value):
        for proxy in open(value, 'r').read().splitlines():
            ip       = proxy.split(':')[0]
            port     = proxy.split(':')[1]
            username = proxy.split(':')[2]
            password = proxy.split(':')[3]
            with open('formatted.txt', 'a') as f:
                f.write(f'{username}:{password}@{ip}:{port}\n')


Formatter().format('proxy.txt')