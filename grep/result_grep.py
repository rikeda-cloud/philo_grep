import re
from grep.philo import Philo


class ResultGrep():
    def __init__(self, result: list[str]):
        self.result = result

    def __get_number_of_philo(self):
        number_of_philo = 0
        for message in self.result:
            if number_of_philo < int(message.split(' ')[1]):
                number_of_philo = int(message.split(' ')[1])
        return number_of_philo

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

    def totalization_result(self):
        philo_list = []
        number_of_philo = self.__get_number_of_philo()
        for i in range(number_of_philo):
            philo_list.append(Philo())
        for message in self.result:
            philo_number = int(message.split(' ')[1]) - 1
            if 'taken' in message:
                philo_list[philo_number].add_taken(message)
            elif 'think' in message:
                philo_list[philo_number].add_think(message)
            elif 'eat' in message:
                philo_list[philo_number].add_eat(message)
            elif 'sleep' in message:
                philo_list[philo_number].add_sleep(message)
            elif 'die' in message:
                philo_list[philo_number].add_die(message)
        self.result = philo_list
        for i, philo in enumerate(self.result):
            print(f'--- philo[{i + 1:>3}] ---')
            print("[taken]")
            [print(message) for message in philo.taken[1]]
            print("[thinking]")
            [print(message) for message in philo.think[1]]
            print("[eating]")
            [print(message) for message in philo.eat[1]]
            print("[sleeping]")
            [print(message) for message in philo.sleep[1]]
            print("[died]")
            [print(message) for message in philo.die[1]]
        print(f' --------------------------------------')
        print(f' |  number  |taken|think|eat|sleep|die|')
        print(f' --------------------------------------')
        for i, philo in enumerate(self.result):
            print(f' |philo[{i + 1:>3}]|{philo.taken[0]:^5}|{philo.think[0]:^5}|{philo.eat[0]:^3}|{philo.sleep[0]:^5}|{philo.die[0]:^3}|')
        print(f' --------------------------------------')

    def grep_result(self, args):
        if args.number:
            self.result = [line for line in self.result if line.split(' ')[1] == args.number]
        if args.motion:
            self.result = [line for line in self.result if args.motion in line]
        for line in self.result:
            print(line)
