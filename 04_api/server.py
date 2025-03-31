from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from fuzzywuzzy import fuzz, process

app = Flask(__name__)
CORS(app)  

# Carregar os dados
df = pd.read_csv('Relatorio_cadop.csv', sep=';', encoding='utf-8').fillna('')

@app.route('/api/search', methods=['GET', 'OPTIONS'])  
def search_operadoras():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    
    query = request.args.get('q', '').lower().strip()
    limit = int(request.args.get('limit', 10))
    
    if not query:
        return _corsify_response(jsonify([]))
    
    try:
        # Logica de busca
        choices = [(i, row['Razao_Social']) for i, row in df.iterrows()]
        results = process.extract(query, choices, scorer=fuzz.token_set_ratio, limit=limit)
        
        matches = []
        for (idx, name), score in results:
            if score > 50:
                record = df.iloc[idx].to_dict()
                record['similarity_score'] = score
                matches.append(record)
        
        return _corsify_response(jsonify(matches))
    
    except Exception as e:
        print("Erro no servidor:", str(e))
        return _corsify_response(jsonify({"error": str(e)}), 500)

def _build_cors_preflight_response():
    response = jsonify({"message": "Preflight OK"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

def _corsify_response(response, status_code=200):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)