import subprocess


def exec_philo(philo_command_line: list[str]) -> list[str]:
    proc = subprocess.run(
            philo_command_line,
            stdout=subprocess.PIPE,
            text=True
    )
    return proc.stdout.split('\n')[:-1]
