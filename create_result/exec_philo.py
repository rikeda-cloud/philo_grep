import subprocess


def exec_philo(philo_command_line: list[str]) -> list[str]:
    proc = subprocess.run(
            philo_command_line,
            stdout=subprocess.PIPE,
            text=True
    )
    with open('log/' + '_'.join(philo_command_line[1:]), 'w') as f:
        f.writelines(proc.stdout)
    return proc.stdout.split('\n')[:-1]
