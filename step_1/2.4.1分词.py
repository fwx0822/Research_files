import jieba
from spyder_kernels.utils.lazymodules import pandas

#添加自定义词典
jieba.load_userdict("专业词典.txt")

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('停用词典.txt', encoding='UTF-8').readlines()]
    return stopwords
# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    #print("正在分词")
    sentence_depart = jieba.cut(sentence.strip(),HMM=False)
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        #if word not in stopwords:
        if word not in stopwords and len(word) >= 2 and not word.isdigit():
        # 只对长度大于2的词进行统计
        # 对wordstop中的词不作统计
        # 对纯数字字符串(例如年份等)不作统计
            if word != '\t':
                outstr += word
                outstr += " "
                #outstr +="\n"#分词及如果分行表示用这个
    return outstr



def output(inputfilename,outputfilename):
    inputfile = open(inputfilename,encoding= 'UTF-8',mode = 'r')
    outputfile = open(outputfilename, encoding='UTF-8', mode='w')
    for line in inputfile.readlines():
        line_seg = seg_depart(line)
        #outputfile.write(line_seg)
        outputfile.write(line_seg + '\n')#分词结果不在一行展示
        #print("-------------------正在分词和去停用词-----------")
    inputfile.close()
    outputfile.close()

if __name__ == '__main__':
    print("__name__",__name__)
inputfilename = "原始文本.txt"
outputfilename = "分词结果.txt"
output(inputfilename,outputfilename)

print("删除停用词和分词成功！！！")
df = pandas.read_csv(outputfilename, header=None, names=["分词结果"])


excel_filename = "分词结果.xlsx"
df.to_excel(excel_filename, index=False)

print("分词结果已保存至:", excel_filename)
