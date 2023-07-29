"""CoderEval API

Usage:
    from HumanEvalX import HumanEvalX
    
    config = json.load(open('humanevl_api_config.json', 'r', encoding='utf-8'))
    # Or build a config object
    
    s = HumanEvalX(config)  # Server
    
    results_file = 'python t 02 p 095 2023-05-31 14-05-46 506657.jsonl'
    results_json = json.loads('[{}]'.format(','.join(list(line.rstrip() for line in open(results_file, 'r', encoding='utf-8')))))
    
    results = s(results_json)
    
    total = 0
    passed = 0

    for generated_code in results['generated_codes']:
        total = total + 1
        if 'compile' in generated_code\
                and 'stderr' in generated_code['compile']\
                and not generated_code['compile']['stderr']\
                and 'execute' in generated_code\
                and 'stderr' in generated_code['execute']\
                and not generated_code['execute']['stderr']:
            # has no err in compiling stage
            # has no err in execution stage
            passed = passed + 1

    f'{passed}/{total}={passed/total}'
    
    
The structure of the results (showing in yamal style):
results:
    generated_codes:
    -
        task-id: 0
        generation:
        prompt:
        testing_code:
        compile:
            stderr
        execute:
            stderr
"""
import json
import requests


class CoderEval:
    def __init__(self, config: dict):
        self.config = config
        self.id = 0
        pass

    def __call__(self, samples: json, timeout: int=8) -> json:
        """Send evaluation request to CoderEval REST API Server
        
        Keyword arguments:
        timeout -- for one sample
        """
        self.id += 1

        content = json.dumps({
            'api_version': self.config['api_version'],
            'api_type': self.config['api_type'],
            'id': self.id,
            'api_key': self.config['api_key'],
            'samples': samples
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
            return json.loads(response.text)
