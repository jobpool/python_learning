import pytest
import os

if __name__ == "__main__":
    pytest.main(["./baidu","-s","--alluredir=report/result"])
    os.system("allure generate report/result/ -o report/html --clean")
    