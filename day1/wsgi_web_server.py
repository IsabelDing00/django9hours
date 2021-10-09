# -*- coding:utf-8 -*-
# Learn from Alex Li
# create by Isabel Ding
# https://blog.csdn.net/laughing2333/article/details/51288660
# Notice: be aware if the localhost has been opened before, remember to close the code you ran before, and then run this
from wsgiref.simple_server import make_server


def run_server(environ,start_response):
    print('hahaha', environ)

    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h2> Hello from Isabel </h2>', encoding="utf-8"),]


s = make_server('localhost', 8000, run_server)  # take the address and then run the run_server
s.serve_forever()   # 相当于一个死循环， 可以一直做