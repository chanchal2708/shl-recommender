from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_features(df):
    df['combined_features'] = df['Assessment Name'] + ' ' + df['Test Type']
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined_features'])
    return tfidf_matrix

def recommend_assessments(query, df, tfidf_matrix, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    query_vector = vectorizer.fit(df['combined_features']).transform([query])
    query_similarity = cosine_similarity(query_vector, tfidf_matrix).flatten()
    similar_indices = query_similarity.argsort()[-top_n:][::-1]
    return df.iloc[similar_indices]