# Dark Pattern Classifier

## Description
This module aims to analyze already identified dark patterns and classify them into 4 sub-types. The module leverages the BERT (Bidirectional Encoder Representations from Transformers) classification model to examine text and perform classification of Dark Patterns into 4 following sub-types:
1. Misdirection
2. Scarcity
3. Social Proof
4. Urgency

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Installation
1. Clone the repository
2. Create a virtual environment with Python version 3.9
3. Activate the virtual environment
4. Run `poetry install` to install dependencies


## Usage
The API for this module is located in `predictor.py`. It can be used simply by importing the file.
```
import dark_pattern_classifier.predictor as predictor
```

- To make predictions, run `predictor.make_prediction()`
    ```
    input_text = "Sample text"
    dark_pattern_present = predictor.make_prediction(input_text)
    ```

- To check the presence of dark patterns on a sequence of elements, run `predictor.make_predictions()`
    ```
    input_list = ["Sample text 1", "Sample text 2"]
    prediction_list = predictor.are_dark_patterns(input_list)
    ```

## License
This project is licensed under the [MIT License](LICENSE).