#https://stackoverflow.com/questions/66611521/in-gitlab-is-it-possible-to-automatically-create-an-issue-from-a-pipeline
import gitlab
import os
import datetime
import pytz

gl = gitlab.Gitlab(os.environ['CI_SERVER_URL'], private_token=os.environ['PRIVATE_TOKEN'])
project = gl.projects.get(os.environ['CI_PROJECT_ID'])
now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
today = now.strftime('%Y/%m/%d')
details = f''' # 概要

{today}分のコミット

# 行ったこと

# 内容チェックリスト

- []
- []
'''


issue_details = {
        'title': f'{today} Enjoying Study',
        'description': details,
        'assignee_ids': [111, 222]
        }

issue = project.issues.create(issue_details )
