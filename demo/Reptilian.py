# 爬虫

# 库 : requests,

import requests
from bs4 import BeautifulSoup
from bs4 import element
import re
import time

# url = "https://www.zhipin.com/job_detail/?query=%E4%BC%9A%E8%AE%A1&scity=101280800&industry=&position="
url = "https://www.zhipin.com/c101280800/h_101280800/?query=%E4%BC%9A%E8%AE%A1&page=1&ka=page-1"
url1 = "https://bj.lianjia.com/zufang/"
bossUrl = "https://www.zhipin.com"

# 拉钩
# lagou_url = "https://www.lagou.com/jobs/list_%E4%BC%9A%E8%AE%A1?city=%E4%BD%9B%E5%B1%B1&cl=false&fromSearch=true&labelWords=&suginput="
lagou_url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%BD%9B%E5%B1%B1&needAddtionalResult=false"

session = requests.session()
headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# print(soup.text)
boss_job_list = soup.find_all('div', class_="job-primary")
boss_page = soup.find("div", class_="page").text
boss_page_list = re.findall('(\\d+)', boss_page)

# first true kd 关键字 pn 页数
lago_post_data = {'first': 'true', 'kd': '会计', 'pn': '1'}
# lago_response = session.post(lagou_url, headers=headers, data=lago_post_data)
# lago_soup = BeautifulSoup(lago_response.text, "lxml")

# https://www.lagou.com/jobs/list_%E4%BC%9A%E8%AE%A1?px=default&city=%E4%BD%9B%E5%B1%B1#filterBox
lago_header = {
    # 'Host': "www.lagou.com",
    # 'Connection': "keep-alive",
    # 'Content-Length': "37",
    # 'Origin': "https://www.lagou.com",
    # 'X-Anit-Forge-Code': "0",
     'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    # 'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    # 'Accept': "application/json, text/javascript, */*; q=0.01",
    # 'X-Requested-With': "XMLHttpRequest",
    # 'X-Anit-Forge-Token': None,
    'Referer': "https://www.lagou.com/jobs/list_%E4%BC%9A%E8%AE%A1",
    # 'Accept-Encoding': "gzip, deflate, br",
    # 'Accept-Language': "zh-CN,zh;q=0.9",
    # 'Cookie': "ga=GA1.2.2026375525.1525620511; user_trace_token=20180506232831-21e2a670-5142-11e8-8f60-525400f775ce; LGUID=20180506232831-21e2aa6c-5142-11e8-8f60-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.2042280525.1526028117; hasDeliver=3; JSESSIONID=ABAAABAAAIAACBIB29940F077989DE1185CA78302A3302F; _putrc=28781494ECF66F42123F89F2B170EADC; login=true; unick=%E4%BD%99%E4%B8%BD%E5%B9%B3; PRE_UTM=; LGSID=20180512225338-41230d09-55f4-11e8-8234-5254005c3644; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSxpPWEL5T3Frjr5xSlFzoIXsXqT_P-mD4HBOLFRyECm%26wd%3D%26eqid%3Dba2f116400016252000000065af6ffec; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; gate_login_token=f2868634071b4bf6479e12938806193a08ae4c580505fac4678bbb66aa81b52c; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1526113572,1526115240,1526115378,1526136819; TG-TRACK-CODE=index_navigation; _gat=1; LGRID=20180512231325-0449765c-55f7-11e8-980b-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1526138005; SEARCH_ID=6d3fb1be32704fccb084195d2457751d"

}

return_data = requests.post(lagou_url, headers=lago_header,data=lago_post_data)
print(return_data.text)


# lagou_job_list = lago_soup.find("ul", class_="item_con_list")
# print(lagou_job_list)


# 打印boss相关信息
def boss_job_detail(div):
    detail = "工作："
    index = "主页："
    info = div.find("div", class_='info-primary').contents
    for s in info:
        if isinstance(s, element.Tag):
            text = s.text.replace("\n", "\t")
            detail += text
            if s.a is not None and s.a.get("href") is not None:
                index = bossUrl + s.a.get("href")
        else:
            detail += "\t"
    detail += "公司信息："
    info = div.find("div", class_='info-company').contents
    for s in info:
        if isinstance(s, element.Tag):
            text = s.text.replace("\n", "\t")
            detail += text
        else:
            detail += "\t"
        # detail += "发布于："
    info = div.find("div", class_='info-publis').contents
    for s in info:
        if isinstance(s, element.Tag):
            text = s.text.replace("\n", "\t")
            detail += text
        else:
            detail += "\t"

    print(detail + "\t" + index)

# 打印拉钩相关工作


# for div in boss_job_list:
#     boss_job_detail(div)
#     # print(div)
# print(boss_page_list)

# for list in lagou_job_list:
#     print(list.text)
