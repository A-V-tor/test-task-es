from marshmallow import Schema, fields


class DocumentsSchema(Schema):
    """Схема сериализации документа"""

    id = fields.Integer()
    rubrics = fields.String()
    text = fields.String()
    created_date = fields.DateTime()
