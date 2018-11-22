from modelmatcher.models import RateMatrix

def read_model(h, model_name):
    '''
    Read a amino acid replacement model in PAML format (used also by PhyML) from file handle h
    and return a RateMatrix.
    '''
    r_vals = []
    freqs = None
    for line in h:
        if line[0] == '#':
            continue
        else:
            input_tokens = line.split()
            vals = list(map(float, input_tokens))
            if len(input_tokens) < 20:
                r_vals.extend(vals)
            else:
                freqs = vals
                break
    else:
        raise IOError('Is the input really a PAML-formatted model?')

    q = RateMatrix(model_name)
    q.set_r_and_freq(r_vals, freqs)
    return q
