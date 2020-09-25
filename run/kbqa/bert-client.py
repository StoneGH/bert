import time
from bert_base.client import BertClient


#sentences = ['陈平的国籍？国籍','陈平的国籍？去世年月','陈平的国籍？逝世日期','陈平的国籍？职业']
#sentences = ['西游记是什么类型的电视剧？类型','西游记是什么类型的电视剧？首播时间','西游记是什么类型的电视剧？国家／地区','西游记是什么类型的电视剧？每集长度','西游记是什么类型的电视剧？播映','西游记是什么类型的电视剧？编剧','西游记是什么类型的电视剧？主题曲']

#sentences = ['高等数学是哪个出版社出版的？出版社','高等数学是哪个出版社出版的？书名','高等数学是哪个出版社出版的？出版时间','高等数学是哪个出版社出版的？isbn','高等数学是哪个出版社出版的？定价','高等数学是哪个出版社出版的？开本']


#sentences = ['高等数学的书名叫什么？出版社','高等数学的书名叫什么？书名','高等数学的书名叫什么？出版时间','高等数学的书名叫什么？isbn','高等数学的书名叫什么？定价','高等数学的书名叫什么？开本']


sentences = ['高等数学的这本书售价多少钱？出版社','高等数学的这本书售价多少钱？书名','高等数学的这本书售价多少钱？出版时间','高等数学的这本书售价多少钱？isbn','高等数学的这本书售价多少钱？定价','高等数学的这本书售价多少钱？开本']


with BertClient(ip='127.0.0.1', port=5575, port_out=5576, show_server_config=False, check_version=False, check_length=False,timeout=50000 ,  mode='CLASS') as bc:
    start_t = time.perf_counter()
    print('start time:{}'.format(start_t))
    res1 = bc.encode(sentences)
    print(res1)
    end_t = time.perf_counter()
    print('end time:{}'.format(end_t))
    print('耗时:',end_t - start_t)
