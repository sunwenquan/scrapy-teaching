from scrapy import Requestclass IterYield:    start_urls = [        'http://quotes.toscrape.com/tag/humor/',        'http://www.baidu.com'    ]    def start_requests(self):        requests = []        for url in self.start_urls:            req = Request(url, dont_filter=True)            requests.append(req)        return requestsdef iter_yield_test():    iteryield = IterYield()    reqs = iteryield.start_requests()    print(reqs)    print(type(reqs)) # list    print(type(iter(reqs))) # list_iterator    print('end')def f():    yield 1    yield 2    yield 3    yield 4def f2():    return [1,2,3,4]def f_test():    g = f()    for i in g:        print(i)def f2_test():    g = f2()    for i in g:        print(i)def f3():    return iter([1,2,3,4])def f3_test():    g = f3()    for i in g:        print(i)if __name__ == '__main__':    f3_test()