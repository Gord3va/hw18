# схемы сериализации
from marshmallow import Schema, fields, ValidationError


def validate_integer(item):
    if type(item) != int:
        raise ValidationError("NO INT")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Integer(validate=validate_integer)
    rating = fields.Float()
    genre = fields.Nested('GenreSchema')
    director = fields.Nested('DirectorSchema')
    """nested – Schema instance, class, class name (string), dictionary,
     or callable that returns a Schema or dictionary. Dictionaries are converted with Schema.from_dict.
only – A list or tuple of fields to marshal. If None, all fields are marshalled. This parameter takes precedence over 
exclude.
exclude – A list or tuple of fields to exclude.
many – Whether the field is a collection of objects.
unknown – Whether to exclude, include, or raise an error for unknown fields in the data. Use EXCLUDE, INCLUDE or RAISE.
kwargs – The same keyword arguments that Field receives."""


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
