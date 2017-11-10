import subprocess

if __name__ == '__main__':
    test_cases = list(range(1001,1006))
    test_cases.extend([0,1,2])
    for test_case in test_cases:
        subprocess.run(['cat', 'output/Excellence-%04d.out' % test_case])
        subprocess.run(['time', 'python3', 'solution.py'], stdin=open('input/Excellence-%04d.in' % test_case))
