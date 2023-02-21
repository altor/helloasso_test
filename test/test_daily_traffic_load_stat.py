import pytest

from lib.daily_traffic_load_stat import DailyTrafficLoadStat


json1 = '{"records": [{"fields": {"bm_prevision": 1, "bm_heure": "2023-02-21T14:20:13.908Z"}},{"fields":{"bm_prevision": 2, "bm_heure": "2023-02-21T14:25:13.908Z"}},{"fields": {"bm_prevision": 3, "bm_heure": "2023-02-21T14:30:13.908Z"}}]}'

tz1 = "2023-02-21T14:20:13.908Z"
tz2 = "2023-02-21T14:25:13.908Z"
tz3 = "2023-02-21T14:30:13.908Z"

def test_get_prevision_for_hour_tz1_on_DailyTraffic_created_on_json1_return_1():
    day_stat = DailyTrafficLoadStat(json1)
    assert day_stat.get_prevision_for_hour(tz1) == 1

def test_get_prevision_for_hour_tz2_on_DailyTraffic_created_on_json1_return_2():
    day_stat = DailyTrafficLoadStat(json1)
    assert day_stat.get_prevision_for_hour(tz2) == 2

def test_get_prevision_for_hour_tz3_on_DailyTraffic_created_on_json1_return_3():
    day_stat = DailyTrafficLoadStat(json1)
    assert day_stat.get_prevision_for_hour(tz3) == 3
