def import_data(filepath):
    test_case = []
    file = open(filepath)
    while True:
        line  = file.readline()
        if not line:
            break
        test_case.append(line.rstrip("\n"))
    file.close()
    return test_case
