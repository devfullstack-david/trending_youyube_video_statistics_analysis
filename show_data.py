import matplotlib.pyplot as plt
import seaborn as sns

def correlation_matrix_of_engagement_metrics(csv):
  plt.figure(figsize=(10, 8))
  metrics = ['views', 'likes', 'dislikes', 'comment_count']
  sns.heatmap(csv[metrics].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
  plt.title('Correlation Matrix of Engagement Metrics')
  plt.show()

def trending_videos_by_category(csv):
  plt.figure(figsize=(12, 6))
  sns.countplot(data=csv, y='category_id', order=csv['category_id'].value_counts().index)
  plt.title('Trending Videos by Category')
  plt.xlabel('Number of Videos')
  plt.ylabel('Category ID')
  plt.show()