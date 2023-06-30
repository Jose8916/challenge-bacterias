import sys
sys.dont_write_bytecode = True # Evita crear la cache
from flask import Flask, request, jsonify
from bacterias import calcular_poblacion_bacteriana

app = Flask(__name__)

@app.route('/calcular_poblacion', methods=['POST'])
def calcular_poblacion():
    data = request.json
    bacterias = data['bacterias']
    dias = data['dias']
    poblacion, bacterias = calcular_poblacion_bacteriana(bacterias, dias)
    resultado = {'poblacion': poblacion, 'bacterias': bacterias}
    return jsonify(resultado)

if __name__ == '__main__':
    app.run()

