from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch


from cortexrag.integration.transformers import TransformersModel
from cortexrag import Engine



def test_transformers(model_name: str = 'Qwen/Qwen2.5-Coder-7B-Instruct'):
    qconfig = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True
    )
    model = AutoModelForCausalLM.from_pretrained(model_name,
                                                 quantization_config=qconfig
                                                 )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = TransformersModel(tokenizer, model)
    engine = Engine(
        topic='Автомобили',
        models=(model, model),
        lang='ru'
    )
    engine.build()
