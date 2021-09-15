import json

import requests  # requests模块需要使用 pip 命令安装

headers = {
    'X-Auth-Token': 'WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP'
}
#
# response = requests.get('https://www.yuque.com/api/v2/hello', headers=headers)
# result = json.loads(response.text)
# print(result)
#
# userinfo = requests.get('https://www.yuque.com/api/v2/users/baili-qq4sf', headers=headers)
# print(json.loads(userinfo.text))

# repos = requests.get('https://www.yuque.com/api/v2/users/baili-qq4sf/repos', headers=headers)
# print(json.loads(repos.text))
# # baili-qq4sf/bgzr5s
#
# repos_details = requests.get('https://www.yuque.com/api/v2/repos/baili-qq4sf/bgzr5s', headers=headers)
# print(json.loads(repos_details.text))
#
# doc_list = requests.get('https://www.yuque.com/api/v2/repos/baili-qq4sf/bgzr5s/docs', headers=headers)
# print(json.loads(doc_list.text))

# doc_details = requests.get('https://www.yuque.com/api/v2/repos/baili-qq4sf/bgzr5s/docs/lxsoz7', headers=headers)
# print(json.loads(doc_details.text))
data={
    'Key':'Description',
    'title':'wewe',
    'slug':'zg56iv',
    'public':'0',
    'format':'markdown',
    'body':'测试内容测试内容不是好的好乱哦出来是的'
}
creat_doc = requests.post('https://www.yuque.com/api/v2/repos/baili-qq4sf/bgzr5s/docs', headers=headers,data=data)
print(json.loads(creat_doc.text))
