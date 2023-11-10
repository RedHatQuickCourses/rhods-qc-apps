import pandas as pd


def create_sample_sql_table(table_name, connection):
    df = pd.DataFrame(
        columns=['uid', 'name', 'active'],
        data=[
            [0, 'Alex', True], 
            [1, 'Guy', False],
            [2, 'Ravi', True],
            [3, 'Rafa', False],
        ]
    )

    df.to_sql(name=table_name, con=connection)
