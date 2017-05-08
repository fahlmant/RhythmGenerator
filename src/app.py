from flask import Flask
from flask import render_template
import os
import sys
import subprocess
import generator
app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    generator.main()
    subprocess.Popen('mv something.ly static/something.ly', shell=True)
    subprocess.Popen('lilypond -f png static/something.ly', shell=True)
    subprocess.Popen('mv something.png static/something.png', shell=True)
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run('0.0.0.0')
