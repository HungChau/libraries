import pandas as pd

def report2dict(cr):
    # Parse rows
    rows = cr.split("\n")
    df = pd.DataFrame(columns=['metric']+rows[0].split())
    for r in rows[1:]:
        if r != '':
            print(r.split())
            df.loc[df.shape[0]] = r.split()[-5:]
    return df