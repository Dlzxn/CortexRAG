import os


def makedir(name: str):
    os.makedirs(f'storage/{name}')