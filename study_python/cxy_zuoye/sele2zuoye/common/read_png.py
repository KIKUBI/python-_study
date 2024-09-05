# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      read_png.py
# Author:       陈啸宇
# Datetime:     2024/8/14 18:24
# Description:
# ---------------------------------------------------------------------------
import os

from study_python.cxy_zuoye.sele2zuoye.common.read_ini import ReadIni


class ReadPng:
    def __init__(self):
        ini = ReadIni()
        self.pngpath = ini.get_png_path('pngName')
        self.pngpaths = os.path.dirname(__file__)
        self.pngpaths = os.path.dirname(self.pngpaths)
        self.pngpathsz = os.path.join(self.pngpaths, self.pngpath)
        if not os.path.exists(self.pngpath):
            os.makedirs(self.pngpathsz)
    def read_png(self):
        return self.pngpathsz



