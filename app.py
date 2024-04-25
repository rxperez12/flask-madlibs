from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def generate_template():
    """Generates a template of story prompts for user to fill in"""
    words = silly_story.prompts

    return render_template('questions.jinja', word_prompt=words)


@app.get('/results')
def get_answers():
    """Gets answers provided by users in story prompt and updates results.jinja"""
    ans = request.args  # this is not exactly a dictionary but can be treated like a dictionary
    results = silly_story.get_result_text(ans)

    return render_template('results.jinja', story=results)
