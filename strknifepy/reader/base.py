# encoding: utf-8
from __future__ import unicode_literals
import codecs
import os

class Reader(object):

    def __init__(self, file_path=None, encoding='utf-8'):
        self._source = codecs.open(file_path, 'rb', encoding=encoding)

    def read(self):
        return self._source
