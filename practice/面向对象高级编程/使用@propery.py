#!usr/bin/env python
# coding: utf-8

# 对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value


if __name__ == '__main__':
    s = Student()
    s.score = 100
    print(s.score)
