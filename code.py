import re
from collections import defaultdict

DISEASE_SYMPTOMS = {
    "Common Cold": ["runny nose", "sore throat", "sneezing", "headache", "mild fever", "stuffy nose", "stomach ache"],
    "Flu": ["high fever", "body aches", "fatigue", "sore throat", "dry cough", "headache", "chills", "weakness"],
    "Migraine": ["severe headache", "throbbing pain", "light sensitivity", "sound sensitivity", "nausea", "vomiting", "blurred vision"],
    "Allergies": ["sneezing", "itchy eyes", "runny nose", "watery eyes", "sore throat", "nasal congestion", "post-nasal drip"],
    "Stomache infection": ["vomiting", "diarrhea", "nausea", "stomach cramps", "abdominal pain", "mild fever", "stomach ache"],
    "Bacterial Gastroenteritis": ["high fever", "severe abdominal pain", "bloody stool", "persistent vomiting", "dehydration"],
    "Strep Throat": [ "red tonsils", "white patches on throat", "tiny red spots on roof of mouth"],
    "Bronchitis": ["chest discomfort", "persistent cough", "mucus production", "fatigue", "shortness of breath", "low-grade fever"]
}

def predict_disease(user_symptoms):
    user_words = set()
    symptom_list = re.split(r'[,\s/]+', user_symptoms.lower().strip())
    
    stop_words = {"a", "an", "the", "i", "my", "is", "have", "am", "feeling", "a little"}
    
    for word in symptom_list:
        if word and word not in stop_words:
            user_words.add(word)

    if not user_words:
        return "No symptoms entered. Please enter a comma-separated list of symptoms.", 0

    disease_scores = defaultdict(int)

    max_matches = 0
    likely_disease = "Unknown"

    for disease, symptoms in DISEASE_SYMPTOMS.items():
        match_count = 0
        
        for symptom in symptoms:
            if symptom in user_words:
                match_count += 1
            
            for user_word in user_words:
                if user_word in symptom and len(user_word) > 3:
                    match_count += 0.5
        
        disease_scores[disease] = match_count
        
        if match_count > max_matches:
            max_matches = match_count
            likely_disease = disease
        elif match_count == max_matches and max_matches > 0:
            pass

    if max_matches == 0:
        return "Could not find a likely match for the symptoms provided. Please try using simpler, specific terms.", 0
        
    return likely_disease, max_matches

def main():
    print("==========================================")
    print("SIMPLE RULE-BASED DISEASE PREDICTOR (V3)")
    print("==========================================")
    
    # Updated symptom list to include 'bloody stool' and 'dehydration'
    print("\nExpanded key symptoms include: high fever, runny nose, sore throat, sneezing, headache,")
    print("body aches, fatigue, cough, nausea, vomiting, diarrhea, stomach cramps, itchy eyes,")
    print("chills, chest discomfort, painful swallowing, white patches on throat, shortness of breath, STOMACH ACHE, BLOODY STOOL, and DEHYDRATION.")
    
    user_input = input("\nEnter your symptoms (e.g., severe abdominal pain, high fever, bloody stool): ")
    
    predicted_disease, score = predict_disease(user_input)

    print("\n==========================================")
    if score > 0:
        print(f"Based on your input, the most likely condition is: \n\n-> {predicted_disease.upper()} (Match Score: {int(score)})")
        print("\n\n*** DISCLAIMER: This is a simple, rule-based prediction and is NOT a substitute for professional medical advice. Please consult a doctor for a proper diagnosis. ***")
    else:
        print(f"Prediction Result: {predicted_disease}")
    print("==========================================")


if __name__ == "__main__":
    main()