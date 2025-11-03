from django import forms

# --- Reusable CSS classes for form fields ---
TAILWIND_CLASSES = "w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
TAILWIND_INPUT = forms.NumberInput(attrs={'class': TAILWIND_CLASSES})
TAILWIND_SELECT = forms.Select(attrs={'class': TAILWIND_CLASSES})

# --- Your Choice Lists (unchanged) ---
YES_NO = [("yes", "Yes"), ("no", "No")]
BOOK_TYPES = [
    ("Series", "Series"), ("Autobiographies", "Autobiographies"),
    ("Travel", "Travel"), ("Self-help", "Self-help"),
    ("Educational", "Educational"),
]
COMPANY_TYPES = [
    ("BPA", "BPA"), ("Cloud Services", "Cloud Services"),
    ("product development", "Product Development"),
    ("service based", "Service Based"),
]
WORKSHOP_TYPES = [
    ("testing", "Testing"), ("cloud computing", "Cloud Computing"),
    ("web development", "Web Development"), ("data analytics", "Data Analytics"),
]
CERTIFICATIONS = [
    ("information security", "Information Security"),
    ("shell programming", "Shell Programming"),
    ("machine learning", "Machine Learning"), ("fullstack", "Full Stack Development"),
]
SUBJECTS = [
    ("programming", "Programming"), ("Management", "Management"),
    ("data engineering", "Data Engineering"), ("networks", "Networks"),
]
CAREER_AREAS = [
    ("testing", "Testing"), ("system developer", "System Developer"),
    ("Business process analyst", "Business Process Analyst"),
    ("data science", "Data Science"),
]
MANAGEMENT_OR_TECH = [("Management", "Management"), ("Technical", "Technical")]
HARD_SMART = [("hard worker", "Hard Worker"), ("smart worker", "Smart Worker")]
READING_SKILLS = [("poor", "Poor"), ("medium", "Medium"), ("excellent", "Excellent")]
MEMORY_SCORE = [("poor", "Poor"), ("medium", "Medium"), ("excellent", "Excellent")]


class CareerForm(forms.Form):
    # --- Integer Fields (using NumberInput widget) ---
    Logical_quotient_rating = forms.IntegerField(min_value=0, max_value=10, widget=TAILWIND_INPUT)
    hackathons = forms.IntegerField(min_value=0, max_value=50, widget=TAILWIND_INPUT)
    coding_skills_rating = forms.IntegerField(min_value=0, max_value=10, widget=TAILWIND_INPUT)
    public_speaking_points = forms.IntegerField(min_value=0, max_value=10, widget=TAILWIND_INPUT)

    # --- Choice Fields (using Select widget) ---
    self_learning_capability = forms.ChoiceField(choices=YES_NO, widget=TAILWIND_SELECT)
    Extra_courses_did = forms.ChoiceField(choices=YES_NO, widget=TAILWIND_SELECT)
    certifications = forms.ChoiceField(choices=CERTIFICATIONS, widget=TAILWIND_SELECT)
    workshops = forms.ChoiceField(choices=WORKSHOP_TYPES, widget=TAILWIND_SELECT)
    reading_and_writing_skills = forms.ChoiceField(choices=READING_SKILLS, widget=TAILWIND_SELECT)
    memory_capability_score = forms.ChoiceField(choices=MEMORY_SCORE, widget=TAILWIND_SELECT)
    Interested_subjects = forms.ChoiceField(choices=SUBJECTS, widget=TAILWIND_SELECT)
    interested_career_area = forms.ChoiceField(choices=CAREER_AREAS, widget=TAILWIND_SELECT)
    Type_company_settle = forms.ChoiceField(choices=COMPANY_TYPES, widget=TAILWIND_SELECT)
    Taken_inputs_from_seniors = forms.ChoiceField(choices=YES_NO, widget=TAILWIND_SELECT)
    Interested_type_of_books = forms.ChoiceField(choices=BOOK_TYPES, widget=TAILWIND_SELECT)
    Management_or_Technical = forms.ChoiceField(choices=MANAGEMENT_OR_TECH, widget=TAILWIND_SELECT)
    hard_smart_worker = forms.ChoiceField(choices=HARD_SMART, widget=TAILWIND_SELECT)
    worked_in_teams = forms.ChoiceField(choices=YES_NO, widget=TAILWIND_SELECT)
    Introvert = forms.ChoiceField(choices=YES_NO, widget=TAILWIND_SELECT)