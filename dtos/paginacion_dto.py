from config import validador
from marshmallow import fields


class PaginacionRequestDTO(validador.Schema):
    #load_default > sirve para que en el caso de no tenga valor esa
    #variable
    page = fields.Integer(required=False, load_default=1)
    perPage = fields.Integer(required= False, load_default=10)
