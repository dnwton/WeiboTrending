url = 'https://s.weibo.com/top/summary?cate=realtimehot'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "cookie": "_s_tentry=ent.ifeng.com; Apache=8549258207007.566.1592639656957; SINAGLOBAL=8549258207007.566.1592639656957; login_sid_t=118dca9b8cce25e28e793a1d746a787a; cross_origin_proto=SSL; UOR=ent.ifeng.com,service.weibo.com,www.google.com; ULV=1655082170337:1:1:1:8549258207007.566.1592639656957:; SUB=_2AkMU_Uzwf8NxqwJRmPERy2zja4hwzg7EieKiob0rJRMxHRl-yT9jqk8rtRB6P31iHxsq-iS6P362Hsy5rTHLbfX1KSFZ"
}

mongo_host = '192.168.0.139'
mongo_port = 27017
database = 'trending'
collection = 'weibo'
