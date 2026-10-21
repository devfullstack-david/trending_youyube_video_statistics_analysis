import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import pickle

def processing_csv(csv):
  csv['description'] = csv['description'].fillna('')
  csv['publish_time'] = pd.to_datetime(csv['publish_time'])
  csv['trending_date'] = pd.to_datetime(csv['trending_date'], format='%y.%d.%m')
  csv['publish_time_naive'] = csv['publish_time'].dt.tz_localize(None)
  csv['days_to_trend'] = (csv['trending_date'] - csv['publish_time_naive']).dt.days
  csv['engagement_rate'] = (csv['likes'] + csv['comment_count']) / csv['views']
  csv['title_length'] = csv['title'].apply(len)
  csv['tags_count'] = csv['tags'].apply(lambda x: len(x.split('|')) if x != '[none]' else 0)

def encode_csv(csv):
  encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
  encoder.set_output(transform="pandas")

  codified_categories = encoder.fit_transform(csv[['category_id']])

  csv_encoded = pd.concat([csv.drop(columns=['category_id']), codified_categories], axis=1)
  csv_encoded = csv_encoded.drop(columns=['category_id'])

  scaler = StandardScaler()
  numeric_columns = ['views', 'likes', 'dislikes']
  csv_encoded[numeric_columns] = scaler.fit_transform(csv_encoded[numeric_columns])

  return csv_encoded

def save_train_test_split(csv):
  independent_columns = csv.drop(columns=['likes'])
  dependent_column = csv['likes']

  X_train, X_test, y_train, y_test = train_test_split(independent_columns, dependent_column, test_size=0.2, random_state=0)

  with open('train_test_split.pkl', 'wb') as f:
    pickle.dump((X_train, X_test, y_train, y_test), f)