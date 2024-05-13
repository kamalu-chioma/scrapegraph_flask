from flask import Flask, render_template, request, jsonify
import os
import nest_asyncio
from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv

load_dotenv() 
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  

nest_asyncio.apply()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        data_spec = request.form['data_spec']

        graph_config = {
            "llm": {
                "api_key": OPENAI_API_KEY,
                "model": "gpt-3.5-turbo",
                "temperature": 0,
            },
        }

        smart_scraper_graph = SmartScraperGraph(
            prompt=data_spec,
            source=url,
            config=graph_config
        )

        result = smart_scraper_graph.run()

        return jsonify(result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
