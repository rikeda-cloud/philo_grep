# 使い方
## コマンドラインを実行する
### python philo_grep.py -p "./philo[\_bonus] number_of_philo time_to_die time_to_eat time_to_sleep [must_eat]"
## 実行結果が出力されたファイルから読み込む
### ./philo[\_bonus] number_of_philo time_to_die time_to_eat time_to_sleep [must_eat] > outfile
### python philo_grep.py -f outfile
## 哲学者の番号でgrepする
### python philo_grep.py -p "./philo 200 410 200 200 5" -n 42
## 文字列でgrepする
### python philo_grep.py -p "./philo 200 410 200 200 5" -m sleeping
## 特定の哲学者の特定の行動のみをgrepする
### python philo_grep.py -p "./philo 200 410 200 200 5" -n 42 -m sleeping
