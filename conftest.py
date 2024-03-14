# 读取数据方法
import pytest


# def read_yaml():
#     return ['chenglong', 'zhengzidan', 'cai10']
#     # return [{'a': 'b'}]
#     # return 'Str'


# @pytest.fixture(scope="function", autouse=False, params=read_yaml(), ids=['c', 'z', 'cal'], name='db')
# def exe_database_sql(request):
#     # print(request.param)
#     print("执行SQL查询")
#     # return "success"
#     yield request.param
#     print("关闭数据库连接")

@pytest.fixture(scope="class", autouse=False, name='login')
def login_ecshop():
    print("登录前")
    yield "用户登录成功"
    print("登录后")

@pytest.fixture(scope="session", autouse=False, name='all')
def all_exe():
    print("all_exe之前")
    yield "用户登录成功"
    print("all_exe之后")
