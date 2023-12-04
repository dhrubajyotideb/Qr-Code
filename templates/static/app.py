from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr_code():
    user_input = request.form['text']  # Retrieve user input from the form
    userqr = qrcode.make(user_input)
    userqr.save('static/userqr.png')  # Save the QR code in the 'static' folder
    return 'QR code generated and saved!'

if name == '__main__':
    app.run()  # Remove the app.run() line when using uWSGI