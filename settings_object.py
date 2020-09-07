# Python imports
import logging
import json
# Third-Party imports
# Project imports
import consts
import utils


class AppSettings(object):

    def __init__(self, *args, **kwargs):
        self.settings_dic = utils.read_file(
            consts.SETTINGS_FILE_NAME)
        self.near_systems = utils.read_file(consts.SYSTEMS_FILE_NAME)
