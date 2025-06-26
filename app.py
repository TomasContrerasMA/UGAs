
from flask import Flask, render_template
import pandas as pd
import folium
import os

app = Flask(__name__)

@app.route('/')
def home():

    df = pd.read_csv('denue_inegi_22_.csv', encoding='latin1')
    oxxos = df[df.raz_social == "CADENA COMERCIAL OXXO SA DE CV"]

    table_html = oxxos.to_html(classes='table table-striped table-bordered', index=False, max_rows=10)

    return render_template('home.html', table=table_html)

@app.route('/flujo')
def flujo():
    return render_template('flujo.html')

@app.route('/auditadas')
def auditadas():
    return render_template('auditadas.html')

@app.route('/atractores')
def atractores():
    return render_template('atractores.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


