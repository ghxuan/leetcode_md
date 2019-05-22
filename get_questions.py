import json
import requests


class Leetcode:
    def __init__(self):
        self.hea = {
            'referer': 'https://leetcode-cn.com',
            'user-agent': 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        }
        self.leave = {1: '简单', 2: '中等', 3: '困难'}
        self.cookies = self.get_cookies()
        self.hea['x-csrftoken'] = self.cookies.get('csrftoken')
        self.login()
        pass

    def get_cookies(self):
        res = requests.get('https://leetcode-cn.com/accounts/login/?next=%2Fproblemset%2Fall%2F',
                           headers=self.hea,
                           verify=False)
        return res.cookies

    # 获取中文标题和cookies/csrftoken
    def get_chinese_and_cookies(self):
        self.hea['content-type'] = 'application/json'
        response = {"operationName": "getQuestionTranslation",
                    "variables": {},
                    "query":
                        "query getQuestionTranslation($lang: String) "
                        "{\n  translations: allAppliedQuestionTranslations(lang: $lang) "
                        "{\n    title\n    question "
                        "{\n      questionId\n      __typename\n    }\n    __typename\n  }\n}\n"}
        res = requests.post('https://leetcode-cn.com/graphql',
                            headers=self.hea,
                            verify=False,
                            data=json.dumps(response))
        return dict((
            (int(question['question']['questionId']), question['title'])
            for question in json.loads(res.text)['data']['translations'])), res.cookies

    # 模拟登陆  更换cookies
    def login(self):
        self.hea['content-type'] = 'multipart/form-data; boundary=-----WebKitFormBoundaryETGpmlA09oWsdlBR'
        self.hea['referer'] = 'https://leetcode-cn.com/accounts/login/'
        self.hea['x-requested-with'] = 'XMLHttpRequest'
        response = {
            "csrfmiddlewaretoken": self.hea['x-csrftoken'],
            "login": "709808634@qq.com",
            "password": "709808634",
            "next": "/problems",
        }
        response = f"""------WebKitFormBoundaryETGpmlA09oWsdlBR
Content-Disposition: form-data; name="csrfmiddlewaretoken"

{self.hea['x-csrftoken']}
------WebKitFormBoundaryETGpmlA09oWsdlBR
Content-Disposition: form-data; name="login"

709808634@qq.com
------WebKitFormBoundaryETGpmlA09oWsdlBR
Content-Disposition: form-data; name="password"

709808634
------WebKitFormBoundaryETGpmlA09oWsdlBR
Content-Disposition: form-data; name="next"

/problems
------WebKitFormBoundaryETGpmlA09oWsdlBR--
"""
        print(response)
        res = requests.post('https://leetcode-cn.com/accounts/login/',
                            headers=self.hea,
                            cookies=self.cookies,
                            verify=False,
                            data=response)
        print(res.text)
        pass


if __name__ == '__main__':
    lee = Leetcode()
