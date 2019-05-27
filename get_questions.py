import json
import requests
from requests_toolbelt import MultipartEncoder

from srv.settings import *


class Leetcode:
    def __init__(self):
        self.hea = {
            'referer': 'https://leetcode-cn.com',
            'user-agent': 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        }
        self.leave = {1: '简单', 2: '中等', 3: '困难'}
        self.cookies = self.get_cookies()
        self.login()
        for k, v in self.get_chinese().items():
            print(k, v)
        pass

    # 获取初次登陆的cookie
    def get_cookies(self):
        res = requests.get('https://leetcode-cn.com/accounts/login/?next=%2Fproblemset%2Fall%2F',
                           headers=self.hea,
                           verify=False)
        return res.cookies

    # 获取后台题号和中文标题
    def get_chinese(self):
        hea = {
            'x-csrftoken': self.cookies.get('csrftoken'),
            'content-type': 'application/json',
        }
        hea.update(self.hea)
        response = {
            "operationName": "getQuestionTranslation",
            "variables": {},
            "query":
                "query getQuestionTranslation($lang: String) "
                "{\n  translations: allAppliedQuestionTranslations(lang: $lang) "
                "{\n    title\n    question "
                "{\n      questionId\n      __typename\n    }\n    __typename\n  }\n}\n"}
        res = requests.post('https://leetcode-cn.com/graphql',
                            headers=hea,
                            cookies=self.cookies,
                            verify=False,
                            data=json.dumps(response))
        # print(res.text)
        return dict((
            (int(question['question']['questionId']), question['title'])
            for question in json.loads(res.text)['data']['translations']))

    # 模拟登陆  更换cookies
    def login(self):
        response = MultipartEncoder({
            "csrfmiddlewaretoken": self.cookies.get('csrftoken'),
            "login": login,
            "password": password,
            "next": "/problems",
        })
        hea = {
            'x-csrftoken': self.cookies.get('csrftoken'),
            'content-type': response.content_type,
            'referer': 'https://leetcode-cn.com/accounts/login/',
            'x-requested-with': 'XMLHttpRequest',
        }
        hea.update(self.hea)
        res = requests.post('https://leetcode-cn.com/accounts/login/',
                            headers=hea,
                            cookies=self.cookies,
                            verify=False,
                            data=response)
        self.cookies = res.cookies
        # print(res.text)
        pass


if __name__ == '__main__':
    lee = Leetcode()
