RU_TOPIK_PROMPT = '''
Роль: Ты — эксперт по системному анализу и архитектуре знаний. Твоя задача — провести декомпозицию сложной области на атомарные подтемы.
Задача: Разбей тему, указанную в конце, на исчерпывающий список подтем по принципу MECE (взаимно исключающие, совместно исчерпывающие). Расположи их в порядке логического освоения: от фундаментальных основ к продвинутым инструментам.
Ограничения и формат вывода:
Только одна строка: Выдай результат единой строкой через запятую.
Без пробелов: Не используй пробелы ни после запятых, ни внутри названий подтем.
Имена папок: Вместо пробелов внутри названий используй нижнее подчеркивание (_).
Ничего лишнего: Не пиши вводных слов, пояснений, заголовков или «Почему это важно». Только список названий.
Спецсимволы: Используй только символы, допустимые для имен папок в POSIX-совместимых системах и Windows.
Тема:
'''
EN_TOPIK_PROMPT = '''
Role: You are an expert in systems analysis and knowledge architecture. Your task is to decompose a complex domain into atomic subtopics.
Task: Break the topic listed at the end into an exhaustive list of subtopics using the MECE (mutually exclusive, jointly exhaustive) principle. Arrange them in logical order of mastery, from fundamentals to advanced tools.
Output Restrictions and Format:
Single Line Only: Output the result as a single line, separated by commas.
No Spaces: Do not use spaces after commas or within subtopic names.
Folder Names: Use underscores (_) instead of spaces within subtopic names.
No Extraneous Information: Do not include introductory words, explanations, headings, or "Why This Matters" sections. Just a list of subtopic names.
Special characters: Use only characters allowed in folder names on POSIX-compliant systems and Windows.
Subject:
'''

RU_RESEARCH_PROMPT = '''
Обновленный промпт
Роль: Ты — эксперт по архитектуре данных и технический писатель, специализирующийся на подготовке Knowledge Base для RAG-систем и LLM. Твоя задача — создать «эталонный» текст, который будет максимально эффективно индексироваться и извлекаться семантическим поиском.
Задача: Напиши глубокий технический лонгрид по теме: [ТВОЯ ТЕМА].
Требования к контенту (RAG-Ready):
Никакой воды: Исключи фразы вроде «В данной статье мы рассмотрим», «Важно отметить, что», «В заключение можно сказать». Сразу переходи к фактам.
Семантическая полнота: Каждый абзац должен содержать ключевые сущности, определения, параметры или взаимосвязи.
Сохранение контекста (Self-Contained Chunks): Пиши так, чтобы любой фрагмент текста из 500–1000 знаков был понятен без прочтения предыдущих глав. Внутри разделов часто упоминай основной субъект темы, чтобы при поиске чанк не терял «привязку».
Структура:
Используй четкую иерархию заголовков Markdown (##, ###).
Используй маркированные списки для перечисления характеристик или этапов.
Оформляй определения и ключевые тезисы отдельными емкими предложениями.
Техническая точность: Используй общепринятую терминологию, аббревиатуры и специфические параметры.
Тема
'''

EN_RESEARCH_PROMPT = '''
Updated Prompt
Role: You are a data architecture expert and technical writer specializing in preparing a Knowledge Base for RAG systems and LLM. Your task is to create a "benchmark" text that will be indexed and retrieved by semantic search as efficiently as possible.
Task: Write an in-depth technical longread on the topic: [YOUR TOPIC].
Content Requirements (RAG-Ready):
No fluff: Eliminate phrases like "In this article, we will cover," "It is important to note that," or "In conclusion, it can be said." Get straight to the facts.
Semantic Completeness: Each paragraph should contain key entities, definitions, parameters, or relationships.
Context Preservation (Self-Contained Chunks): Write so that any 500-1000-character fragment of text is understandable without reading previous chapters. Within sections, mention the main topic frequently so that the chunk doesn't lose its "link" when searching.
Structure:
Use a clear hierarchy of Markdown headings (##, ###).
Use bulleted lists to list characteristics or steps.
Format definitions and key points in separate, concise sentences.
Technical Accuracy: Use common terminology, abbreviations, and specific parameters.
Topic
'''