import re
import tokenizer
import tiktoken

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

enc_text = tokenizer.encoe(raw_text)
print(len(enc_text))
