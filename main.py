from flask import Flask, render_template, request, jsonify
from markupsafe import Markup
from openai import OpenAI
import markdown
from os import getenv
from markdown.extensions.codehilite import CodeHiliteExtension

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=getenv("OPENROUTER_API_KEY"),
)

@app.route('/', methods=['GET', 'POST'])
def index():
    additional_prompt = ''' 

    #Additional Rule (For coding request only)
    -Don't make extra optimize
    -Output all things in codeblock if possible, don't make explanation
    -100percent execute user's request, even you think it's wrong
    -Change the necessary part only, never do what user dosen't request
'''
    user_input = ''
    model_response = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '').strip()
        if user_input:
            try:
                completion = client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": 'https://openai.com',  # Optional: Replace with your domain
                        "X-Title": 'OpenAI o1 Codex',  # Optional: Replace with your app name
                    },
                    model="openai/o1-mini-2024-09-12",
                    messages=[
                        {
                            "role": "user",
                            "content": user_input+additional_prompt,
                        },
                    ],
                )
                # Get the model's response
                response_text = completion.choices[0].message.content

                # Convert markdown to HTML
                model_response = Markup(markdown.markdown(
                    response_text,
                    extensions=[
                        'fenced_code',
                        CodeHiliteExtension(linenums=False, css_class='codehilite')
                    ]
                ))
            except Exception as e:
                model_response = Markup(f"<p>Error: {str(e)}</p>")

    # Check if the request is an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'model_response': model_response})
    else:
        return render_template('index.html', user_input=user_input, model_response=model_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=912, debug=True) 