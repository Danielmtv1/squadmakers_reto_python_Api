from marshmallow import Schema, fields, exceptions


class JokeSchema(Schema):

    id = fields.Int(dump_only=True)
    joke = fields.Str()


class IdSchema(Schema):

    id = fields.Int()
    joke = fields.Str(dump_only=True)


class JokeSchemaChoice(fields.Str):
    args = fields.Str()


class JokeUpdateSchema(Schema):
    joke = fields.Str(dump_only=True)


class SumOneSchema(Schema):
    number = fields.Int()


class DelimitedListField(fields.Str):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _deserialize(self, value, attr, data, **kwargs):
        value = value[0]
        try:
            list = value.split(",")
            for item in list:
                fields.Int()._deserialize(item, attr, data, **kwargs)
            return list
        except AttributeError:
            raise exceptions.ValidationError(
                f"{attr} is not a delimited list it has a non string value {value}."
            )


class MCMSchema(Schema):
    numbers = DelimitedListField()
