# -*- coding:utf-8 -*-
# Learn from Alex Li
# create by Isabel Ding
# Reference: https://keelii.com/2018/09/24/socket-programming-in-python/

import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket() 时传入的 socket 地址族参数 socket.AF_INET 表示因特网 IPv4 地址族，SOCK_STREAM 表示使用 TCP 的 socket 类型，协议将被用来在网络中传输消息
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind(('localhost', 8000)) # bind() 用来关联 socket 到指定的网络接口（IP 地址）和端口号 (('host', port))
    sock.listen(5)   # allow the max number of 5 to wait to get

    while True:
        # wait for others to connect
        conn, addr = sock.accept()
        # get the request from the browser
        data = conn.recv(1024)   # 可以收1024个字符
        print(data)

        # send back the content
        conn.send(b"HTTP/1.1 200 OK\r\nConnect-Type:text/html; charset=utf-8\r\n\r\n")   # send the content as text
        conn.send("<h1 style='color:red'>You are beautiful</h1>".encode("utf-8"))

        # close the socket connetcion
        conn.close()

if __name__ == "__main__":
    # go to localhost:8000 and you will see "Your are beautiful"in h1 and in red.   MAGIC!!!!!!
    main()