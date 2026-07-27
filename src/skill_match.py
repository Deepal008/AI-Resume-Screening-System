import re

def extract_skills(text):
    """
    Extract skills from text.
    """

    words = re.findall(r"/b[a-zA-Z]+\b", text.lower())

    return set(words)

def match_skills(job_description, resume_text):

    """
    Compare resume skill with job description.
    """

    jd_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume_text)

    matched = jd_skills.intersection(resume_skills)
    missing = jd_skills.difference(resume_skills)

    if len(jd_skills) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_skills))* 100, 2)

    return {
        "matched_skills": sorted(list(matched)),
        "missing_skills": sorted(list(missing)),
        "matching_score": score
    }