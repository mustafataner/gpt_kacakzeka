

import os
from flask import Flask, render_template, request
from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prompt = ""
    response = ""

    if request.method == 'POST':
        prompt = request.form.get('prompt')

        if prompt:
            llm = OpenAI(temperature=0.92, model_name='gpt-3.5-turbo')
            response = llm(prompt)
        else:
            response = "Lütfen bir soru girin."

    return render_template('index.html', prompt=prompt, response=response)

if __name__ == '__main__':
    app.run(debug=False)
