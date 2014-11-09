import re

def join(text):
  text = re.sub(r'([^,])\n\s*([\)\]\}"\'\.,]|->|::)', r'\1\2', text)
  text = re.sub(r'([\(\[\{"\'\.]|::|->)\s*\n\s*', r'\1', text)
  text = re.sub(r'\s*\n\s*', ' ', text)

  return text