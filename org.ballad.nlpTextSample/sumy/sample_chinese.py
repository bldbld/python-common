from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
 
# 输入中文文本
text = """
自然语言处理（NLP）是计算机科学、人工智能和语言学领域的一个子领域，研究计算机与人类语言之间的相互作用，特别是如何编程以处理和分析大规模的自然语言数据。
最终目标是使计算机能够“理解”文档的内容，包括其中的语言细微差别。该技术可以准确地提取文档中包含的信息和见解，并对文档进行分类和组织。
"""
 
# 解析文本
parser = PlaintextParser.from_string(text, Tokenizer("chinese"))
summarizer = LsaSummarizer()
 
# 生成摘要
summary = summarizer(parser.document, 2)
for sentence in summary:
    print(sentence)