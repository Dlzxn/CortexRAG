try:
    from transformers import pipeline

except Exception as e:
    raise ImportError('To use custom models, type: pip install transformers')


from cortexrag.core import BaseChatModel


class TransformersModel(BaseChatModel):
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model


    def generate(self, message: str, system_prompt = 'You are helpful agent'):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ]
        input_text = self.tokenizer.apply_chat_template(messages,
                                                    tokenize=False,
                                                    add_generation_prompt=True
                                                    )
        inputs = self.tokenizer(input_text, return_tensors="pt").to(self.model.device)
        input_length = inputs.input_ids.shape[1]
        result_tokens = self.model.generate(
            **inputs,
            max_new_tokens=2048,
            do_sample=True,
            temperature=0.4,
            top_p=0.9,
            repetition_penalty=1.1
        )
        result = self.tokenizer.decode(result_tokens[0][input_length:], skip_special_tokens=True)
        print(result)
        return result.strip()
