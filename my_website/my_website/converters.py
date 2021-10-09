# -*- coding:utf-8  -*-
# created by Isabel Ding

class YearConverter():
    regex = r'0-9{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d"