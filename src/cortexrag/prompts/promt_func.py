from cortexrag.prompts.base_prompts import EN_TOPIK_PROMPT, RU_TOPIK_PROMPT, RU_RESEARCH_PROMPT, EN_RESEARCH_PROMPT


def get_topik_prompt(lang: str):
    if lang == 'en':
        return EN_TOPIK_PROMPT
    elif lang == 'ru':
        return RU_TOPIK_PROMPT
    else:
        raise ValueError('Language not supported, ru, en modes available')

def get_research_prompt(lang: str):
    if lang == 'en':
        return EN_RESEARCH_PROMPT
    elif lang == 'ru':
        return RU_RESEARCH_PROMPT
    else:
        raise ValueError('Language not supported, ru, en modes available')
