from src.loaddata import load_and_preprocess_data
from src.recommend import create_features, recommend_assessments

def main():
    file_path = 'data/shl_assessments.csv'
    df = load_and_preprocess_data(file_path)
    if df is not None:
        tfidf_matrix = create_features(df)
        query = "cognitive test for leadership skills"
        recommended_assessments = recommend_assessments(query, df, tfidf_matrix)
        print("\nRecommended Assessments:")
        print(recommended_assessments[['Assessment Name', 'URL', 'Duration', 'Test Type']])

if __name__ == "__main__":
    main()