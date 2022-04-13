from flask import Flask, render_template, request, flash
import ipaddress


app = Flask(__name__)
app.secret_key = "net"
'''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='images/favicon.png')
'''
@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/results', methods=["GET", "POST"])
def results():

    network = request.form['network']

    net = list(ipaddress.ip_network(network).hosts())

    hosts = f"There are {len(net):,} usable hosts"
    
    network_add = network
    first_host = net[0]
    last_host = net[-1]
    broadcast = net[-1] +1

    range = f"Host Range: {first_host} to {last_host}"
    
    return render_template('results.html', network_add=network_add, hosts=hosts, range=range, broadcast=broadcast)


if __name__ == '__main__':
    app.run()

    

