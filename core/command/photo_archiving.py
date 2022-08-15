#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
照片归档
@author: Shadow
"""

import sys
import os
# import shutil
from ..logging.logger import LoggerFactory

class PhotoArchiving:

    def __init__(self, path = ""):
        self.__path = "/Volumes/walkerljl/lpp/"
        self.__logger = LoggerFactory().get_logger()

    def archive(self):
        self.__logger.info("Archiving, path is '%s'." % (self.__path))
        # out_put_path = "/Volumes/walkerljl/images/"
        # if not os.path.exists(os.path.dirname(out_put_path)):
        #     os.makedirs(os.path.dirname(out_put_path))
        photo_dirs = {""}
        for root, dirs, files in os.walk(self.__path, topdown = True):
            for file in files:
                # file_name = os.path.join(root, file)
                file_name = file
                if file.endswith(".JPG") == True:
                    photo_dirs.add(root)
                    self.__logger.info("Add photo directory '%s' to colletion." % (root))
                # self.__logger.info("Processed, file name is '%s', path is '%s'." % (file_name, root))
            # for dir in dirs:
            #     dir_name = os.path.join(root, dir)
            #     self.__logger.info("Processed, directory is '%s'." % (dir_name))
        for photo_dir in photo_dirs:
            # shutil.copy(photo_dir, out_put_path)
            self.__logger.info("Photo directory is '%s'" % (photo_dir))
        self.__logger.info("Archived, path is '%s'." % (self.__path))

  
        