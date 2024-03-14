import pytest


@pytest.fixture(scope="function", autouse=False, name='um')
def user_manage():
    print("用户管理之前的准备工作")
    yield "用户管理"
    print("用户管理之后的扫尾工作")