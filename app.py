import psycopg2
import flask
from flask import request, jsonify

conn = psycopg2.connect(database="bsegf5gzh3uvewm75smv", user="upn7zorz7rny5qlmw8di", password="Kn463TU1YtWLbIstwXGS",
                        host="bsegf5gzh3uvewm75smv-postgresql.services.clever-cloud.com", port="5432")
cur = conn.cursor()
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/branches/autocomplete', methods=['POST', 'GET'])
def branch_details():
    branch = request.args.get('q')
    if request.args.get('limit') is None:
        limit = 3
    else:
        limit = request.args.get('limit')
    if request.args.get('offset') is None:
        offset = 0
    else:
        offset = request.args.get('offset')
    fetched_data = get_bank_details(branch, limit, offset)
    resp = jsonify(branches=filter_data(fetched_data))
    return resp


@app.route('/api/branches', methods=['POST', 'GET'])
def find_string_across_all_rows_n_column():
    string_to_search = request.args.get('q')
    if request.args.get('limit') is None:
        limit = 3
    else:
        limit = request.args.get('limit')
    if request.args.get('offset') is None:
        offset = 0
    else:
        offset = request.args.get('offset')
    fetched_data = get_bank_details_across_table(string_to_search, limit, offset)
    resp = jsonify(branches=filter_data(fetched_data))
    return resp


def filter_data(fetched_data):
    branches = []
    for i in fetched_data:
        d = dict()
        d["ifsc"] = i[0]
        d["bank_id"] = i[1]
        d["branch"] = i[2]
        d["address"] = i[3]
        d["city"] = i[4]
        d["district"] = i[5]
        d["state"] = i[6]
        branches.append(d)
    return branches


def get_bank_details(branch_name, limit, offset):
    s = "select * from branches where branch ~* '{}' ORDER BY ifsc ASC limit {} offset {};".format(branch_name, limit,
                                                                                                   offset)
    cur.execute(s)
    return cur.fetchall()


def get_bank_details_across_table(string_to_search, limit, offset):
    branch_name = string_to_search.upper()
    s = "select * from branches where ifsc='{}' OR branch='{}' OR city='{}' OR district='{}' OR state='{}' OR address='{}' ORDER BY ifsc ASC limit {} offset {};".format(
        branch_name, branch_name, branch_name, branch_name, branch_name, branch_name, limit, offset)
    cur.execute(s)
    return cur.fetchall()


if __name__ == '__main__':
    app.run(debug=True)
