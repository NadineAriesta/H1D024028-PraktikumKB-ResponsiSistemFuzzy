import sys
import os

# Tambahkan folder saat ini ke path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
application = app

# Test route untuk memastikan Flask jalan
@app.route('/test-flask')
def test_flask():
    return "Flask is alive!"

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Template Error: {str(e)}"

@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    try:
        from fuzzy_logic import evaluate_offer
        data = request.get_json()
        
        gaji = float(data.get('gaji', 0))
        relevansi = float(data.get('relevansi', 0))
        fleksibilitas = float(data.get('fleksibilitas', 0))
        reputasi = float(data.get('reputasi', 0))
        
        result = evaluate_offer(gaji, relevansi, fleksibilitas, reputasi)
        
        return jsonify({
            "success": True,
            "data": result
        })
    except Exception as e:
        import traceback
        return jsonify({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
