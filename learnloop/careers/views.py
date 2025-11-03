from django.shortcuts import render

# Create your views here.
def careers_view(request):
    return render(request, 'roadmap.html')


import joblib
import numpy as np
from django.shortcuts import render
from .forms import CareerForm
from django.conf import settings
import os

# --- Load models and encoders ---
model_path = os.path.join(settings.BASE_DIR, 'careers', 'ml', 'career_model.pkl')
encoders_path = os.path.join(settings.BASE_DIR, 'careers', 'ml', 'encoders.pkl')

model = joblib.load(model_path)
encoders = joblib.load(encoders_path) 
# -------------------------------------------------

# 1. THE FIX: 
# This map connects your 'forms.py' field names (keys)
# to the exact model column names from your 'dict_keys' (values).
FEATURE_MAP = {
    # Form Field Name : "Model Column Name"
    
    # --- Numerical Fields ---
    # (We assume their column names match the form field names)
    'Logical_quotient_rating': 'Logical_quotient_rating', 
    'hackathons': 'hackathons',
    'coding_skills_rating': 'coding_skills_rating',
    'public_speaking_points': 'public_speaking_points',
    
    # --- Categorical Fields (from your dict_keys output) ---
    'self_learning_capability': 'self-learning capability?',
    'Extra_courses_did': 'Extra-courses did',
    'certifications': 'certifications',
    'workshops': 'workshops',
    'reading_and_writing_skills': 'reading and writing skills',
    'memory_capability_score': 'memory capability score',
    'Interested_subjects': 'Interested subjects',
    'interested_career_area': 'interested career area ', # <-- Note the trailing space!
    'Type_company_settle': 'Type of company want to settle in?',
    'Taken_inputs_from_seniors': 'Taken inputs from seniors or elders',
    'Interested_type_of_books': 'Interested Type of Books',
    'Management_or_Technical': 'Management or Technical',
    'hard_smart_worker': 'hard/smart worker',
    'worked_in_teams': 'worked in teams ever?',
    'Introvert': 'Introvert'
}


def career_predict(request):
    if request.method == "POST":
        form = CareerForm(request.POST)
        if form.is_valid():
            try:
                user_data = []
                cleaned_data = form.cleaned_data
                
                # 2. Loop over the MAPPING
                for form_field, model_column in FEATURE_MAP.items():
                    
                    # Get value from the form using the form's name
                    value = cleaned_data.get(form_field) 
                    
                    # 3. Check if the MODEL's column name is in the encoder
                    if model_column in encoders:
                        # Transform the value (e.g., 'yes' -> 1)
                        value = encoders[model_column].transform([value])[0]
                    
                    # 4. Handle Nones or empty strings (for numerical fields)
                    if value is None or value == '':
                        value = 0.0 
                    
                    # 5. Append the (now numerical) value
                    user_data.append(float(value))

                # 6. Predict
                prediction = model.predict([user_data])[0]

                # 7. Inverse transform the result
                predicted_job = encoders["Suggested Job Role"].inverse_transform([prediction])[0]

                return render(request, "careers/result.html", {"career": predicted_job})

            except Exception as e:
                # This will catch any new errors, like a model/encoder key mismatch
                form.add_error(None, f"An error occurred during prediction: {e}")
    else:
        form = CareerForm()

    return render(request, "careers/careerform.html", {"form": form})