"""CodeGeeX API V2

For "1.x.x.x", return string; for "2.x.x.x", return json.

For "2.x.x.x", verbose=true means more info will be printed out to the
server's stdout (not return to client).

Uage:
    from codegeex_api import CodeGeeX
    
    codegeex_api_config =
            json.load(open('codegeex_api_config.json', 'r', encoding='utf-8'))
    # Or build a config object
    
    m = CodeGeeX(codegeex_api_config)  # model
    
    m_return = m(PROMPT)
    
    m_return = m(PROMPT, temperature=0.2, top_p=0.95)
    
    generated_code = m_return['stdout'][0]

Note:
    CodeGeeX's code sometimes uses <|endoftext|> .
    Use replace() to clean up, e.g.:
        generated_code.replace('<|endoftext|>', '')
"""
import json
import requests
import re


class CodeGeeX:
    def __init__(self, config: dict):
        self.config = config
        self.id = 0
        pass

    def __call__(
            self,
            prompt: str,
            out_seq_length=1024,
            seq_length=2048,
            top_k=0,
            top_p=0.95,
            temperature=0.8,
            micro_batch_size=1,
            backend='megatron',
            verbose=False) -> str:
        self.id += 1

        content = json.dumps({
            'api_version': self.config['api_version'],
            'api_type': self.config['api_type'],
            'id': self.id,
            'api_key': self.config['api_key'],
            'prompt': prompt,
            'args': {
                'out_seq_length': out_seq_length,
                'seq_length': seq_length,
                'top_k': top_k,
                'top_p': top_p,
                'temperature': temperature,
                'micro_batch_size': micro_batch_size,
                'backend': backend,
                'verbose': verbose
            }
        }).encode(encoding='utf-8')

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.post(
                url=self.config['api_base'], data=content, headers=headers)
        if response.status_code != 200:
            response.raise_for_status()
        else:
            data = json.loads(response.text)['response']
            return data
