"""CodeGeeX Utility


"""
from typing import *
import gzip
import json


def stream_jsonl_all(filename: str) -> Iterable[Dict]:
    """Get samples from jsonl.gz

    E.g.:
        codegeex/benchmark/humaneval-x/cpp/data/humaneval_cpp.jsonl.gz
    Ref:
        https://github.com/THUDM/CodeGeeX/blob/main/codegeex/benchmark/evaluate_humaneval_x.py#L85

    """
    results = []
    if filename.endswith(".gz"):
        fp = gzip.open(open(filename, "rb"), "rt")
    else:
        fp = open(filename, "r")
    for line in fp:
        if any(not x.isspace() for x in line):
            results.append(json.loads(line))
    fp.close()

    return results
