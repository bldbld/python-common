from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
 
# 输入文本
text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence
concerned with the interactions between computers and human language, in particular how to program computers to process
and analyze large amounts of natural language data. The result is a computer capable of "understanding" the contents
of documents, including the contextual nuances of the language within them. The technology can then accurately extract
information and insights contained in the documents as well as categorize and organize the documents themselves.
"""
 
# 解析文本
parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()
 
# 生成摘要
summary = summarizer(parser.document, 2)
for sentence in summary:
    print(sentence)