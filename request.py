import requests, bs4


class Request:
    def __init__(self):
        pass

    def get_temp(self):
        s = requests.get('https://sinoptik.com.ru/погода-москва')
        b = bs4.BeautifulSoup(s.text, "html.parser")
        p3 = b.select('.weather__article_main_right-table .table__temp')
        res = []
        for pogoda in p3:
            res.append(pogoda.getText())
        print(res)
        return res
