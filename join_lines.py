import re

def join(text):
  result = re.sub(r',\s*\n\s*([)}\]])', r'\1', text)
  if result != text:
    return result, -1

  match = re.search(r'"(\s*[\+\.])\s*\n\s*"', text)
  if match != None:
    result = re.sub(r'"(\s*[\+\.])\s*\n\s*"', ' ', text)
    return result, -(len(match.group(1)) + 1)

  match = re.search(r'\'(\s*[\+\.])\s*\n\s*\'', text)
  if match != None:
    result = re.sub(r'\'(\s*[\+\.])\s*\n\s*\'', ' ', text)
    return result, -(len(match.group(1)) + 1)


  text = re.sub(r'([^,])\n\s*([\)\]\}"\'\.,]|->|::)', r'\1\2', text)
  text = re.sub(r'([\(\[\{"\'\.]|::|->)\s*\n\s*', r'\1', text)
  text = re.sub(r'\s*\n\s*', ' ', text)

  return text, 0