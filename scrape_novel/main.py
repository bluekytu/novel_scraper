
import json
from flask import Flask
from flask_restful import Resource, Api
import mysql.connector

app = Flask(__name__)

api = Api(app)


class create_dict(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


class SQL():
    def __init__(self):
        self.title = ""
        self.description = ""
        self.NovelDB = mysql.connector.connect(
            host="localhost",
            user="root",
            password="fahad1721",
            database="noveldata"
        )

    pass

    def getTitles(self):
        NovelCursor = self.NovelDB.cursor()

        sqlStatement = "SELECT * FROM NOVELS"
        NovelCursor.execute(sqlStatement)
        res = NovelCursor.fetchall()
        result = [i[1] for i in res]

        return result

    def getDesc(self):
        NovelCursor = self.NovelDB.cursor()

        sqlStatement = "SELECT * FROM NOVELS"
        NovelCursor.execute(sqlStatement)
        mydict = create_dict()
        res = NovelCursor.fetchall()
        for row in res:
            mydict.add("Title", ({row[1]}))
            mydict.add("Description", ({row[2]}))
        return mydict


sql = SQL()
mydict = sql.getDesc()
stud_json = json.dumps(mydict, indent=2, sort_keys=True)


class TestBench(Resource):
    def get(self):

        return stud_json


api.add_resource(TestBench, '/')
app.run(debug=True)
