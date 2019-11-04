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


def read_csv(input_file):
    """ Deal with reading big csv files """
    with open(input_file, 'r') as f:
        a = f.readline()
    csv_list = a.split(',')
    tsv_list = a.split('\t')
    if len(csv_list) > len(tsv_list):
        sep = ','
    else:
        sep = '\t'

    reader = pd.read_csv(input_file, iterator=True, low_memory=False, delimiter=sep)
    loop = True
    chunk_size = 100000
    chunks = []
    while loop:
        try:
            chunk = reader.get_chunk(chunk_size)
            chunks.append(chunk)
        except StopIteration:
            loop = False
    df = pd.concat(chunks, ignore_index=True)
    return df


def get_filenames(path, format_files, filtered_with=''):
    filenames = [f for f in listdir(path) if isfile(join(path, f)) and f[-3:]==format_files and f.find(filtered_with)>-1]
    
    return filenames
