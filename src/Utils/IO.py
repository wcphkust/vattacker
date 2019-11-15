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
    time_string = time.strftime("%d%H%M", time_array)
    filepath = filepath + "_result_" + time_string
    output_file = open(filepath + '.json', 'w')
    json.dump(success_result, output_file, indent=4)


def load_adversarial_example(filepath):
    input_file = open(filepath + '.json', 'r')
    results = json.load(input_file)
    return results


def export_check_result(filepath, check_result):
    """
    # type of check result:
        # A: totally same
        # B: sentimental different
        # C: illegal grammar
        # D: Others
    """
    check_result_A = []
    check_result_B = []
    check_result_C = []
    check_result_D = []
    for item in check_result:
        if item["type"] == "A":
            check_result_A.append(item)
        if item["type"] == "B":
            check_result_B.append(item)
        if item["type"] == "C":
            check_result_C.append(item)
        if item["type"] == "D":
            check_result_D.append(item)
    time_array = time.localtime(time.time())
    time_string = time.strftime("%d%H%M", time_array)

    filepath_A = filepath + "_checkA_" + time_string
    output_file_A = open(filepath_A + '.json', 'w')
    json.dump(check_result_A, output_file_A, indent=4)

    filepath_B = filepath + "_checkB_" + time_string
    output_file_B = open(filepath_B + '.json', 'w')
    json.dump(check_result_B, output_file_B, indent=4)

    filepath_C = filepath + "_checkC_" + time_string
    output_file_C = open(filepath_C + '.json', 'w')
    json.dump(check_result_C, output_file_C, indent=4)

    filepath_D = filepath + "_checkD_" + time_string
    output_file_D = open(filepath_D + '.json', 'w')
    json.dump(check_result_D, output_file_D, indent=4)

    file_path_overview = filepath + "_overview_" + time_string
    output_file_overview = open(file_path_overview + '.json', 'w')
    check_overview = {"all(A+B+C+D)": len(check_result),
                      "totally Same(A)": (len(check_result_A), str(len(check_result_A) / len(check_result))[:5] + '%'),
                      "sentimental different(B)": (
                      len(check_result_B), str(len(check_result_B) / len(check_result))[:5] + '%'),
                      "illegal grammar(C)": (
                      len(check_result_C), str(len(check_result_C) / len(check_result))[:5] + '%'),
                      "Others(D)": (len(check_result_D), str(len(check_result_D) / len(check_result))[:5] + '%')}
    json.dump(check_overview, output_file_overview, indent=4)

    check_result_sorted = []
    check_result_sorted.extend(check_result_A)
    check_result_sorted.extend(check_result_B)
    check_result_sorted.extend(check_result_C)
    check_result_sorted.extend(check_result_D)
    file_path_sorted_all = filepath + "_SortedAll_" + time_string
    output_file_sorted_all = open(file_path_sorted_all + '.json', 'w')
    json.dump(check_result_sorted, output_file_sorted_all, indent=4)


