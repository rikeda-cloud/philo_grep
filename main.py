from get_result_from_file import get_result_from_file
from parse_command_line import parse_command_line
from exec_philo import exec_philo
from result_grep import ResultGrep


def main():
    args = parse_command_line()
    if args.philo:
        result = exec_philo(args.philo.split(' '))
    elif args.file:
        result = get_result_from_file(args.file)
    else:
        print("Please enter required option argument p or f")
        exit(1)
    grep = ResultGrep(result)
    if grep.check_result():
        exit(1)
    if args.totalization:
        grep.totalization_result()
    else:
        grep.grep_result(args)


if __name__ == '__main__':
    main()
