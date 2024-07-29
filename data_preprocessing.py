import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load data
ecom_data = pd.read_excel('ecom customer_data.xlsx')
mall_data = pd.read_csv('Mall_Customers.csv')

# Preprocess e-commerce data
def preprocess_ecom_data(df):
    df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
    le = LabelEncoder()
    df['Gender'] = le.fit_transform(df['Gender'])
    return df

# Preprocess mall data
def preprocess_mall_data(df):
    le = LabelEncoder()
    df['Genre'] = le.fit_transform(df['Genre'])
    return df

ecom_data_preprocessed = preprocess_ecom_data(ecom_data)
mall_data_preprocessed = preprocess_mall_data(mall_data)

# Normalize data
def normalize_data(df):
    scaler = StandardScaler()
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df

ecom_data_normalized = normalize_data(ecom_data_preprocessed)
mall_data_normalized = normalize_data(mall_data_preprocessed)

# Save preprocessed data
ecom_data_normalized.to_csv('ecom_data_normalized.csv', index=False)
mall_data_normalized.to_csv('mall_data_normalized.csv', index=False)
