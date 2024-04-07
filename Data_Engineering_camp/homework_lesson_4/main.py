from flask import Flask, jsonify, request

app = Flask(__name__)
records = []

@app.route('/api/add_record/<record>', methods=['POST'])
def add_record(record):
    records.append(record)
    return f'New added record: {record}'

@app.route('/api/last_10_records', methods=['GET'])
def last_10_records():
    return jsonify({'last 10 added records': records[-10:]})

@app.route('/api/delete_record/<record>', methods=['DELETE'])
def delete_record(record):
    if record in records:
        records.remove(record)
        return f'Removed record: {record}'
    else:
        return f'Record {record} not found', 404

if __name__ == '__main__':
    app.run(debug=True, port = 5000)