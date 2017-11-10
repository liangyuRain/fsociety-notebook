import subprocess

if __name__ == '__main__':
    test_cases = list(range(1000,1009))
    # test_cases = list(range(0,3))
    test_cases.extend(range(2000,2006))

    for test_case in test_cases:
        subprocess.run(['cat', 'output/RacingGems-%04d.out' % test_case])
        subprocess.run(['time', 'java', 'Problem_G'], stdin=open('input/RacingGems-%04d.in' % test_case))
