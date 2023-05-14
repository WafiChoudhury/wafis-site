from flask import Flask, render_template

# using flask allows us to pass specific data for each variable to the same index.html file
app = Flask(__name__)

# function to get data from postgresql database


@app.route('/')
def home_page():
    # creating plotly figure and passing it to index.html, use sql query to get data from database
    return render_template('index.html')


# specifiying host and port
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
