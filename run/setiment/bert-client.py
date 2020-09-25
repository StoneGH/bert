from bert_base.client import BertClient


attrs = ['质量很好，和详情描述一致。','大小比TX2小好多，还好没有买TX2。','这款升级版的价格更低，性能也更好，显示屏很垃圾，用树莓派的时候画质很差。','用这个板子发现真心不亏这个价格，不愧是英伟达出品。']

with BertClient(ip='127.0.0.1', port=5575, port_out=5576, show_server_config=False, check_version=False, check_length=False,timeout=50000 ,  mode='CLASS') as bc:
    res1 = bc.encode(attrs)
    print(res1)
