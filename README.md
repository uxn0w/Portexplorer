<img src="/Resource/Logo.jpg" alt="OUT Data" border="0" />

<img src="https://img.shields.io/badge/version-1.0r-green" alt="Version app"> <img src="https://img.shields.io/badge/python-3.6+-blue" alt="Python version"> <img src="https://img.shields.io/badge/platform-Cross-%23989898" alt="Platform"> <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL v3-critical" alt="License"></a>

## Usage & CLI
Launch pexpl.py without arguments

````
> python3 ./pexpl.py
````
Launch pexpl.py with arguments

````
> python3 ./pexpl.py -help

Usage: python3 ./portexplorer.py {-m MODE} {-r RANGE} [-t TARGETS]

MODE -m:
    0: Normal 80 threads (Default)
    1: Faster 100 threads
    2: Ultra  130 threads

PORT RANGE -r:
    0: 1-9999 ports (Default)
    1: 1-49150 ports

> python3 ./pexpl.py -t target1 target2
> python3 ./pexpl.py -m 1 target1
> python3 ./pexpl.py -m 2 -r 1 target1 target2 target3 
````
