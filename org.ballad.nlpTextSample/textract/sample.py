import textract
 
# 从Word文档中提取文本
text = textract.process("example.docx")
# text = textract.process("cssf_12_552_governance.pdf")

# 打印提取的文本
print(text.decode('utf-8'))


with open('test.txt','w') as f:
   f.write(text.decode('utf-8'))