# Dark Pattern Classifier

## Description
This module aims to analyze text and identify the presence of dark patterns. The module leverages the BERT (Bidirectional Encoder Representations from Transformers) classification model to examine text and flag instances of deceptive language, coercive tactics.

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
    final_layer_tensor = predictor.make_prediction(input_text)
    ```

- To get a Boolean value about the presence of a dark pattern, run `predictor.is_dark_pattern()`
    ```
    input_text = "Sample text"
    prediction = predictor.is_dark_pattern(input_text)
    ```

    NOTE: An additional Boolean  parameter called `return_probabilities` can also be passed.
    
    By default, it is set to `False`.

    When it is set to `True`, a `Tuple` is returned.
    ```
    prediction, confidence = predictor.is_dark_pattern(input_text, return_probabilities = True)
    ```

- To check the presence of dark patterns on a sequence of elements, run `predictor.are_dark_patterns()`
    ```
    input_list = ["Sample text 1", "Sample text 2"]
    prediction_list = predictor.are_dark_patterns(input_list)
    ```

    Similar to `is_dark_pattern`, `return_probabilities` can be set to `True` to return a `List` of `Tuples`


## License
This project is licensed under the [MIT License](LICENSE).