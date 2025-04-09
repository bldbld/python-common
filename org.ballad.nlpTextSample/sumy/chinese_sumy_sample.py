from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from datasets import Dataset
import fitz  # PyMuPDF
import spacy

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)  # Open the PDF file
    text = ""
    for page in doc:  # Iterate through each page
        text += page.get_text()  # Extract text and append it to the text variable
    return text

def split_into_sentences(text):
    doc = nlp(text)  # Process the text with SpaCy
    sentences = [sent.text.strip() for sent in doc.sents]  # Extract sentences and strip whitespace
    return sentences

pdf_path = 'sample_report_bingtuan.pdf' 
# pdf_path = 'cssf_12_552_governance.pdf'
text = extract_text_from_pdf(pdf_path) 
nlp = spacy.load("zh_core_web_sm")  
# nlp = spacy.load("en_core_web_sm")  
sentences = split_into_sentences(text) 
data = {"sentence": sentences}
dataset = Dataset.from_dict(data)

print(dataset.__len__)

for text in dataset:
    # 解析文本
    parser = PlaintextParser.from_string(text, Tokenizer("chinese"))
    # parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    
    # 生成摘要
    summary = summarizer(parser.document, 2)
    for sentence in summary:
        print(sentence)

 
