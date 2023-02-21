from urllib.request import urlopen
import json
import sys

from lib.bm_api import BmAPI
from lib.daily_traffic_load_stat import DailyTrafficLoadStat

tz1 = "2023-02-21T14:20:13.908Z"

def main():

    bm_api = BmAPI()

    json_stat = bm_api.get_daily_stat()
    
    day_stat = DailyTrafficLoadStat(json_stat)
    print(day_stat.get_prevision_for_hour(tz1))

if __name__ == '__main__':
    sys.exit(main())
