# -*- coding:utf-8 -*-
# Learn from Alex Li
# create by Isabel Ding
# https://blog.csdn.net/laughing2333/article/details/51288660
# Notice: be aware if the localhost has been opened before, remember to close the code you ran before, and then run this
from wsgiref.simple_server import make_server

def book(environ, start_response):
    print("Book Page")

    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h2> Book Page </h2>', encoding="utf-8"), ]

def food(environ, start_response):
    print("Food Page")

    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h2> Food Page </h2>', encoding="utf-8"), ]

def url_dispacher():
    urls = {
        '/book': book,
        '/food': food,
    }
    return urls

def run_server(environ,start_response):
    print('hahaha', environ)

    url_list = url_dispacher()  # get all the urls
    request_url = environ.get("PATH_INFO")
    print('request url', request_url)

    if request_url in url_list:
        data = url_list[request_url](environ,start_response)  # () helps to execute this line, get data from urls
        return data # return the data to show on web
    else:
        start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes('<h2> Page not fond! </h2>', encoding="utf-8"),]
        # the start_response here are required every time,
        # but django will help users to do it so you don't have to redo -> import HttpResponse


s = make_server('localhost', 8000, run_server)  # take the address and then run the run_server
s.serve_forever()   # 相当于一个死循环， 可以一直做