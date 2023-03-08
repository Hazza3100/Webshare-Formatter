from functools import cache

class Formatter:
    def __init__(self):
        pass

    @staticmethod
    @cache
    def format(value):
        with open(value) as f:
            lines = f.read().split('\n')
        formatted_lines = []
        for line in lines:
            if line.strip():
                ip, port, username, password = line.split(':')
                formatted_line = '{}:{}@{}:{}\n'.format(username, password, ip, port)
                formatted_lines.append(formatted_line)
        with open('formatted.txt', 'w') as f:
            f.writelines(formatted_lines)

Formatter().format('proxy.txt')
