# Python imports
import logging
import json
import re
import glob
import os
from time import sleep
# Third-Party imports
import pyttsx3
# Project imports
import consts


def read_file(json_file_name):
    with open(json_file_name) as f:
        file_content_dict = json.loads(f.read())
    return file_content_dict


def get_latest_log_file(file_path):
    list_of_files = glob.glob(file_path)
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def read_latest_eve_intel_logs(path_to_logs):
    with open(path_to_logs, encoding="utf16", errors='ignore') as f:
        logs_content = f.read().strip(' ')
        found = re.findall(r'.*(\[.*\] .* > .*)', logs_content)
    return found[consts.LATEST_LOGS_NUMBER:]


def check_for_new_log(compare_list, logs_list):
    dif_list = [i for i in compare_list + logs_list if i not in compare_list]
    return dif_list


def check_new_log_content(new_log_entry, SettingsObject):
    logging.info(f'found {len(new_log_entry)} new log entries')
    # convert new log entry to a list
    for i in new_log_entry:
        new_log_entry_list = i.split(' ')
        
        # clear items
        new_log_entry_list = [i.strip('*') for i in new_log_entry_list]

        # check if the near systems in the new log
        if not any((y in new_log_entry_list for y in consts.EXCEPTION_WORDS)):
            for i in SettingsObject.near_systems['jumps_to_near_systems']:
                for k, v in i.items():
                    if any((x in new_log_entry_list for x in v)):
                        # play sound if near systems in the new log
                        jumps = int(k)
                        text = f'Enemy in {jumps} jumps from the region.'
                        play_alarm(
                            text, SettingsObject.settings_dic['alarm_volume'])
                        logging.info(f'Enemy in {jumps} in <{v}>')


def play_alarm(text, volume):
    engine = pyttsx3.init()
    engine.setProperty('volume', eval(volume))
    engine.say(text)
    engine.runAndWait()
    #logging.info('Warning played')
