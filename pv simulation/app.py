from flask import Flask, request, jsonify, render_template
from simulation import pv_simulation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate')
def simulate():
    irradiance = float(request.args.get('irradiance', 1000))
    temperature = float(request.args.get('temperature', 25))
    V, I, P = pv_simulation(irradiance, temperature)
    data = {
        "voltage": V.tolist(),
        "current": I.tolist(),
        "power": P.tolist()
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
