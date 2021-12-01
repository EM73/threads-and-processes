import sys
import os
import platform

"""
Python version: 3.8.5
Interpreter: CPython
Interpreter version: 3.8.5 (default, Jul 28 2020, 12:59:40) [GCC 9.3.0]
Operating system: Linux
Operating system version: 5.4.0-48-generic
Processor: x86_64
CPUs: 8
"""

#◦ (0pkt albo 1pkt) program poprawnie raportuje wersję języka Python,
print(f"Python version: {platform.python_version()}")
#◦ (0pkt albo 1pkt) program poprawnie raportuje używany interpreter,
print(f"Interpreter: {platform.python_implementation()}")
#◦ (0pkt albo 1pkt) program poprawnie raportuje wersję interpretera,
print(f"Interpreter version: {sys.version}")
#◦ (0pkt albo 1pkt) program poprawnie raportuje nazwę systemu operacyjnego,
print(f"Operating system: {platform.system()}")
#◦ (0pkt albo 1pkt) program poprawnie raportuje wersję systemu operacyjnego,
print(f"Operating system version: {platform.version()}")
#◦ (0pkt albo 1pkt) program poprawnie raportuje informacje o procesorze,
print(f"Processor: {platform.machine()}")
#◦ (0pkt albo 1pkt) program poprawnie raportuje liczbę dostępnych procesorów
print(f"CPUs: {os.cpu_count()}")
