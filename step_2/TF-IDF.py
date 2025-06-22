import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# 读取文档
df = pd.read_csv(r'/Users/fuwenxiao/Desktop/pycharm/TDF/分词结果.txt', sep='\t',
                 header=None,names=['text'],encoding='utf-8')

# 分词
corpus = df['text'].tolist()
# 计算 TF-IDF，设置max_df和min_df参数
tfidf_vectorizer = TfidfVectorizer(max_df=0.85, min_df=2)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# 提取关键词及其对应的 TF-IDF 值
feature_names = tfidf_vectorizer.get_feature_names_out()
tfidf_values = tfidf_matrix.toarray()

# 创建 DataFrame
tfidf_df = pd.DataFrame(tfidf_values, columns=feature_names)

# 保存到 Excel 文件
output_file = r'/Users/fuwenxiao/Desktop/pycharm/TDF/结果.xlsx'
tfidf_df.to_excel(output_file, index=False)

print("TF-IDF 结果已保存到", output_file)
