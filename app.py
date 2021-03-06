from flask import Flask, render_template
from models.edu import Edu

from mlab import mlab_connect

app = Flask(__name__)
mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/english')
def english():
    return render_template('english-center-list.html', filtered_english = Edu.objects())

if __name__ == '__main__':
  app.run(debug=True)
