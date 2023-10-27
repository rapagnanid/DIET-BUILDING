from flask import Flask, render_template, request, redirect, url_for
from usda_api import get_nutritional_data_in_real_time, translate_to_english

app = Flask(__name__)

# ...

@app.route('/search', methods=['GET', 'POST'])
def search_food():
    if request.method == 'POST':
        user_query_italian = request.form['query']
        user_query_english = translate_to_english(user_query_italian)
        return redirect(url_for('search_food', query=user_query_english))

    user_query = request.args.get('query')

    if user_query:
        nutritional_data = get_nutritional_data_in_real_time(user_query)
        return render_template('search_results.html', nutritional_data=nutritional_data)

    return render_template('search_results.html', nutritional_data=[])

# ...


@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


