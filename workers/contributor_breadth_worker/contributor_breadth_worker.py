#SPDX-License-Identifier: MIT
import os, subprocess
from datetime import datetime
import logging
import requests
import json
from urllib.parse import quote
from multiprocessing import Process, Queue

import pandas as pd
import sqlalchemy as s
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData
## You do NOT have to import the base worker 
## Especially right now, if you're not doing repo collection. 
## You might take out the "collection" function and make 
## a new file called `base_worker_contributor.py`
from workers.worker_base import Worker

class ValueWorker(Worker):
    def __init__(self, config={}):

        worker_type = "contributor_breadth_worker"

        # Define what this worker can be given and know how to interpret
        given = [['github_url']]
        models = ['value']

        # Define the tables needed to insert, update, or delete on
        data_tables = ['contributor_repo']
        operations_tables = ['worker_history', 'worker_job']


        # Run the general worker initialization
        super().__init__(worker_type, config, given, models, data_tables, operations_tables)


        '''
        self.config.update({
            'repo_directory': self.augur_config.get_value('Workers', 'facade_worker')['repo_directory']
        })
        '''

        self.tool_source = 'Contributor Breadth Worker'
        self.tool_version = '1.0.0'
        self.data_source = 'GitHub'

    '''
    Not sure if self and entry_info are anything other than standard broker task 
    information. 
    '''
    def contributor_breadth_model(self, entry_info, cntrb_id):
        """ Data collection and storage method
        """

        '''
        self.logger.info(entry_info)
        self.logger.info(repo_id)

        repo_path_sql = s.sql.text("""
            SELECT repo_id, CONCAT(repo_group_id || chr(47) || repo_path || repo_name) AS path
            FROM repo
            WHERE repo_id = :repo_id
        """)

        relative_repo_path = self.db.execute(repo_path_sql, {'repo_id': repo_id}).fetchone()[1]
        absolute_repo_path = self.config['repo_directory'] + relative_repo_path

        try:
            self.generate_value_data(repo_id, absolute_repo_path)
        except Exception as e:
            self.logger.error(e)

        '''

        contributor_sql = s.sql.text("""
            SELECT cntrb_id, gh_user_id, gh_repos_url from contributors 
            where gh_user_id is not null;  

        """)

        self.register_task_completion(entry_info, repo_id, "contributor_breadth")

    def get_cntrb_repos(self, cntrb_id):
        """Runs scc on repo and stores data in database

        :param repo_id: Repository ID
        :param path: Absolute path of the Repostiory
        """

        '''
        self.logger.info('Running `scc`....')
        self.logger.info(f'Repo ID: {repo_id}, Path: {path}')

        output = subprocess.check_output([self.config['scc_bin'], '-f', 'json', path])
        records = json.loads(output.decode('utf8'))

        for record in records:
            for file in record['Files']:
                repo_labor = {
                    'repo_id': repo_id,
                    'rl_analysis_date': datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
                    'programming_language': file['Language'],
                    'file_path': file['Location'],
                    'file_name': file['Filename'],
                    'total_lines': file['Lines'],
                    'code_lines': file['Code'],
                    'comment_lines': file['Comment'],
                    'blank_lines': file['Blank'],
                    'code_complexity': file['Complexity'],
                    'tool_source': self.tool_source,
                    'tool_version': self.tool_version,
                    'data_source': self.data_source,
                    'data_collection_date': datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
                }

                result = self.db.execute(self.repo_labor_table.insert().values(repo_labor))
                self.logger.info(f"Added Repo Labor Data: {result.inserted_primary_key}")
        '''

        '''

        PSEUDO CODE

        **you probably need to do github API collection in some similar 
        ** way as the current base_worker.py ... you'd just rewrite it 
        ** in your base_worker_contributors.py file to be relevant to 
        ** non-repo-centric collection. 

        URL: To get a person's info about repos contributed to: 
            curl -H "Authorization: token APIKEY" https://api.github.com/users/ABrain7710
            curl -H "Authorization: token YOURTOKEN" https://api.github.com/users/ABrain7710
            *curl -H "Authorization: token YOURTOKEN" https://api.github.com/users/ABrain7710/events 


        FROM EVENTS URL: 
        "id"
        "type"
        "repo.id" "repo block"
        "repo.name" "repo block"
        "repo.url" "repo block"
        "created_at"

        FULL JSON: 

              {
    *"id": "14128914907",
    *"type": "IssueCommentEvent",
    "actor": {
      "id": 61482022,
      "login": "ABrain7710",
      "display_login": "ABrain7710",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ABrain7710",
      "avatar_url": "https://avatars.githubusercontent.com/u/61482022?"
    },
    "repo": {
      *"id": 78134122,
      *"name": "chaoss/augur",
      *"url": "https://api.github.com/repos/chaoss/augur"
    },
    "payload": {
      "action": "created",
      "issue": {
        "url": "https://api.github.com/repos/chaoss/augur/issues/991",
        "repository_url": "https://api.github.com/repos/chaoss/augur",
        "labels_url": "https://api.github.com/repos/chaoss/augur/issues/991/labels{/name}",
        "comments_url": "https://api.github.com/repos/chaoss/augur/issues/991/comments",
        "events_url": "https://api.github.com/repos/chaoss/augur/issues/991/events",
        "html_url": "https://github.com/chaoss/augur/issues/991",
        "id": 734083207,
        "node_id": "MDU6SXNzdWU3MzQwODMyMDc=",
        "number": 991,
        "title": "Contributors endpoint does not show commits data",
        "user": {
          "login": "sgoggins",
          "id": 379847,
          "node_id": "MDQ6VXNlcjM3OTg0Nw==",
          "avatar_url": "https://avatars3.githubusercontent.com/u/379847?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/sgoggins",
          "html_url": "https://github.com/sgoggins",
          "followers_url": "https://api.github.com/users/sgoggins/followers",
          "following_url": "https://api.github.com/users/sgoggins/following{/other_user}",
          "gists_url": "https://api.github.com/users/sgoggins/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/sgoggins/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/sgoggins/subscriptions",
          "organizations_url": "https://api.github.com/users/sgoggins/orgs",
          "repos_url": "https://api.github.com/users/sgoggins/repos",
          "events_url": "https://api.github.com/users/sgoggins/events{/privacy}",
          "received_events_url": "https://api.github.com/users/sgoggins/received_events",
          "type": "User",
          "site_admin": false
        },
        "labels": [
          {
            "id": 867527606,
            "node_id": "MDU6TGFiZWw4Njc1Mjc2MDY=",
            "url": "https://api.github.com/repos/chaoss/augur/labels/API",
            "name": "API",
            "color": "c2e0c6",
            "default": false,
            "description": "Related to Augur's metrics API"
          },
          {
            "id": 512453059,
            "node_id": "MDU6TGFiZWw1MTI0NTMwNTk=",
            "url": "https://api.github.com/repos/chaoss/augur/labels/bug",
            "name": "bug",
            "color": "f4abef",
            "default": true,
            "description": "Documents unexpected/wrong/buggy behavior"
          }
        ],
        "state": "open",
        "locked": false,
        "assignee": {
          "login": "ABrain7710",
          "id": 61482022,
          "node_id": "MDQ6VXNlcjYxNDgyMDIy",
          "avatar_url": "https://avatars0.githubusercontent.com/u/61482022?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/ABrain7710",
          "html_url": "https://github.com/ABrain7710",
          "followers_url": "https://api.github.com/users/ABrain7710/followers",
          "following_url": "https://api.github.com/users/ABrain7710/following{/other_user}",
          "gists_url": "https://api.github.com/users/ABrain7710/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/ABrain7710/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/ABrain7710/subscriptions",
          "organizations_url": "https://api.github.com/users/ABrain7710/orgs",
          "repos_url": "https://api.github.com/users/ABrain7710/repos",
          "events_url": "https://api.github.com/users/ABrain7710/events{/privacy}",
          "received_events_url": "https://api.github.com/users/ABrain7710/received_events",
          "type": "User",
          "site_admin": false
        },
        "assignees": [
          {
            "login": "ABrain7710",
            "id": 61482022,
            "node_id": "MDQ6VXNlcjYxNDgyMDIy",
            "avatar_url": "https://avatars0.githubusercontent.com/u/61482022?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/ABrain7710",
            "html_url": "https://github.com/ABrain7710",
            "followers_url": "https://api.github.com/users/ABrain7710/followers",
            "following_url": "https://api.github.com/users/ABrain7710/following{/other_user}",
            "gists_url": "https://api.github.com/users/ABrain7710/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/ABrain7710/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/ABrain7710/subscriptions",
            "organizations_url": "https://api.github.com/users/ABrain7710/orgs",
            "repos_url": "https://api.github.com/users/ABrain7710/repos",
            "events_url": "https://api.github.com/users/ABrain7710/events{/privacy}",
            "received_events_url": "https://api.github.com/users/ABrain7710/received_events",
            "type": "User",
            "site_admin": false
          }
        ],
        "milestone": null,
        "comments": 0,
        "created_at": "2020-11-01T23:03:16Z",
        "updated_at": "2020-11-09T15:04:23Z",
        "closed_at": null,
        "author_association": "MEMBER",
        "active_lock_reason": null,
        "body": "Please help us help you by filling out the following sections as thoroughly as you can.\r\n\r\n**Description:**\r\nCommits are a type of contribution, but they are not captured in the contributors endpoint: \r\nhttp://augur.osshealth.io:5055/api/unstable/repos/25440/contributors\r\n\r\n",
        "performed_via_github_app": null
      },
      "comment": {
        "url": "https://api.github.com/repos/chaoss/augur/issues/comments/724069788",
        "html_url": "https://github.com/chaoss/augur/issues/991#issuecomment-724069788",
        "issue_url": "https://api.github.com/repos/chaoss/augur/issues/991",
        "id": 724069788,
        "node_id": "MDEyOklzc3VlQ29tbWVudDcyNDA2OTc4OA==",
        "user": {
          "login": "ABrain7710",
          "id": 61482022,
          "node_id": "MDQ6VXNlcjYxNDgyMDIy",
          "avatar_url": "https://avatars0.githubusercontent.com/u/61482022?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/ABrain7710",
          "html_url": "https://github.com/ABrain7710",
          "followers_url": "https://api.github.com/users/ABrain7710/followers",
          "following_url": "https://api.github.com/users/ABrain7710/following{/other_user}",
          "gists_url": "https://api.github.com/users/ABrain7710/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/ABrain7710/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/ABrain7710/subscriptions",
          "organizations_url": "https://api.github.com/users/ABrain7710/orgs",
          "repos_url": "https://api.github.com/users/ABrain7710/repos",
          "events_url": "https://api.github.com/users/ABrain7710/events{/privacy}",
          "received_events_url": "https://api.github.com/users/ABrain7710/received_events",
          "type": "User",
          "site_admin": false
        },
        "created_at": "2020-11-09T15:04:23Z",
        "updated_at": "2020-11-09T15:04:23Z",
        "author_association": "CONTRIBUTOR",
        "body": "It appears the contributors metric is not counting commits, because the cmt_ght_author_id column is NULL for all the rows in the table. I tried to look at the contributor worker, and I can't find where the cmt_ght_augur_id is being set. ",
        "performed_via_github_app": null
      }
    },
    "public": true,
    *"created_at": "2020-11-09T15:04:23Z",
    "org": {
      "id": 29740296,
      "login": "chaoss",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/chaoss",
      "avatar_url": "https://avatars.githubusercontent.com/u/29740296?"
    }
  },
