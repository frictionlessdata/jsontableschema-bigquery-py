# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import os
from jtsbq import Table


# Credentials
client_email = os.environ['GOOGLE_CLIENT_EMAIL']
private_key = os.environ['GOOGLE_PRIVATE_KEY']

table = Table(
        client_email= client_email,
        private_key=private_key,
        project_id='jsontableschema-bigquery-py',
        dataset_id='test',
        table_id='test')
table.download('tmp/schema.json', 'tmp/data.csv')