"""Postprocess code before testing

"""
from language_features import CPP_INCLUDES

class Postprocessor:
    def __init__(self):
        pass

    def __call__(
            self,
            language: str,
            prompt: str,
            code: str,
            ) -> str:
        """preprocess the code

        
        """

        # CodeGeeX's code sometimes uses <|endoftext|>
        code = code.replace('<|endoftext|>', '')

        if language =='python':
              # From CodeGeeX - line 40 @evaluate_humaneval_x.py
              code_ = []
              for line in code.split("\n"):
                  if (len(line.strip()) > 0 and line[0] != ' ' and line[0] != '\t'):
                      break
                  code_.append(line)
              code = "\n".join(code_)

              # sys.exit() may cause code exit directly without testing
              code = code.replace('sys.exit', '')
        elif language == 'java':
                # Remove dupliated 
                # class Solution
                code_ = []
                for line in code.split("\n"):
                    if line.strip().startswith('class Solution')\
                            or line.strip().startswith('`'):
                        break
                    code_.append(line)
                code = "\n".join(code_)
        elif language == 'cpp':
                # There are main() both in generated code and test.
                # int main(){
                code_ = []
                for line in code.split("\n"):
                    if line.strip().startswith('int main(){'):
                        break
                    code_.append(line)
                code = "\n".join(code_)

        return code
