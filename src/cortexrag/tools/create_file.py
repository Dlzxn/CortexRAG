


def create_md(path: str, text: str):
    '''
    Создание файла для хранения информации от LLM
    :param path:
    :param text:
    :return:
    '''
    try:
        with open(f'storage/{path}', 'w') as f:
            f.write(text)

    except FileNotFoundError:
        print('\033[31mFile not found\033[0m')

    except FileExistsError:
        print('\033[31mFileExistsError\033[0m')

    except Exception as e:
        print(f'[UNK ERROR] {e}')