import time
import json


def import_data(filepath):
    test_case = []
    file = open(filepath)
    while True:
        line = file.readline()
        if not line:
            break
        test_case.append(line.rstrip("\n"))
    file.close()
    return test_case[:200]


def export_success_attack(filepath, success_result):
    time_array = time.localtime(time.time())
    time_string = time.strftime("%Y%m%d%H%M%S", time_array)
    filepath = filepath + "_result_" + time_string
    output_file = open(filepath + '.json', 'w')
    json.dump(success_result, output_file, indent=4)
