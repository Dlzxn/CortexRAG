from pyrag.prompts.base_prompts import EN_TOPIK_PROMPT, RU_TOPIK_PROMPT


def get_topik_prompt(lang: str, topic: str):
    if lang == 'en':
        return EN_TOPIK_PROMPT + f'topic: {topic}'
    elif lang == 'ru':
        return RU_TOPIK_PROMPT + f'Тема: {topic}'
    else:
        raise ValueError('Language not supported, ru, en modes available')
