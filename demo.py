import pandas as pd

from datafacts import generate_img


if __name__ == '__main__':

    df = pd.DataFrame.from_dict({
        'Ethnic composition': ['Non-Hispanic White'] * 60 +
                              ['Hispanic and Latino'] * 18 +
                              ['Black or African American'] * 13 +
                              ['Asian'] * 6 +
                              ['Other'] * 3,
        'Gender composition': ['Male'] * 55 + ['Female'] * 45,
        'Manufacturer and model': ['GE Optima 540'] * 72 + ['Siemens Scope 16'] * 28,
    })

    cols = ['Ethnic composition', 'Gender composition', 'Manufacturer and model']

    text = "Clinical decision support software based on machine learning to " \
           "augment diagnosis of abdominal CT scans."

    sections = {
        'Type of algorithm': 'Convolutional neural network',
        'Algorithm AUC': {'Training data': '0.94', 'Validation data': '0.91'}
    }

    generate_img(df, 'img.png', cols=cols, sections=sections, summary_description=text)
