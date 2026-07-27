from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resume(job_description, resume_text):
    """
    Calculate similarity score between a job description
    and a resume
    """

    documents = [job_description, resume_text]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])

    score = round(similarity[0][0] * 100, 2)

    return score