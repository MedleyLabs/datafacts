import os
import pandas as pd

from datafacts import generate_img


def main():

    df = pd.DataFrame.from_dict({
        'Ethnic composition': ['Non-Hispanic White'] * 60 +
                              ['Hispanic and Latino'] * 18 +
                              ['Black or African American'] * 13 +
                              ['Asian'] * 6 +
                              ['Other'] * 3,
        'Gender composition': ['Male'] * 52 + ['Female'] * 45 + ['Non-Binary'] * 3,
        'Manufacturer and model': ['GE Optima 540'] * 72 + ['Siemens Scope 16'] * 28,
    })

    cols = ['Ethnic composition', 'Gender composition', 'Manufacturer and model']

    text = "Clinical decision support software based on machine learning to " \
           "augment diagnosis of abdominal CT scans."

    sections = {
        'Type of algorithm': 'Convolutional neural network',
        'Algorithm AUC': {'Training data': '0.94', 'Validation data': '0.91'}
    }

    if not os.path.exists('img/'):
        os.mkdir('img')

    generate_img(df, 'img/datafacts.png', cols=cols, sections=sections, summary_description=text)


if __name__ == '__main__':

    main()
