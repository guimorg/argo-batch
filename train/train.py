# This is the script that 'trains' the KMeans
# algorithm. It saves the model in a pickle
# that is later stored in S3 by Argo
import pandas as pd

from sklearn.cluster import KMeans


def main():
    data = pd.read_csv('/mnt/vol/Mall_Customers.csv', usecols=['Spending Score (1-100)', 'Annual Income (k$)'])
    km = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
    # Training the model
    km.fit(x)

    # Saving the model
    from sklearn.externals import joblib
    joblib.dump(km, '/mnt/vol/kmeans.joblib')


if __name__ == "__main__":
    main()
