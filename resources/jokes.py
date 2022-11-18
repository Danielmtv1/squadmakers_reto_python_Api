from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from resources.requestsApp import chuckNorrisJoke, dadJoke, RandomJokes
from db import db
from models.jokesmodel import JokeModel, save_to_db, update_to_db, delete_from_db
from schemas import JokeSchema, IdSchema, JokeSchemaChoice

blp = Blueprint("Jokes", "jokes", description="Radom jokes by chucknorris or dad")

# in this module, i write the method, get, post,put and delete for http://localhost/jokes/


@blp.route("/jokes/")
class joke(MethodView):
    @blp.route("/jokes/")
    @blp.arguments(JokeSchemaChoice, location="query")
    @blp.response(200, JokeSchema)
    def get(self, *args):
        args = request.args
        path_param = args.get("choice", default="", type=str)
        if path_param == "Dad":
            try:
                return jsonify(dadJoke()), 201
            except KeyError:
                abort(404, menssage=" Jokes not found ")
        elif path_param == "Chuck":
            try:
                return jsonify(chuckNorrisJoke()), 201
            except KeyError:
                abort(404, menssage="jokes not found")
        else:
            try:
                joke = RandomJokes()
                return jsonify(joke)
            except KeyError:
                abort(404, menssage=" Jokes not found ")

    @blp.arguments(JokeSchema)
    @blp.response(201, JokeSchema)
    def post(self, jokes):
        jokes = JokeModel(joke=RandomJokes())
        try:
            save_to_db(jokes)
        except IntegrityError:
            abort(
                400,
                message="A joke with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the joke.")

        return jokes

    @blp.arguments(IdSchema, location="query")
    @blp.response(201, IdSchema)
    def put(
        self,
        *args,
    ):
        args = request.args
        id = args.get("id", default="", type=int)
        try:
            query = db.session.query(JokeModel)
            joke_filter = query.filter(JokeModel.id == id).first()
            joke_filter.joke = joke_filter.joke = RandomJokes()
            # actualizar
            update_to_db()
        except IntegrityError:
            abort(
                400,
                message="id not found",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the joke.")

        return joke_filter

    @blp.arguments(IdSchema, location="query")
    def delete(
        self,
        *args,
    ):
        args = request.args
        id = args.get("id", default="", type=int)
        try:
            jokes = JokeModel.query.get_or_404(id)
            delete_from_db(jokes)
        except SQLAlchemyError:
            abort(400, message="Not foud id Joke")
        return {"message": "joke deleted"}, 200
