from config import validador
from marshmallow import types, fields, validate

class ChangePasswordResquestDTO(validador.Schema):
    token = fields.String (requerid=True)
    #valido que sea string y ademas que no sea menor a 6 caracatetes
    password = fields.String(validate=validate.Length(min=6), requerid=True)

