import time

import pytest

from common.common_util import CommonUtil
from common.requests_util import RequestUtil
from common.yaml_util import read_yaml


# @pytest.mark.usefixtures("exe_database_sql")
class Test(CommonUtil):
    # workAge = 10

    # @pytest.mark.smoke
    # @pytest.mark.skip(reason="无理由跳过")
    @pytest.mark.parametrize('caseinfo', read_yaml('testcases/product_manage/get_token.yaml'))
    def test_baili(self, caseinfo):
        # time.sleep(3)
        print("测试百里老师")
        print(caseinfo)
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method, url=url, params=data)
        result = res.json()
        print("获取统一的接口鉴权码:" + str(result))
        # flag = True
        # assert flag is True
        # raise Exception("百里老师又开车了？")

    # def test_xingyao(self, login, pm):
    #     # time.sleep(3)
    #     print("测试星瑶老师" + login + pm)
    #     assert 'a' in 'abc'
    #     # assert 1==1
    #     # raise Exception("星瑶老师又开车了？")
    #
    # # @pytest.mark.smoke
    # # @pytest.mark.skipif(workAge < 10, reason="工作经验少于10年跳过")
    # def test_yiran(self):
    #     # time.sleep(3)
    #     print("测试依然老师")
    #     assert 1<2

# class TestJiaoyu:
#     def test_01_mashang(self):
#         print("码尚教育")

# if __name__ == '__main__':
#     pytest.main()

