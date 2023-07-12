## CodeGeeX REST API Server

The CodeGeeX REST API Server provides convenient access to CodeGeeX Code Generation Model.

### Ref:  
- [THUDM/CodeGeeX: CodeGeeX: An Open Multilingual Code Generation Model (KDD 2023)](https://github.com/THUDM/CodeGeeX)


<hr/>

### HTTP authentication  

- api_key: D4B94CC818A3D8A725CCC8FE68B97  
    Tool: https://acte.ltd/utils/randomkeygen - 256 wep  
- MD5: 5c0f6958f8ec27e336a1bd04cb64d9a4  
    Tool: https://www.md5hashgenerator.com/  

#### E.g.:  

../codegeex_api_python/examples/codegeex_server_config.json :  
```json
{
  "api_base": "http://localhost:8080/v1",
  "api_version": "2.1.0.0",
  "api_type": "codegeex",
  "api_key": "D4B94CC818A3D8A725CCC8FE68B97"
}
```

./codegeex_rest_api_server_api_keys.json :  
```json
{
  "5c0f6958f8ec27e336a1bd04cb64d9a4": {
    "email": "<User's email here>"
  }
}
```
