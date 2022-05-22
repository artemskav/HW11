from utils import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def candidates_page():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:pk>')
def candidate_id(pk):
    candidate = get_candidate(pk)
    if candidate is None:
        return "Такого нет"
    return render_template('card.html', candidate=candidate)

@app.route('/skills/<skills>')
def candidate_skills(skills):
    candidates_with_skills = get_candidates_by_skill(skills)
    if candidates_with_skills is None:
        return "Укажите навык"
    n_candidates = len(candidates_with_skills)
    return render_template('skill.html', skills=skills,
                           n_candidates=n_candidates,
                           candidates=candidates_with_skills)

@app.route('/search/<name>')
def search_page(name):
    candidats = get_candidates_by_name(name.lower())
    n_search = len(candidats)
    return render_template('search.html', candidats=candidats,
                            n_search=n_search)

if __name__ == "__main__":
	app.run()
