def get_result_from_file(file_path: str) -> list[str]:
    result_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            result_list.append(line.rstrip('\n'))
    return result_list
