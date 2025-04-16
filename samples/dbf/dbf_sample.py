import pandas as pd
from dbfread import DBF

# 指定 DBF 文件路径
dbf_path = 'FILE_NAME.DBF'

# 使用dbfread读取DBF文件
table = DBF(dbf_path, encoding='GBK', ignore_missing_memofile=True)

# 输出 CSV 文件
df = pd.DataFrame(iter(table))
df.to_csv('output.csv', index=False, encoding='GBK')
