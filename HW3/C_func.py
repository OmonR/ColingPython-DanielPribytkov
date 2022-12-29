import tqdm
from corus import load_corpora


path = 'annot.opcorpora.xml.byfile.zip'
records = load_corpora(path)

def data_creation():
    with open('pos_data.txt', 'w', encoding='utf-8') as f:
        for rec in tqdm.tqdm(records):
            for par in rec.pars:
                for sent in par.sents:
                    for token in sent.tokens:
                        f.write(f'{token.text} {token.forms[0].grams[0]}\n')
    return