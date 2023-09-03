import argparse


def parse_command_line():
    parser = argparse.ArgumentParser(description='このスクリプトの説明')
    parser.add_argument('-p', '--philo', type=str, help="コマンドラインを指定")
    parser.add_argument('-f', '--file', type=str, help='実行結果のファイルパスを指定')
    parser.add_argument('-n', '--number', help='指定した哲学者の番号でgrep')
    parser.add_argument('-m', '--motion',  help='motionでgrep')
    parser.add_argument('-t', '--totalization', action='store_true', help='実行結果を集計')
    return parser.parse_args()
