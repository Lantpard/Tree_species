from flask import Flask, render_template, request
import folium
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/trees')
def trees():
    return render_template('trees.html')

@app.route('/app')
def dash():
    star_coords = (4.430081,-75.2112492)

    folium_map = folium.Map(location=star_coords, zoom_start=13)
    #folium_map.save('src/templates/map.html')
    #html_string=folium_map.get_root().render()
    folium.Marker(
      location=[4.430081,-75.2112492],
      popup="leo",
   ).add_to(folium_map)
    html_string = folium_map._repr_html_()
    return render_template('app.html',folium_map=html_string)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)