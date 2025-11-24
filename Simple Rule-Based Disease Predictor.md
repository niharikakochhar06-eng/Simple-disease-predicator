Simple Rule-Based Disease Predictor

1. Project Overview

The Simple Rule-Based Disease Predictor is a command-line application designed as a demonstration of a minimalist expert system. Its core function is to analyze user-inputted symptoms and apply a fixed set of clinical rules to determine the most statistically likely health condition from its knowledge base.

It utilizes deterministic classification logic based on symptom-matching scores.

1. Features

Rule-Based Logic: Utilizes a predefined internal dictionary (DISEASE\_SYMPTOMS) to map symptoms to conditions.

Scoring Algorithm: Implements a fuzzy matching score to identify the disease with the highest correlation to the user's reported symptoms.

Detailed Knowledge Base: Includes symptom differentiation for closely related conditions like Viral Gastroenteritis, Bacterial Gastroenteritis, Flu, Strep Throat, and Bronchitis.

Robust Input Handling: Uses the re module to tokenize user input, allowing for comma, space, or slash separation of symptoms, and automatically filters out common stop words.

Clear Output: Provides a prediction and a matching score directly in the console.

1. Technologies/Tools Used

Language: Python 3.x

Core Modules: re (Regular Expressions), collections (defaultdict)

Version Control: Git

1. Steps to Install & Run the Project

This project requires only the standard Python installation and no external libraries.

1. Installation

Clone the GitHub repository to your local machine:

git clone [YOUR\_REPOSITORY\_URL]

cd simple-disease-predictor


Ensure the main file is present in the directory: disease\_predictor.py.

1. Execution

Run the application from your terminal:

python disease\_predictor.py


The program will prompt you to enter your symptoms as a comma-separated list.

1. Example Usage

Input:

Enter your symptoms (e.g., severe abdominal pain, high fever, bloody stool): high fever, body aches, chills


Output:

\==========================================

Based on your input, the most likely condition is:

-> FLU (Match Score: 3)

\*\*\* DISCLAIMER: This is a simple, rule-based prediction and is NOT a substitute for professional medical advice. Please consult a doctor for a proper diagnosis. \*\*\*

\==========================================


1. Instructions for Testing

The primary method for functional testing is by using sample inputs designed to trigger specific predictions:

Test Scenario

Input Symptoms

Expected Prediction

Test Case 1 (Flu)

high fever, body aches, chills, dry cough

Output-Flu

Test Case 2 (Strep Throat)

painful swallowing, red tonsils, white patches on throat

Output-Strep Throat

Test Case 3 (Bacterial GI)

severe abdominal pain, bloody stool, dehydration

Output-Bacterial Gastroenteritis

Test Case 4 (Common Cold)

runny nose, sneezing, stomach ache

Output-Common Cold
