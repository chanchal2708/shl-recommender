import pandas as pd

def load_and_preprocess_data(file_path):
    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        print("Data loaded successfully.")
    except pd.errors.EmptyDataError:
        print("The CSV file is empty or not formatted correctly.")
        return None
    except FileNotFoundError:
        print("The CSV file was not found. Please check the file path.")
        return None

    # Display the first few rows of the DataFrame
    print("\nFirst few rows of the dataset:")
    print(df.head())

    # Check for missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    # Check data types
    print("\nData types of each column:")
    print(df.dtypes)

    # Check unique values in 'Test Type' column
    print("\nUnique values in 'Test Type' column:")
    print(df['Test Type'].unique())

    # Preprocess the data
    # Fill missing values
    df.fillna({'Remote Testing Support': 'No', 'Adaptive/IRT Support': 'No'}, inplace=True)

    # Convert 'Duration' to numerical format (e.g., minutes)
    df['Duration'] = df['Duration'].apply(lambda x: int(x.split()[0]))

    # Normalize text in 'Assessment Name'
    df['Assessment Name'] = df['Assessment Name'].str.lower()

    # Display the first few rows after preprocessing
    print("\nFirst few rows after preprocessing:")
    print(df.head())

    return df

# Specify the path to your CSV file
file_path = 'shl_assessments.csv'

# Load and preprocess the data
df = load_and_preprocess_data(file_path)

# If you want to save the preprocessed data to a new CSV file
if df is not None:
    df.to_csv('preprocessed_shl_assessments.csv', index=False)
    print("\nPreprocessed data saved to preprocessed_shl_assessments.csv")