import os
import time

import pytest

if __name__ == '__main__':
    # pytest.main(["-vs"])
    pytest.main(["--junitxml=outputs/result.xml"])
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")
