from etl import transform
import pandas as pd

def test_revenue_positive():
    df = pd.DataFrame({"qty": [1, 2], "price": [10, 20]})
    result = transform(df)
    assert (result["revenue"] >= 0).all()
