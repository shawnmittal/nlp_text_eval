from flask import Flask, redirect, request, url_for, jsonify

# NLP packages
from .parse_and_eval import *

app = Flask(__name__)


@app.route('/url_eval', methods=['POST'])
def eval_url():
    url = request.get_json()
    article = get_and_parse(url)
    sentiment = vader(article)
    return jsonify(
        title=article.title,
        summary=article.summary,
        keywords=article.keywords,
        score=sentiment)


if __name__ == '__main__':
    app.run()
