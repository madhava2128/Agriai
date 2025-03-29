from marshmallow import Schema, fields

class TranslationSchema(Schema):
    id = fields.Int(required=True)
    language = fields.Str(required=True)
    text = fields.Str(required=True)

class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

class DocumentSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(required=True)