import subprocess

if __name__ == '__main__':
    test_cases = list(range(1000,1041))
    test_cases.extend([0,1,2])
    for test_case in test_cases:
        subprocess.run(['cat', 'output/Triangle-%04d.out' % test_case])
        subprocess.run(['time', 'python3', 'solution.py'], stdin=open('input/Triangle-%04d.in' % test_case))
