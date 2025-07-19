from flask import Flask, request, send_file
from rembg import remove
import io, os

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Background Remover API Working!'

@app.route('/remove', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {'error': 'No image provided'}, 400

    file = request.files['image']
    input_data = file.read()
    output_data = remove(input_data)

    return send_file(io.BytesIO(output_data), mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
