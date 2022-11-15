from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from resources.requestsApp import chuckNorrisJoke, dadJoke, RandomJokes
from db import db
from models.jokesmodel import JokeModel
from schemas import JokeSchema, IdSchema


blp = Blueprint("Jokes", "jokes", description="Radom jokes by chucknorris or dad")

# in this module, i write the method, get, post,put and delete for http://localhost/jokes/


@blp.route("/jokes/")
class joke(MethodView):
    @blp.route("/jokes/")
    @blp.arguments(JokeSchema, location="query")
    @blp.response(200, JokeSchema)
    def get(
        self,
    ):
        args = request.args
        path_param = args.get("choice", default="", type=int)
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
            db.session.add(jokes)
            db.session.commit()
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
            db.session.commit()
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
            db.session.delete(jokes)
            db.session.commit()
        except SQLAlchemyError:
            abort(400, message="Not foud id Joke")
        return {"message": "joke deleted"}, 200
