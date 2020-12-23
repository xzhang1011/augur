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

        1. Call this endpoint to get the repo listing 
        2. Populate the repo listing in the contributors_repo table
        3. Consider if any of this is useful in the near term ... its a big JSON block... Things 
        sean kinda would like to get while we are here: 
            **a. name
            **b. full_name
            **c. forks_url (*need* an enumeration of forks)
            d. collaborators_url (and maybe the full list of collaborators now)
            e. branches_url
            f. stargazers_url
            g. contributors_url
            *g1. login from the contributors_url
            *g2. id value from the contributors_url
            *g3. node_id value from contributors_url
            h. subscribers_url
            *i. created_at
            j. homepage
            k. forks
            l. watchers
            m. default_branch
            n. license -- just the "key" value from the json
