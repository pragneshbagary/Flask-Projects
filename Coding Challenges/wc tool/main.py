# from flask import Flask, request

# app = Flask('__name__')


def line_count(text):
    return text.count('\n')

def word_count(text):
    return len(text.split())

def count_bytes(text):
    return len(text.encode('utf-8'))

def char_count(text):
    return len(text)    


# @app.route('/', methods = ['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         file

with open("test.txt" , "r") as file:
    text = file.read()
    print(line_count(text))
    print(word_count(text))
    print(count_bytes(text))
    print(char_count(text))



