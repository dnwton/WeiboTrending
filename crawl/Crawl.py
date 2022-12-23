import parsel
import requests


class Crawl:

    def crawl(self, url, headers):
        response = requests.get(url=url, headers=headers)
        selector = parsel.Selector(response.text)
        trs = selector.css('#pl_top_realtimehot tbody tr')
        data = []
        i = 1
        for tr in trs:
            title = tr.css('.td-02 a::text').get()
            hot = tr.css('.td-02 span::text').get()
            meta_data = {
                'rank': i,
                'title': title,
                'hot': hot,
            }
            data.append(meta_data)
            i += 1

        return data
