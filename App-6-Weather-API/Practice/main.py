from flask import Flask,  render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('practice.html')

@app.route('/api/v1/<word>')
def get_word(word):
    word = word.upper()
    return {
        "word": word
    }
    
if __name__ == '__main__':  
    app.run(debug=True, port = 5001)