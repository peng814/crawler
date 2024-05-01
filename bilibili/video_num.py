import requests

cookies = {
    'BIDUPSID': '74874FC1BD3C62548357E76EEDC733A0',
    'PSTM': '1701018716',
    'BAIDUID': '74874FC1BD3C625422F78ED41748AFFA:FG=1',
    'BD_UPN': '12314753',
    'BA_HECTOR': '8lakal0585052l81200180871im6v2v1q',
    'BAIDUID_BFESS': '74874FC1BD3C625422F78ED41748AFFA:FG=1',
    'ZFY': 'Pgm6id9a13ACsIcgGDkFaVDjaL4pVKC8fQjqkww6q6c:C',
    'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'BIDUPSID=74874FC1BD3C62548357E76EEDC733A0; PSTM=1701018716; BAIDUID=74874FC1BD3C625422F78ED41748AFFA:FG=1; BD_UPN=12314753; BA_HECTOR=8lakal0585052l81200180871im6v2v1q; BAIDUID_BFESS=74874FC1BD3C625422F78ED41748AFFA:FG=1; ZFY=Pgm6id9a13ACsIcgGDkFaVDjaL4pVKC8fQjqkww6q6c:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598',
    'Referer': 'https://news.baidu.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'rtt': '1',
    'bsst': '1',
    'cl': '2',
    'tn': 'news',
    'rsv_dl': 'ns_pc',
    'word': 'chatgpt',
}

response = requests.get('https://www.baidu.com/s', params=params, cookies=cookies, headers=headers)
print(response.text)
