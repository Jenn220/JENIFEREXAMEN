from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reino Cuántico - Alvarez</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 30px;
            padding: 50px;
            max-width: 900px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }
        
        h1 {
            text-align: center;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            margin-bottom: 10px;
        }
        
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 1.2em;
            margin-bottom: 40px;
        }
        
        .info-section {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
            padding: 30px;
            border-radius: 20px;
            margin-bottom: 30px;
            border-left: 5px solid #667eea;
        }
        
        .info-section h2 {
            color: #667eea;
            margin-bottom: 15px;
        }
        
        .info-section p {
            color: #555;
            line-height: 1.8;
            font-size: 1.1em;
        }
        
        .quantum-facts {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .fact-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .fact-card:hover {
            transform: translateY(-10px);
        }
        
        .fact-card h3 {
            color: #764ba2;
            margin-bottom: 10px;
        }
        
        .fact-card p {
            color: #666;
            font-size: 0.95em;
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
            font-style: italic;
        }
        
        .particle {
            display: inline-block;
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1><span class="particle">⚛️</span> .....jenii <span class="particle">⚛️</span></h1>
        <p class="subtitle">Explorando las maravillas de la mecánica cuántica</p>
        
        <div class="info-section">
            <h2>¿?</h2>
            <p>
                El reino cuántico es el mundo de lo infinitamente pequeño, donde las partículas 
                subatómicas se comportan de maneras que desafían nuestra intuición. En este reino, 
                las partículas pueden estar en múltiples lugares al mismo tiempo, atravesar barreras 
                sólidas y comunicarse instantáneamente a través de distancias infinitas.
            </p>
        </div>
        
        <div class="quantum-facts">
            <div class="fact-card">
                <h3>🌀 Superposición</h3>
                <p>Una partícula cuántica puede existir en múltiples estados simultáneamente hasta que es observada.</p>
            </div>
            
            <div class="fact-card">
                <h3>🔗 Entrelazamiento</h3>
                <p>Dos partículas pueden estar conectadas de tal manera que el estado de una afecta instantáneamente a la otra.</p>
            </div>
            
            <div class="fact-card">
                <h3>📏 Principio de Incertidumbre</h3>
                <p>Es imposible conocer simultáneamente la posición exacta y el momento de una partícula.</p>
            </div>
            
            <div class="fact-card">
                <h3>🌊 Dualidad Onda-Partícula</h3>
                <p>La luz y la materia exhiben propiedades tanto de ondas como de partículas.</p>
            </div>
            
            <div class="fact-card">
                <h3>🎯 Túnel Cuántico</h3>
                <p>Las partículas pueden atravesar barreras que clásicamente serían impenetrables.</p>
            </div>
            
            <div class="fact-card">
                <h3>💻 Computación Cuántica</h3>
                <p>Los ordenadores cuánticos utilizan qubits que pueden procesar información exponencialmente más rápido..</p>
            </div>
        </div>
        
        <div class="footer">
            <p>Proyecto CI/CD - Examen Final</p>
            <p>Desarrollado por Jenifer Alvarez</p>
            <p>Desplegado automáticamente con GitHub Actions + Docker + Traefik</p>
        </div>
    </div>
</body>
</html>
    '''

@app.route('/health')
def health():
    return {'status': 'ok', 'message': 'Reino Cuántico funcionando correctamente'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)