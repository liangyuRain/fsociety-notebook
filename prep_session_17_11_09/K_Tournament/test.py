import subprocess

if __name__ == '__main__':
    test_cases = list(range(1000,1040))
    for test_case in test_cases:
        subprocess.run(['cat', 'output/TournamentWins-%d.out' % test_case])
        subprocess.run(['time', 'python3', 'solution.py'], stdin=open('input/TournamentWins-%d.in' % test_case))
