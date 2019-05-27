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
        self.cookies = None
        # self.get_cookies()
        # self.login()
        # self.get_question('two-sum')
        self.re_get()
        pass

    def re_get(self):
        self.get_cookies()
        self.login()
        self.get_questions()
        pass

    # 获取初次登陆的cookie
    def get_cookies(self):
        res = requests.get('https://leetcode-cn.com/accounts/login/?next=%2Fproblemset%2Fall%2F',
                           headers=self.hea,
                           verify=False)
        self.cookies = res.cookies

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

    # 获取后台题号和中文标题并获取详细信息
    def get_questions(self):
        hea = {
            'x-csrftoken': self.cookies.get('csrftoken'),
            'content-type': 'application/json',
        }
        response = {"operationName": "getQuestionTranslation",
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
        all_res = requests.get('https://leetcode-cn.com/api/problems/all/',
                               headers=hea,
                               cookies=self.cookies,
                               verify=False)
        level = {1: '简单', 2: '中等', 3: '困难'}
        title = dict((
            (int(question['question']['questionId']), question['title'])
            for question in json.loads(res.text)['data']['translations']
            if question['title']))
        parameters = [(status['stat']['question_id'], title.get(status['stat']['question_id'], 'null'),
                       status['stat']['question__title'], status['stat']['question__title_slug'],
                       status['stat']['question__article__live'], status['stat']['question__article__slug'],
                       level[status['difficulty']['level']], status['stat']['total_submitted'],
                       status['stat']['total_acs'], status['stat']['frontend_question_id'])
                      for status in json.loads(all_res.text)['stat_status_pairs']]
        for para in parameters[::-1]:
            print(para)
            self.get_question(para[3])

    def get_question(self, slug):
        hea = {
            'x-csrftoken': self.cookies.get('csrftoken'),
            'content-type': 'application/json',
        }
        response = {
            "operationName": "questionData",
            "variables": {
                "titleSlug": ""
            },
            "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    __typename\n  }\n}\n"
        }

        response['variables']['titleSlug'] = slug
        res = requests.post('https://leetcode-cn.com/graphql',
                            headers=hea,
                            verify=False,
                            cookies=self.cookies,
                            data=json.dumps(response))
        data = json.loads(res.text)['data']['question']
        # print(data["codeSnippets"])
        # print(data["content"])
        # print(data["translatedContent"])
        print(data["title"], data.get('translatedTitle', 'null'))


if __name__ == '__main__':
    lee = Leetcode()
