# 使い方
## コマンドラインを実行する
### python philo_grep.py -p "./philo 42 42 42 42 42"
## 実行結果が出力されたファイルから読み込む
### ./philo 42 42 42 42 42 > outfile
### python philo_grep.py -f outfile
## 哲学者の番号でgrepする
### python philo_grep.py -p "./philo 42 42 42 42 42" -n 42
## 文字列でgrepする
### python philo_grep.py -p "./philo 42 42 42 42 42" -m sleeping
## 特定の哲学者の特定の行動のみをgrepする
### python philo_grep.py -p "./philo 42 42 42 42 42" -n 42 -m sleeping
