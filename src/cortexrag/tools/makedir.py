import os


from cortexrag.state import Topik, WorkerInput



def makedir(name: str):
    try:
        os.makedirs(f'storage/{name}', exist_ok=True)
    except Exception as e:
        print(f'[UNK] {e}')

def make_all_dir(state: Topik):
    dirs = state.main_topics
    for dir in dirs:
        makedir(dir)