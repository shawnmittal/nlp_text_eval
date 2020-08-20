# Simple Flask NLP API
A simple flask api that takes a news url and returns a summary along with NLTK Vader sentiment. Using newspaper3k library for url parsing.

## Requirements
- beautifulsoup4==4.9.1
- newspaper3k==0.2.8
- nltk==3.5
- flask==1.1.2

## Build
```
docker build -t nlpapi:latest .
```

## Run
```
docker run -p 5000:5000 nlpapi:latest
```

## Test
```
python3 /tests/test_request.py
```