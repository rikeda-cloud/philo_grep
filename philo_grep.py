import re
import argparse
import subprocess


def parse_command_line():
    parser = argparse.ArgumentParser(description='このスクリプトの説明', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-p', '--philo', type=str, help="コマンドラインを指定")
    parser.add_argument('-f', '--file', type=str, help='実行結果のファイルパスを指定')
    parser.add_argument('-n', '--number', help='指定した哲学者の番号でgrep')
    parser.add_argument('-m', '--motion',  help='motionでgrep')
    return parser.parse_args()


def exec_philo(philo_command_line: list[str]) -> list[str]:
    proc = subprocess.run(
            philo_command_line,
            stdout=subprocess.PIPE,
            text=True
    )
    return proc.stdout.split('\n')[:-1]


def get_result(file_path: str) -> list[str]:
    result_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            result_list.append(line.rstrip('\n'))
    return result_list


class ResultGrep():
    def __init__(self, result: list[str]):
        self.result = result

    def check_result(self) -> bool:
        motion_list = ['eating', 'sleeping', 'taken', 'thinking', 'died']
        pattern = "|".join(map(re.escape, motion_list))
        for line in self.result:
            if line == '':
                continue
            if not re.search(pattern, line):
                print(f"予期しない文字列\"{line}\"が含まれています")
                return True
        return False

    def print_result(self):
        for line in self.result:
            print(line)

    def grep_result(self, args):
        if args.number:
            self.result = [line for line in self.result if line.split(' ')[1] == args.number]
        if args.motion:
            self.result = [line for line in self.result if args.motion in line]

def main():
    args = parse_command_line()
    if args.philo:
        result = exec_philo(args.philo.split(' '))
    elif args.file:
        result = get_result(args.file)
    else:
        print("Please enter required option argument p or f")
        exit(1)
    grep = ResultGrep(result)
    if grep.check_result():
        exit(1)
    grep.grep_result(args)
    grep.print_result()


if __name__ == '__main__':
    main()
