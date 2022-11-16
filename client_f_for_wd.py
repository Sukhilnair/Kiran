from datetime import datetime
import time

def datetime_from_utc_to_local(orig_timestamp):
    try:
        utc_datetime = datetime.fromtimestamp(orig_timestamp/1000)
        # now_timestamp = time.time()
        # offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
        return utc_datetime
    except Exception as err:
        print("Error while converting timestamp to human readable: ", err)
        return orig_timestamp

def process_event_json_before_sink(event_json):
    try:
        for tmp in event_json['event']['tags']:
            if tmp['key'] == 'direction':
                if tmp['value'] == 'EXIT':
                    tmp['value'] == 'Wrong Direction'
                    event_json['event']['priority'] = 3
                    readable_datetime = str(datetime_from_utc_to_local(int(event_json['info']['event_timestamp'])))
                    readable_time = readable_datetime
                    # readable_time = readable_datetime.split(' ')[-1].split('.')[0]
                    event_json['event']['name'] = event_json['event']['name']
    except Exception as err:
        print("Error while resetting priority: ", err)
    return event_json


# import json
# if __name__== '__main__':
#     json_data = json.load(open('final.json'))
#     process_event_json_before_sink(json_data)
#     print("Priority: ", json_data['event']['priority'])
#     print("name: ", json_data['event']['name'])
