from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management
CORS(app) 

NEWS_API_KEY = '57ab365b466b4115ad926b7e8a63bdfb'  # Replace 'your_news_api_key' with your actual News API key

@app.route('/news', methods=['GET'])
def get_news():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()['articles']
        return jsonify(news_data)
    else:
        return jsonify({'error': 'Failed to fetch news'}), 500

if __name__ == '__main__':
    app.run(debug=True)
