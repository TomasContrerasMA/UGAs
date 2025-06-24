
from flask import Flask, render_template
import pandas as pd
import folium
import os

app = Flask(__name__)

@app.route('/')
def show_table():

    df = pd.read_csv('denue_inegi_22_.csv', encoding='latin1')
    oxxos = df[df.raz_social == "CADENA COMERCIAL OXXO SA DE CV"]

    agebs = len(oxxos.ageb.unique())
    num_oxxos = len(oxxos)

    table_html = oxxos.to_html(classes='table table-striped table-bordered', index=False, max_rows=10)

    return render_template('table.html', table=table_html, agebs=agebs, num_oxxos=num_oxxos)

@app.route('/mapa_oxxos')
def mapa_oxxos():
    df = pd.read_csv('denue_inegi_22_.csv', encoding='latin1')
    oxxos = df[df.raz_social == "CADENA COMERCIAL OXXO SA DE CV"]

    mapa = folium.Map(location=[oxxos['latitud'].mean(), oxxos['longitud'].mean()], zoom_start=13)

    for _, row in oxxos.iterrows():
        folium.CircleMarker(
            location=[row['latitud'], row['longitud']],
            popup=row['nom_estab'],
            radius=5,
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(mapa)
    if not os.path.exists('static'):
        os.makedirs('static')
    mapa.save('static/mapa.html')
    return render_template('mapa.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


