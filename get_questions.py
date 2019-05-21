import json
import requests


class Leetcode:
    def __init__(self):
        self.hea = {
            'content-type': 'application/json',
            'referer': 'https://leetcode-cn.com',
            'User-Agent': 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        }
        self.leave = {1: '简单', 2: '中等', 3: '困难'}
        self.title = {}
        pass

    def get_chinese(self):
        response = {"operationName": "getQuestionTranslation",
                    "variables": {},
                    "query":
                        "query getQuestionTranslation($lang: String) "
                        "{\n  translations: allAppliedQuestionTranslations(lang: $lang) "
                        "{\n    title\n    question "
                        "{\n      questionId\n      __typename\n    }\n    __typename\n  }\n}\n"}
        res = requests.post('https://leetcode-cn.com/graphql',
                            headers=self.hea,
                            data=json.dumps(response))
        self.title = dict((
            (int(question['question']['questionId']), question['title'])
            for question in json.loads(res.text)['data']['translations']))
        pass


if __name__ == '__main__':
    lee = Leetcode()
    lee.get_chinese()
