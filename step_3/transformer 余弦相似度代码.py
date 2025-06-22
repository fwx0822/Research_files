from sentence_transformers import SentenceTransformer, util
import torch
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

texts = ["终身教育并非具体实体，而是指人的一生教育与个人及社会生活全体的教育的总和。它本质是一种思想原则，旨在打破传统教育的时间与空间限制，将教育视为持续一生的综合过程。", "终身教育是个人或集团为提升生活水平，通过一生经历的人性、社会和职业过程，涵盖正规、非正规及不正规学习的综合统一理念。"]
embeddings = model.encode(texts, convert_to_tensor=True)

from sentence_transformers.util import cos_sim
import torch
similarity_matrix = cos_sim(embeddings, embeddings)

threshold = 0.70
similar_pairs = []
for i in range(len(texts)):
    for j in range(i + 1, len(texts)):
        if similarity_matrix[i][j] > threshold:
            similar_pairs.append((texts[i], texts[j], similarity_matrix[i][j].item()))

import pandas as pd
results = pd.DataFrame(similar_pairs, columns=["Text1", "Text2", "Similarity"])
results.to_csv("similar_education_ideologies.csv", index=False)