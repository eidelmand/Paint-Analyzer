from flask import Flask, requests
app = Flask(__name__)

url = ''


@app.route('/send_picture', methods=['POST'])
def receive_picture():
    picture = requests.form['picture']
    results = analyze_picture(picture)
    requests.post(url,data={'results': results})


if __name__ == '__main__':
    app.run(debug=True, port=5000)