import json
from flask import request, jsonify
from resources.requestsApp import (
    mcm_for,
    comma_separated_params_to_list,
)
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import SumOneSchema, MCMSchema

blp = Blueprint(
    "Mathreto", "mathreto", description=" Api Math mcm of numbers and number +1"
)
# in this module, i write the method, get, for least common multiple and sum 1 for the number


@blp.route("/mcnNumbers")
class Mathmcm(MethodView):
    @blp.arguments(MCMSchema, location="query")
    def get(self, *args, **kwargs):
        number_str = request.args.get("numbers")
        if "," in number_str:
            numbers = map(int, number_str.split(","))
        else:
            numbers = [int(number_str)]

        resultmcm = str(mcm_for(numbers))

        return resultmcm


@blp.route("/sumOne")
class MathSumOne(MethodView):
    @blp.arguments(SumOneSchema, location="query")
    def get(self, *args, **kwargs):
        try:
            args = request.args
            number = args.get("number", default="", type=int)
            sumOne = str(number + 1)
            json.loads(sumOne)
            return jsonify(sumOne)
        except KeyError:
            abort(404, menssage="The sum not found")
