# 程序功能：爬取头条热榜的榜单数据
# 原创作者：马哥python说
# 联系方式：公众号"老男孩的平凡之路"

import requests
import pandas as pd
import re

# 保存文件名
result_file = '头条热榜.csv'
# 请求头
h1 = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
}
# 请求地址
url = 'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc'
r = requests.get(url, headers=h1)
# 查看响应码
print(r.status_code)
# 接收返回数据
json_data = r.json()
# 统计数据量
data_num = len(json_data['data'])
print('数量量：', data_num)
title_list = []  # 热榜标题
value_list = []  # 热度值
url_list = []  # 热榜链接
category_list = []  # 热榜分类
label_list = []  # 热榜标签
for data in json_data['data']:
	# 热榜标题
	title = data['Title']
	print('热榜标题：', title)
	title_list.append(title)
	# 热度值
	value = data['HotValue']
	value_list.append(value)
	# 热榜分类
	try:
		category = data['InterestCategory']
		category = '/'.join(category)
	except:
		category = ''
	category_list.append(category)
	# 热榜标签
	label = data['Label']
	label_list.append(label)
	# 热榜链接
	url2 = data['Url']
	try:
		url3 = re.search(r"(?<=https:\/\/www\.toutiao\.com\/trending\/)\d+", url2).group(0)
		url4 = 'https://www.toutiao.com/trending/' + str(url3)
	except:
		url4 = url2
	url_list.append(url4)
# 把列表数据组装成Dataframe数据
df = pd.DataFrame(
	{
		'热榜排名': range(1, data_num + 1),  # 一共50条
		'热榜标题': title_list,
		'热度值': value_list,
		'热榜标签': label_list,
		'热榜分类': category_list,
		'热榜链接': url_list,
	}
)
# 保存到csv文件
df.to_csv(result_file, header=True, index=False, encoding='utf_8_sig')
print('文件保存成功：', result_file)
