# 使い方
## コマンドラインを実行する
### python main.py -p "./philo[\_bonus] number die eat sleep [must_eat]"
## 実行結果が出力されたファイルから読み込む
### ./philo 42 42 42 42 42 > outfile
### python main.py -f outfile
## 哲学者の番号でgrepする
### python main.py -p "./philo 42 42 42 42 42" -n 42
## 文字列でgrepする
### python main.py -p "./philo 42 42 42 42 42" -m sleeping
## 特定の哲学者の特定の行動のみをgrepする
### python main.py -p "./philo 42 42 42 42 42" -n 42 -m sleeping
## 哲学者の行動を集計
### python main.py -p "./philo 42 42 42 42 42" -t
