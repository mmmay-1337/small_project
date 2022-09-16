# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

example_ds_df = pd.DataFrame(data = pd.date_range(start = '2022-01-25', end = '2022-05-01'))


# Write recipe outputs
example_dataset = dataiku.Dataset("example_dataset")
example_dataset.write_with_schema(example_ds_df)

# changes here

# another change

# here is another line, take mine instead
