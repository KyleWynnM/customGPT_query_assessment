from flask import Flask, request, jsonify

# initialize flask object
app = Flask(__name__)

# define service endpoint route
@app.route('/s', methods=['GET'])
def test_service():
    # get the value of the 'q' query parameter from the request URL
    query = request.args.get('q')

    # process the query parameter
    result = process_query(query)

    # return the result as JSON
    return jsonify({'result': result})

# process query
def process_query(query):
    # open query database
    medical_questions = open('medical-questions', 'r')
    # initialize array of suggestions
    suggestions = []

    # as the database is sorted by search numbers and not alphabetically, simply read
    # down the list and check if the term matches the current query
    # this order of reading ensures you get the four most popular results
    while len(suggestions) < 4:
        current_line = medical_questions.readline()

        # splice the current line to just be the length of the current query to see if it matches
        if current_line[:len(query)] == query:
            # append just the term, not the number
            suggestions.append(current_line.split("\t")[0])

    return suggestions

if __name__ == '__main__':
    app.run(debug=True)
