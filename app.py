from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configure your OpenAI API key
openai.api_key = 'sk-...2SdO'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_code', methods=['POST'])
def get_code():
    try:
        data = request.get_json()
        user_input = data['input']
        
        # Use OpenAI's GPT-3 to generate code
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=100
        )
        generated_code = response.choices[0].text.strip()

        return jsonify({'code': generated_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
