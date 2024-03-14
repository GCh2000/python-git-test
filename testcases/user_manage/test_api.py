import pytest
import requests

from common.common_util import CommonUtil
from common.requests_util import RequestUtil
from common.yaml_util import read_yaml


class TestApi(CommonUtil):

    access_token = ""

    # @pytest.mark.parametrize('arg1,arg2', [['name', '百里'], ['age', '18']])
    @pytest.mark.parametrize('caseinfo', read_yaml('testcases/user_manage/get_token.yaml'))
    def test_01_get_token(self, caseinfo):
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method, url=url, params=data)
        result = res.json()
        print("获取统一的接口鉴权码:" + str(result))
        # TestApi.access_token = res.json()['access_token']
        # assert 'access_token' in str(result)

    # @pytest.mark.parametrize('caseinfo', read_yaml('testcases/user_manage/edit_flag.yaml'))
    # def test_02_edit_flag(self, caseinfo):
    #     print("编辑标签接口：")
    #     name = caseinfo['name']
    #     method = caseinfo['request']['method']
    #     url = caseinfo['request']['url']+TestApi.access_token
    #     data = caseinfo['request']['data']
    #     validate = caseinfo['validate']
    #     res = RequestUtil.session.request(method=method, url=url, json=data)
    #     result = res.json()
    #     print(result)


