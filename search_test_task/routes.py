from flask import render_template, jsonify
from elasticsearch import Elasticsearch
from flask_apispec import marshal_with
from .models import Documents
from .schema import DocumentsSchema
from . import app, db, docs


es = Elasticsearch(
    'http://localhost:9200',
)


@app.route('/', methods=['GET'])
def index():
    """Визуальное отображение базы данных"""

    data = Documents.query.all()

    return render_template(
        'index.html',
        data=data,
    )


@app.route('/search/<value>/', methods=['GET'])
@marshal_with(DocumentsSchema(many=True))
def search_document(value):
    """Поиск документов по текстовому запросу"""

    try:
        resp = es.search(
            size=20, index='myindex-1', query={'match': {'text': value}}
        )

        list_id = []
        for hit in resp['hits']['hits']:
            num = '%(id)s' % hit['_source']
            list_id.append(int(num))

        list_data = (
            db.session.query(Documents)
            .filter(Documents.id.in_(list_id))
            .order_by(Documents.created_date)
            .all()
        )

        return list_data

    except Exception:
        return jsonify({'message': 'ERROR search'}), 404


@app.route('/remove/<id>/', methods=['DELETE'])
def delete_documents(id):
    """Удаление документа из базы данных и индекса"""

    try:
        document_in_db = Documents.query.filter_by(id=id).first()
        if document_in_db is None:
            return jsonify({'message': 'does not exist'})
        db.session.delete(document_in_db)
        db.session.commit()
        document_in_index = es.delete(index='myindex-1', id=id)
        return jsonify(
            {'message': f'delete {id} {document_in_db} {document_in_index}'}
        )
    except Exception:
        return jsonify({'message': 'ERROR delete'}), 404


# документация для ендпоинтов
docs.register(search_document)
docs.register(delete_documents)
