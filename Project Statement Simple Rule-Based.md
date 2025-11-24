Project Statement: Simple Rule-Based Disease Predictor

1. Problem Statement

The core problem addressed by this project is the need for a simple, accessible demonstration of deterministic classification logic using basic programming structures. Specifically, how can a program effectively interpret unstructured, free-form text input (a list of symptoms) and accurately classify it into one of several predefined categories (common diseases) based purely on a set of explicit rules and pattern matching? This requires robust input handling and a scoring mechanism to differentiate between closely related outcomes.

1. Scope of the Project

The scope of the Simple Rule-Based Disease Predictor is strictly limited to a proof-of-concept, command-line application built entirely in Python.

In Scope:

Implementing a static knowledge base of common diseases and their symptoms (e.g., Flu, Cold, Strep, Gastroenteritis).

Developing a core prediction engine using a scoring algorithm for symptom matching.

Building robust input preprocessing using regular expressions (re).

Providing clear console output and necessary medical disclaimers.

Out of Scope:

Integration with external databases or APIs.

Use of Machine Learning (ML) or probabilistic models.

A graphical user interface (GUI) or web interface.

Clinical validation or use as a replacement for professional medical diagnosis.

1. Target Users

The primary target users for this project are academic:

Students and Educators: Individuals studying fundamental programming concepts, data structures (dictionaries and sets), and classification algorithms.

Beginner Developers: Those seeking a straightforward, real-world example of how to implement a basic expert system using only built-in Python modules.

1. High-Level Features

Rule-Based Classification: Predicts a likely condition from a predefined list.

Intelligent Input Processing: Cleans and tokenizes user symptom input to ensure accurate matching.

Symptom Scoring: Calculates a quantitative "Match Score" to show the correlation confidence for the predicted disease.

Differentiated Conditions: Includes fine-grained symptom sets to distinguish between similar illnesses (e.g., Viral vs. Bacterial infection).
