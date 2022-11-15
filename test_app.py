import os

os.environ["DATABASE_URL"] = "sqlite://"  # use an in-memory database for tests

import unittest
from flask import current_app
from app import create_app, db
from resources.requestsApp import (
    mcm_for,
)
from models.jokesmodel import JokeModel


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    # test status 200 in /jokes/
    def test_get_jokes(self):
        response = self.client.get("/jokes/", follow_redirects=True)
        assert response.status_code == 200

    # test of mcm function with a list and expected result.
    def test_mcm(self):
        lista = [1, 2, 3, 4, 5]
        resultado = mcm_for(lista)

        self.assertEqual(resultado, 60)
