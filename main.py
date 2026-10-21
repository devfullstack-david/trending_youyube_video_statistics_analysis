import pandas as pd
import processing_data as ppd
import show_data as shd

from sklearn.preprocessing import StandardScaler

data = pd.read_csv("USvideos.csv")

ppd.processing_csv(data)

shd.correlation_matrix_of_engagement_metrics(data)
shd.trending_videos_by_category(data)

data = ppd.encode_csv(data)

ppd.save_train_test_split(data)