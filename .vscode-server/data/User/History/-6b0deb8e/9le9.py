# my_package/__init__.py
from .module1 import greet
from .module2 import farewell

print("my_package가 로드되었습니다.")

__all__ = ['greet', 'farewell']