from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query == 'irving':
        return render_template('index.html')
    elif query == 'bryant':
        return render_template('bryant_info.html')
    
    return "검색 결과가 없습니다."

if __name__ == '__main__':
    app.run(debug=True)
