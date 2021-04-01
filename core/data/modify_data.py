import json
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
filename='../../../DataSet/vqa-v2/vqa/v2_OpenEnded_mscoco_train2014_questions.json'
noun_train=[]
with open(filename) as f:
    data=json.load(f)
    questions=data['questions']
    questions_new=[]
    for q in questions:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        tokens = nltk.word_tokenize(q['question'])
        tags=nltk.pos_tag(tokens)
        for i in tags:
            if (i[1]=='NN' or i[1]=='NNS' or i[1]=='NNP' or i[1]=='NNPS'):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                noun_train.append(i[0])
# for i in noun_train:
#     print(i)  



filename='../../../DataSet/vqa-v2/vqa/v2_OpenEnded_mscoco_val2014_questions.json'
noun_val=[]
with open(filename) as f:
    data=json.load(f)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    questions=data['questions']
    questions_new=[]
    for q in questions:
        tokens = nltk.word_tokenize(q['question'])
        tags=nltk.pos_tag(tokens)
        for i in tags:
            if (i[1]=='NN' or i[1]=='NNS' or i[1]=='NNP' or i[1]=='NNPS'):
                noun_val.append(i[0])
# for i in noun_val:
#     print(i)    
for i in noun_val  :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    print((list(set(noun_val) - set(noun_train))))      