from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        print(city)

        if city:
            api_key = 'd9a370b6d08a1b9f99297f63d28fec27'
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            print(response.status_code)
            if response.status_code == 200:
                data = response.json()
                print(data)
                return render_template('index.html', data=data)
            else:
                return render_template('index.html', error='City not found')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
