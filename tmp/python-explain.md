# Python 3 
import pandas

def remove_common_prefix(data: pandas.DataFrame, col: str, prefix: str, ws_prefix: str) -> pandas.DataFrame: 
    data[col] = data[col].str[len(prefix) :] 
    if ws_prefix: 
        # keep the single whitespace as prefix 
        data[col] = " " + data[col] 
    return data

# Explanation of what the code does