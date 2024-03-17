from flask import Flask, request, jsonify
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route('/upload', methods=['POST'])

def upload_image():
    print("upload")
    if 'image' in request.files:
        image_file = request.files['image']
        # Save the image to a desired location
        image_file.save('uploaded_image.png')
        response_data = {'status': 'success', 'message': 'Image uploaded successfully!'}
    else:
        response_data = {'status': 'error', 'message': 'No image found in the request.'}

    return jsonify(response_data)

if __name__ == '__main__':
    #app.run(ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

