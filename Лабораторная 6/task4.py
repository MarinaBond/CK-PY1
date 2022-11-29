import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(filename, delimiter: str = ",", new_line: str = '\n') -> list[dict]:
    """
    This function convert json to csv
    :param filename: This is the name of input file
    :param delimiter: This is the separator between values
    :param new_line: This is the separator between strings
    :return: This is the operator for returning data after the function has been executed
    """
    with open(filename, 'r') as inp_f:
        keys = []
        d_1 = {}
        d_2 = {}
        d_3 = {}
        d_4 = {}
        json_dict = [d_1, d_2, d_3, d_4]
        for ind, string in enumerate(inp_f):
            str_1 = string.strip(new_line).split(delimiter)
            if ind == 0:
                keys = [header for header in str_1]
            else:
                for x, _ in enumerate(keys):
                    if ind == 1:
                        d_1[keys[x]] = str_1[x]
                    elif ind == 2:
                        d_2[keys[x]] = str_1[x]
                    elif ind == 3:
                        d_3[keys[x]] = str_1[x]
                    elif ind == 4:
                        d_4[keys[x]] = str_1[x]
        return json_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
