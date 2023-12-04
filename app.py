from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr_code():
    user_input = request.form['text']  # Retrieve user input from the form
    generate_qr(user_input)
    return 'QR code generated and saved!'

def generate_qr(text):
    userqr = qrcode.make(text)
    userqr.save('static/userqr.png')  # Save the QR code in the 'static' folder

@app.route('/generate_qr_direct', methods=['GET'])
def generate_qr_direct():
    user_input = request.args.get('user_input')
    generate_qr(user_input)
    return f'QR code for {user_input} generated and saved!'

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)