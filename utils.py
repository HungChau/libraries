import pandas as pd


def report2dict(cr):
    """
    This function is to transform the free text result from classification_result to indexed format dataframe
    :param cr: the text result from classification_result()
    :return: dataframe format for the result
    """
    # Parse rows
    rows = cr.split("\n")
    df = pd.DataFrame(columns=['metric'] + rows[0].split())
    for r in rows[1:]:
        if r != '':
            print(r.split())
            df.loc[df.shape[0]] = r.split()[-5:]
    return df
