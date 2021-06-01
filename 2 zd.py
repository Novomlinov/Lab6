#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    dict_items = {5: 'x', 10: 'y'}.items()
    print('Словарь --', dict_items)
    inv_dict = lambda d: {v: k for k, v in d}
    print('Новый славарь --', inv_dict(dict_items))