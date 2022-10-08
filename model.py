from marshmallow import fields, validates_schema, Schema,ValidationError

from global_path import VALID_CMD_PARAMS


class RequestParam(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_param_cmd(self,values,*args,**kwargs):
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd" нет такого значения')

        return values

class QueryRequestValue(Schema):
    queries = fields.Nested(RequestParam,many=True)
