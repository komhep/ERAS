# Python imports
import logging
import time
# Third-Party imports
# Project imports
import utils
from settings_object import AppSettings
import consts

logging.getLogger().setLevel(logging.INFO)
logging.info('Starting EVE early alarm system')

SettingsObject = AppSettings()
logging.info('Settings object created')

logs_file_path = utils.get_latest_log_file(
    SettingsObject.settings_dic['path_to_eve_logs'])
logging.info('Paths are set')

first_run = True
compare_logs_list = []

logging.info('Listening to the channel...')
while True:
    latest_logs = utils.read_latest_eve_intel_logs(logs_file_path)
    if first_run:
        compare_logs_list = latest_logs
        first_run = False

    new_log_entry = utils.check_for_new_log(compare_logs_list, latest_logs)
    if new_log_entry:
        utils.check_new_log_content(new_log_entry, SettingsObject)
    compare_logs_list = latest_logs

    (consts.UPDATE_RATE_SECS)

logging.warning('Listener finished the job!')
