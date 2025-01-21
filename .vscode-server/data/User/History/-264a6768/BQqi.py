# main.py

import my_package

my_package.function1()  # module1의 function1을 호출
my_package.function2()  # Module2의 function2를 호출

# package 3 내용
from my_package3 import module1, module2

print(module1.greet("철수"))
print(module2.farwell("영희"))
