import pandas as pd
from sklearn.datasets import make_classification

def remove_collinear_cols(x_data):
    return x_data.drop(['D', 'I'], axis=1)

class CreateClassificationData():
    def __init__(self):
        x_arr, y_arr = make_classification(
            n_samples=5000,
            n_features=10,
            n_classes=2,
            random_state=1
        )
        col_names = ['A', 'B', 'C', 'D', 'E',
                     'F', 'G', 'H', 'I', 'J']
        x_df = pd.DataFrame(x_arr, columns=col_names)
        y_df = pd.DataFrame({'Target': y_arr})
        # Training set n=3500
        self.x_train = x_df.iloc[:3500]
        self.y_train = y_df.iloc[:3500]

        # Testing set n=1500
        self.x_test = x_df.iloc[3500:]
        self.y_test = y_df.iloc[3500:]

    def prepare_data(self):
        self.x_train = remove_collinear_cols(self.x_train)
        self.x_test = remove_collinear_cols(self.x_test)

    def upload_data(self):
        dfs = [self.x_train, self.y_train, self.x_test, self.y_test]
        df_name = ['x_train', 'y_train', 'x_test', 'y_test']
        i = 0
        for df in dfs:
            file_name = df_name[i]
            df.to_csv(f'data/{file_name}.csv', index=0)
            i+=1


def main():
    
    # Create and Upload data to Blob Store
    data_creator = CreateClassificationData()
    data_creator.prepare_data()
    data_creator.upload_data()

if __name__ == '__main__':
    main()
