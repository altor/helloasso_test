import json

class DailyTrafficLoadStat:
    """
    """

    def __init__(self, json_str):
        self.json_stat_array = json.loads(json_str)['records']

    def get_prevision_for_hour(self, hour):
        """
        Return traffic load information for input hour
        :param (str) hour:
        :return int:
        :raise ValueError: if the given hour can't be found in the daily statistics
        """
        for i in range(len(self.json_stat_array)):
            if self.json_stat_array[i]['fields']['bm_heure'] == hour:
                return self.json_stat_array[i]['fields']['bm_prevision']
        raise ValueError
            
    
    def get_minimal_prevision(self):
        """
        Return the hour of the day with the minimal traffic load and the traffic load
        :return (str, int):
        """
        pass

    def get_maximal_prevision(self):
        """
        Return the hour of the day with the maximal traffic load and the traffic load
        :return (str, int):
        """
        pass

    def get_average_traffic_load(self):
        """
        Return average_traffic_load for the current day
        :return (timestamp, int):
        """
        pass
