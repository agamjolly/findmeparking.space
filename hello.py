from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listings')
def listings():
    return render_template('listings.html')

@app.route('/lease')
def lease():
    return render_template('lease.html')

@app.route('/listing_la')
def listingsla():
    return render_template('listing_la.html')

@app.route('/listing_la2')
def listingslatwo():
    return render_template('listing_la2.html')

@app.route('/listing_la3')
def listingslathree():
    return render_template('listing_la3.html')

@app.route('/listing_ny')
def listingsny():
    return render_template('listing_ny.html')
  
@app.route('/listing_ny2')
def listingsnytwo():
    return render_template('listing_ny2.html')

@app.route('/listing_ny3')
def listingsnythree():
    return render_template('listing_ny3.html')

@app.route('/listing_sf')
def listingsf():
    return render_template('listing_sf.html')

@app.route('/listing_sf2')
def listingsftwo():
    return render_template('listing_sf2.html')

@app.route('/listing_sf3')
def listingsfthree():
    return render_template('listing_sf3.html')
  
@app.route('/newyork')
def newyork():
    return render_template('newyork.html')

@app.route('/sanfrancisco')
def sf():
    return render_template('sanfrancisco.html')

@app.route('/losangeles')
def la():
    return render_template('losangeles.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 