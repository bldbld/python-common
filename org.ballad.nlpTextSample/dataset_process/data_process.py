import textract
from harvesttext import HarvestText
 
def store2txt (text,file_name,tag):
    with open(file_name+'_'+tag+'.txt','w') as f:
         f.write(text)

# 使用 Textact 提取内容
# 从Word Docx文档中提取文本 
def read_from_docx(file_name, isStoreTxt):
    text = textract.process(file_name)
    text = text.decode('utf-8')
    if isStoreTxt:
        store2txt(text, file_name,'source_text')
    return text

# 使用 HarvestText 优化数据集
def clean_data(text, file_name, isStoreTxt):
    ht = HarvestText()
    cleaned_text = ht.clean_text(text)
    if isStoreTxt:
        store2txt(cleaned_text, file_name,'cleaned')

# 使用 HarvestText 生成摘要
def summary_text_harvesttext(text, file_name, isStoreTxt):
    return

# 使用 sumy 生成摘要
def summary_text_sumy(text, file_name, isStoreTxt):
    return

file_name = "example.docx"
text = read_from_docx(file_name,True)
clean_data(text, file_name,True)