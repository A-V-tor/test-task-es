import os
from datetime import datetime
import csv
from elasticsearch import Elasticsearch
from search_test_task import db, app
from search_test_task.models import Documents
from config import basedir


file_csv = os.path.join(basedir, 'posts.csv')


def fill_data_base():
    """ Наполнение базы данных и индекса данными """
    
    app.app_context().push()

    es = Elasticsearch(
        'http://localhost:9200',
    )

    with open(file_csv) as f:
        for i, row in enumerate(csv.reader(f)):
            # пропуск первой строки-оглавления
            if i == 0:
                continue
            text = row[0]
            date = datetime.strptime(str(row[1]), '%Y-%m-%d %H:%M:%S')
            rubrics = row[2]

            # запись в индекс
            doc = {
                'id': i,
                'text': text,
            }
            es.index(index='myindex-1', id=i, document=doc)

            # запись в базу данных

            document = Documents(rubrics=rubrics, text=text, created_date=date)
            db.session.add(document)

        db.session.commit()
