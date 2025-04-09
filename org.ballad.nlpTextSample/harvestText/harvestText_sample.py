from harvesttext import HarvestText

# (使用networkx实现) 使用Textrank算法，得到从文档集合中抽取代表句作为摘要信息，可以设置惩罚重复的句子，也可以设置字数限制(maxlen参数)：

print("各种清洗文本")
ht0 = HarvestText()
# 默认的设置可用于清洗微博文本
# text1 = "回复@钱旭明QXM:[嘻嘻][嘻嘻] //@钱旭明QXM:杨大哥[good][good]"
# print("清洗微博【@和表情符等】")
# print("原：", text1)
# print("清洗后：", ht0.clean_text(text1))




para = "工资福利费用减少40.96万元，占全年费用总额的0.00%"
entity_mention_dict = {'武磊':['武磊','武球王'],'郜林':['郜林','郜飞机'],'前锋':['前锋'],'上海上港':['上港'],'广州恒大':['恒大'],'单刀球':['单刀']}
entity_type_dict = {'武磊':'球员','郜林':'球员','前锋':'位置','上海上港':'球队','广州恒大':'球队','单刀球':'术语'}
ht.add_entities(entity_mention_dict,entity_type_dict)
print("\nSentence segmentation")
print(ht.seg(para,return_sent=True)) 


# ht = HarvestText()
# print("\nText summarization")
# docs = ["武磊威武，中超第一射手！",
#         "郜林看来不行，已经到上限了。",
#         "武球王威武，中超最强前锋！",
#         "武磊和郜林，谁是中国最好的前锋？"]

# for doc in ht.get_summary(docs, topK=2):
#     print(doc)
# print("\nText summarization(避免重复)")
# for doc in ht.get_summary(docs, topK=3, avoid_repeat=True):
#     print(doc)
