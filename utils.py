import json
from pprint import pprint as pp

def load_candidates_from_json():
    """возвращает список всех кандидатов"""
    with open("candidates.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data

def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate.get("id") == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidate_names = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_name in candidate.get("name").lower():
            candidate_names.append(candidate)
    return candidate_names


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidate_skills = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        str_skills = candidate.get("skills").lower().split(", ")
        if skill_name.lower() in str_skills:
            candidate_skills.append(candidate)
    return candidate_skills


#pp(get_candidates_by_skill("Delphi"))
