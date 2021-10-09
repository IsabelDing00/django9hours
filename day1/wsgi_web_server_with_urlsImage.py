# -*- coding:utf-8 -*-
# Learn from Alex Li
# create by Isabel Ding
# https://blog.csdn.net/laughing2333/article/details/51288660
# Notice: be aware if the localhost has been opened before, remember to close the code you ran before, and then run this
from wsgiref.simple_server import make_server

import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def book(environ, start_response):
    print("Book Page")

    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    data = """
        <h1>Welcom to book page</h1>
            <img src='/static/imgs/testing/gif' />
        <p>Thank you for visiting</p>
    """
    # need to change the picture name

    return [bytes(data,encoding="utf-8"), ]

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

def imageHandler(url):
    """
    :param url: /static/omgs/testimg.gif
    :return:
    """
    # print("this is base dir:")
    image_path = re.sub('static', '/static_data', url)
    # print("Base dir: ", BASE_DIR)
    img_abs_path = os.path.join(BASE_DIR, image_path)
    if os.path.isfile(img_abs_path):  # check if this file exist
        f = open(image_path, "rb")  # open this file as rb
        data = f.read  # get the image and return
        return [data, 0]
    return [None, 1]

def run_server(environ,start_response):
    print('hahaha', environ)

    url_list = url_dispacher()  # get all the urls
    request_url = environ.get("PATH_INFO")
    print('request url', request_url)

    if request_url in url_list:
        data = url_list[request_url](environ,start_response)  # () helps to execute this line, get data from urls
        return data # return the data to show on web
    elif request_url.startswith("/static/"):
        img_data, img_status = imageHandler(request_url)
        if img_status == 0:   # img exist
            start_response("200 OK", [('Content-Type', 'text/jpg;charset=utf-8')])
            return img_data
    else:
        start_response("404", [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes('<h2> Page not fond! </h2>', encoding="utf-8"),]


s = make_server('localhost', 8000, run_server)  # take the address and then run the run_server
s.serve_forever()   # 相当于一个死循环， 可以一直做