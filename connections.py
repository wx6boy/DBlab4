import json
import psycopg2
import datetime

def main_conn():
    conn = psycopg2.connect(
                database="postgres",
                user="postgres",
                password="",
                host="127.0.0.1",
                port="5432"
            )
    return conn


def user_conn():
    conn = psycopg2.connect(
        database="lab4",
        user="wx6boy",
        password="",
        host="127.0.0.1",
        port="5432"
    )
    return conn


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return str(obj)
        return json.JSONEncoder.default(self, obj)