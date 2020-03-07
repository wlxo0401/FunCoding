






from bs4 import BeautifulSoup




headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://namu.wiki/w/%EC%88%98%EB%8F%84%EA%B6%8C%20%EC%A0%84%EC%B2%A0%201%ED%98%B8%EC%84%A0/%EC%97%AD%20%EB%AA%A9%EB%A1%9D'
requests.get(url, headers = headers)

soup = BeautifulSoup(requests, 'html.parser')

i = 1
f = open('1호선.txt', 'w')
for anchor in soup.select('a.wiki-link-internal'):
    data = str(i) + '  ' + anchor.get_text()
    i = i + 1
    f.write(data)
f.close()
