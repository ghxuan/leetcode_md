# import os
# import time

import sys
import json
import getopt
import sqlite3
import requests
import datetime
from requests_toolbelt import MultipartEncoder

from srv.settings import *


# s = time.time()


# noinspection SqlInsertValues
class LEETCode:
    def __init__(self):
        self.con = sqlite3.connect('leetcode.db')
        self.cur = self.con.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS questions (id text, title text, titleSlug text, '
            'articleLive text, articleSlug text, level text, totalSubmitted text, totalAcs text, '
            'frontendId text, translatedTitle text, content text, translatedContent text, codeSnippets text)')
        self.hea = {
            'referer': 'https://leetcode-cn.com',
            'user-agent': 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        }
        self.leave = {1: '简单', 2: '中等', 3: '困难'}
        self.cookies = None
        # self.get_cookies()
        # self.login()
        # self.get_questions()
        # self.get_question('customers-who-bought-all-products')
        # self.re_get()
        pass

    def re_get(self):
        self.cur.execute('DROP TABLE questions')
        self.con.commit()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS questions (id text, title text, titleSlug text, '
            'articleLive text, articleSlug text, level text, totalSubmitted text, totalAcs text, '
            'frontendId text, translatedTitle text, content text, translatedContent text, codeSnippets text)')
        self.get_cookies()
        self.login()
        self.get_questions()
        pass

    # 获取初次登陆的cookie
    def get_cookies(self):
        res = requests.get('https://leetcode-cn.com/accounts/login/?next=%2Fproblemset%2Fall%2F',
                           headers=self.hea)
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
        # response = {"operationName": "getQuestionTranslation",
        #             "variables": {},
        #             "query":
        #                 "query getQuestionTranslation($lang: String) "
        #                 "{\n  translations: allAppliedQuestionTranslations(lang: $lang) "
        #                 "{\n    title\n    question "
        #                 "{\n      questionId\n      __typename\n    }\n    __typename\n  }\n}\n"}
        # res = requests.post('https://leetcode-cn.com/graphql',
        #                     headers=hea,
        #                     cookies=self.cookies,
        #                     data=json.dumps(response))
        all_res = requests.get('https://leetcode-cn.com/api/problems/all/',
                               headers=hea,
                               cookies=self.cookies)
        level = {1: '简单', 2: '中等', 3: '困难'}
        # title = dict((
        #     (int(question['question']['questionId']), question['title'])
        #     for question in json.loads(res.text)['data']['translations']
        #     if question['title']))
        # parameters = [(status['stat']['question_id'], title.get(status['stat']['question_id'], 'null'),
        #                status['stat']['question__title'], status['stat']['question__title_slug'],
        #                status['stat']['question__article__live'], status['stat']['question__article__slug'],
        #                level[status['difficulty']['level']], status['stat']['total_submitted'],
        #                status['stat']['total_acs'], status['stat']['frontend_question_id'])
        #               for status in json.loads(all_res.text)['stat_status_pairs']]
        # for para in parameters[::-1]:
        #     print(para)
        #     self.get_question(para[3])
        for status in json.loads(all_res.text)['stat_status_pairs'][::-1]:
            title = status['stat']['question__title'].replace("'", '"')
            print(status['stat']['question_id'], status['stat']['frontend_question_id'], title)
            self.cur.execute(
                f"INSERT INTO questions(id, title, titleSlug, articleLive, articleSlug, level, totalSubmitted, "
                f"totalAcs, frontendId, translatedTitle, content, translatedContent) "
                f"VALUES ('{status['stat']['question_id']}', '{title}"
                f"', '{status['stat']['question__title_slug']}', '{status['stat']['question__article__live']}', "
                f"'{status['stat']['question__article__slug']}', '{level[status['difficulty']['level']]}', "
                f"'{status['stat']['total_submitted']}', '{status['stat']['total_acs']}', "
                f"'{status['stat']['frontend_question_id']}', "
                f"'{self.get_question(status['stat']['question__title_slug'])}')")
        self.con.commit()
        pass

    # 获取单个题的标题和题
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
            "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    "
                     "questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n   "
                     " translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    "
                     "dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      "
                     "profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags "
                     "{\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n "
                     "   codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n "
                     "   hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n   "
                     " sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    "
                     "enableRunCode\n    enableTestMode\n    envInfo\n    __typename\n  }\n}\n "
        }

        response['variables']['titleSlug'] = slug
        res = requests.post('https://leetcode-cn.com/graphql',
                            headers=hea,
                            cookies=self.cookies,
                            data=json.dumps(response))
        data = json.loads(res.text)['data']['question']
        # return (data.get('translatedTitle', data["title"]), data["content"],
        #         data.get('translatedContent', data["content"]), str(data["codeSnippets"]))
        if data["content"]:
            temp = "', '".join((data.get('translatedTitle', data["title"]),
                                data["content"].replace("'", '"'),
                                data['translatedContent']))
        else:
            temp = "', '".join((data['title'] if data['translatedTitle'] is None else data['translatedTitle'],
                                '', ''))
        return temp

    def write_md(self, date=None, slug=None, title=None, frontend_id=None, translated_title=None, code='Python3'):
        where = [f'title="{title}"' if title is not None else '',
                 f'titleSlug="{slug}"' if slug is not None else '',
                 f'frontendId="{frontend_id}"' if frontend_id is not None else '',
                 f'translatedTitle="{translated_title}"' if translated_title is not None else '']
        where = 'WHERE ' + ' AND '.join(filter(lambda x: x, where)) if set(where) != {''} else ''
        self.cur.execute(f'SELECT frontendId, translatedTitle, title, titleSlug, translatedContent '
                         f'FROM questions {where}')
        temps = self.cur.fetchall()
        if not temps:
            print("请输入正确的中文标题或该题的序号或英文标题\n"
                  "假如输入正确的标题后还无法生成正确的md文件，"
                  "请输入python get_questions.py --reset 后，"
                  "再运行生成md文件的代码")
            return
        for temp in temps:
            frontend_id, translated_title, title, title_slug, translated_content = temp
            # print(frontend_id, translated_title, title, title_slug)
            if translated_content == '':
                print('该题是会员题，请账号充值会员后再看')
            with open(f'{frontend_id}、{title_slug}.md', 'w+', encoding='utf-8') as f:
                if date is None:
                    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                f.write(
                    f'---\ntitle: leetcode : {translated_title if translated_title else title}\ndate: {date}\n'
                    f'tags: [{code}, Leetcode]\n---\n\n')
                f.write(f'[{translated_title if translated_title else title}]'
                        f'(https://leetcode-cn.com/problems/{title_slug}/)\n\n')
                f.write(translated_content.replace('</p>', '</p>\n\n<!-- more -->', 1))
                f.write('\n' * 3)
                print(frontend_id, translated_title, title, title_slug, "已添加完成")
        pass


def main():
    lee = LEETCode()
    # print(sys.argv[1:])
    opts, args = getopt.getopt(sys.argv[1:],
                               "ac:i:rs:t:d:",
                               ["reset", "all", "title=", "id=", "chinese=", "slug=", "date="])
    opts = dict(opts)
    if '--reset' in opts or '-r' in opts:
        lee.re_get()
    if '--all' in opts or '-a' in opts:
        lee.write_md()
    elif '-i' in opts or '--id' in opts or '-t' in opts or '--title' in opts or '-c' in opts or '--chinese' in opts or \
            '-s' in opts or '--slug' in opts:
        translated_title = opts.get('--chinese', opts.get('-c', None))
        frontend_id = opts.get('--id', opts.get('-i', None))
        title = opts.get('--title', opts.get('-t', None))
        slug = opts.get('--slug', opts.get('-s', None))
        date = opts.get('--date', opts.get('-d', None))
        lee.write_md(date=date, slug=slug, title=title, frontend_id=frontend_id, translated_title=translated_title)
    # print(opts, args)
    # lee.write_md()
    # print(time.time() - s)
    # 447.82914447784424
    # 480.8169491291046


if __name__ == '__main__':
    main()
