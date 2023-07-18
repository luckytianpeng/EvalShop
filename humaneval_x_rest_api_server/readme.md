## HumanEval-X REST API Server

The HumanEval-X REST API Server provides convenient access to HumanEval-X benchmark.

### Ref:  
- [HumanEval-X: A new benchmark for Multilingual Program Synthesis](https://github.com/THUDM/CodeGeeX/blob/main/codegeex/benchmark/README.md)


<hr/>

### HTTP authentication  

- api_key: 8EA3D62222ACAA5315A1ED6B3F883  
    Tool: https://acte.ltd/utils/randomkeygen - 256 wep  
- MD5: e4665bcbaa4668d024d22c9b77939797  
    Tool: https://www.md5hashgenerator.com/  

#### E.g.:  

../humaneval_x_api_python/examples/humanevl_x_api_config.json :  
```json
{
  "api_base": "http://127.0.0.1:8088/v2",
  "api_version": "2.1.0.0",
  "api_type": "HumanEval-X-Evaluation",
  "api_key": "8EA3D62222ACAA5315A1ED6B3F883"
}
```

./humaneval_x_rest_api_server_api_keys.json :  
```json
{
  "e4665bcbaa4668d024d22c9b77939797": {
    "email": "<User's email here>"
  }
}
```
