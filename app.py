from flask import Flask, render_template, request, redirect, url_for
from storage_csv import StorageCsv

app = Flask(__name__)
storage = StorageCsv('movies.csv')

@app.route('/')
def index():
    movies = storage.list_movies()
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        rating = request.form['rating']
        poster = request.form['poster']
        storage.add_movie(title, year, rating, poster)
        return redirect(url_for('index'))
    return render_template('add_movie.html')

@app.route('/update/<title>', methods=['GET', 'POST'])
def update_movie(title):
    if request.method == 'POST':
        rating = request.form['rating']
        storage.update_movie(title, rating)
        return redirect(url_for('index'))
    return render_template('update_movie.html', title=title)

@app.route('/delete/<title>')
def delete_movie(title):
    storage.delete_movie(title)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
