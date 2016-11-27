# encoding: utf-8
from __future__ import unicode_literals
from collections import OrderedDict
import codecs
import os


class Cut(object):
    def __init__(self, value='', size=None, zfill=False):
        self.size = size
        self.zfill = zfill
        self.value = value

    def __repr__(self):
        return '<Cut: {}>'.format(self.value)


class Knife(OrderedDict):
    def __init__(self, source='', endline='\n', *args, **kwargs):
        super(OrderedDict, self).__init__()
        self._source = source
        self._endline = endline

    def lines(self):
        return self._source.split(self._endline)

    @classmethod
    def _cuts(cls):
        return [getattr(cls, i) for i in cls.__dict__ if isinstance(getattr(cls, i), Cut)]

    def crop_lines(self, start=0):
        cuts = self._cuts()
        for line in self.lines():
            for cut in cuts:
               start = self.crop(line, cut, start)

    def crop(self, line, cut, start):
        final_position = start + cut.size
        if cut.zfill:
            cut.value = line[start: final_position].zfill(cut.size)
        else:
            cut.value = line[start: final_position]
        return final_position
