"""
ICD-10 Diagnosis Codes Seed Data
Collection of 100 common ICD-10 codes from various categories
Source: https://www.icd10data.com/ICD10CM/Codes
"""

ICD10_CODES = [
    # Infectious and parasitic diseases (A00-B99)
    {"code": "A09", "description": "Infectious gastroenteritis and colitis, unspecified"},
    {"code": "A41.9", "description": "Sepsis, unspecified organism"},
    {"code": "B34.9", "description": "Viral infection, unspecified"},
    {"code": "A49.9", "description": "Bacterial infection, unspecified"},
    {"code": "J06.9", "description": "Acute upper respiratory infection, unspecified"},
    
    # Neoplasms (C00-D49)
    {"code": "C50.919", "description": "Malignant neoplasm of unspecified site of unspecified female breast"},
    {"code": "C61", "description": "Malignant neoplasm of prostate"},
    {"code": "C18.9", "description": "Malignant neoplasm of colon, unspecified"},
    {"code": "D50.9", "description": "Iron deficiency anemia, unspecified"},
    
    # Endocrine, nutritional and metabolic diseases (E00-E89)
    {"code": "E11.9", "description": "Type 2 diabetes mellitus without complications"},
    {"code": "E11.65", "description": "Type 2 diabetes mellitus with hyperglycemia"},
    {"code": "E78.5", "description": "Hyperlipidemia, unspecified"},
    {"code": "E66.9", "description": "Obesity, unspecified"},
    {"code": "E03.9", "description": "Hypothyroidism, unspecified"},
    {"code": "E05.90", "description": "Thyrotoxicosis, unspecified without thyrotoxic crisis or storm"},
    {"code": "E55.9", "description": "Vitamin D deficiency, unspecified"},
    {"code": "E87.6", "description": "Hypokalemia"},
    
    # Mental, behavioral and neurodevelopmental disorders (F01-F99)
    {"code": "F32.9", "description": "Major depressive disorder, single episode, unspecified"},
    {"code": "F41.9", "description": "Anxiety disorder, unspecified"},
    {"code": "F43.10", "description": "Post-traumatic stress disorder, unspecified"},
    {"code": "F10.20", "description": "Alcohol dependence, uncomplicated"},
    {"code": "F90.9", "description": "Attention-deficit hyperactivity disorder, unspecified type"},
    
    # Diseases of the nervous system (G00-G99)
    {"code": "G43.909", "description": "Migraine, unspecified, not intractable, without status migrainosus"},
    {"code": "G44.1", "description": "Vascular headache, not elsewhere classified"},
    {"code": "G47.00", "description": "Insomnia, unspecified"},
    {"code": "G89.29", "description": "Other chronic pain"},
    {"code": "G62.9", "description": "Polyneuropathy, unspecified"},
    
    # Diseases of the eye and adnexa (H00-H59)
    {"code": "H10.9", "description": "Conjunctivitis, unspecified"},
    {"code": "H52.4", "description": "Presbyopia"},
    {"code": "H53.9", "description": "Visual disturbance, unspecified"},
    
    # Diseases of the ear and mastoid process (H60-H95)
    {"code": "H66.90", "description": "Otitis media, unspecified, unspecified ear"},
    {"code": "H81.10", "description": "Benign paroxysmal vertigo, unspecified ear"},
    {"code": "H91.90", "description": "Unspecified hearing loss, unspecified ear"},
    
    # Diseases of the circulatory system (I00-I99)
    {"code": "I10", "description": "Essential (primary) hypertension"},
    {"code": "I25.10", "description": "Atherosclerotic heart disease of native coronary artery without angina pectoris"},
    {"code": "I48.91", "description": "Unspecified atrial fibrillation"},
    {"code": "I50.9", "description": "Heart failure, unspecified"},
    {"code": "I63.9", "description": "Cerebral infarction, unspecified"},
    {"code": "I73.9", "description": "Peripheral vascular disease, unspecified"},
    
    # Diseases of the respiratory system (J00-J99)
    {"code": "J00", "description": "Acute nasopharyngitis [common cold]"},
    {"code": "J01.90", "description": "Acute sinusitis, unspecified"},
    {"code": "J02.9", "description": "Acute pharyngitis, unspecified"},
    {"code": "J03.90", "description": "Acute tonsillitis, unspecified"},
    {"code": "J18.9", "description": "Pneumonia, unspecified organism"},
    {"code": "J20.9", "description": "Acute bronchitis, unspecified"},
    {"code": "J40", "description": "Bronchitis, not specified as acute or chronic"},
    {"code": "J44.9", "description": "Chronic obstructive pulmonary disease, unspecified"},
    {"code": "J45.909", "description": "Unspecified asthma, uncomplicated"},
    
    # Diseases of the digestive system (K00-K95)
    {"code": "K21.9", "description": "Gastro-esophageal reflux disease without esophagitis"},
    {"code": "K29.70", "description": "Gastritis, unspecified, without bleeding"},
    {"code": "K30", "description": "Functional dyspepsia"},
    {"code": "K58.9", "description": "Irritable bowel syndrome without diarrhea"},
    {"code": "K59.00", "description": "Constipation, unspecified"},
    {"code": "K80.20", "description": "Calculus of gallbladder without cholecystitis without obstruction"},
    {"code": "K92.9", "description": "Disease of digestive system, unspecified"},
    
    # Diseases of the skin and subcutaneous tissue (L00-L99)
    {"code": "L20.9", "description": "Atopic dermatitis, unspecified"},
    {"code": "L30.9", "description": "Dermatitis, unspecified"},
    {"code": "L50.9", "description": "Urticaria, unspecified"},
    {"code": "L60.0", "description": "Ingrowing nail"},
    {"code": "L70.0", "description": "Acne vulgaris"},
    
    # Diseases of the musculoskeletal system (M00-M99)
    {"code": "M25.50", "description": "Pain in unspecified joint"},
    {"code": "M54.5", "description": "Low back pain"},
    {"code": "M54.2", "description": "Cervicalgia"},
    {"code": "M79.3", "description": "Panniculitis, unspecified"},
    {"code": "M79.1", "description": "Myalgia"},
    {"code": "M19.90", "description": "Unspecified osteoarthritis, unspecified site"},
    {"code": "M81.0", "description": "Age-related osteoporosis without current pathological fracture"},
    {"code": "M62.81", "description": "Muscle weakness (generalized)"},
    
    # Diseases of the genitourinary system (N00-N99)
    {"code": "N18.9", "description": "Chronic kidney disease, unspecified"},
    {"code": "N30.00", "description": "Acute cystitis without hematuria"},
    {"code": "N39.0", "description": "Urinary tract infection, site not specified"},
    {"code": "N40.0", "description": "Benign prostatic hyperplasia without lower urinary tract symptoms"},
    {"code": "N92.0", "description": "Excessive and frequent menstruation with regular cycle"},
    {"code": "N94.6", "description": "Dysmenorrhea, unspecified"},
    
    # Pregnancy, childbirth and the puerperium (O00-O9A)
    {"code": "O21.9", "description": "Vomiting of pregnancy, unspecified"},
    {"code": "O26.90", "description": "Pregnancy related conditions, unspecified, unspecified trimester"},
    
    # Symptoms, signs and abnormal findings (R00-R99)
    {"code": "R05.9", "description": "Cough, unspecified"},
    {"code": "R06.02", "description": "Shortness of breath"},
    {"code": "R07.9", "description": "Chest pain, unspecified"},
    {"code": "R10.9", "description": "Unspecified abdominal pain"},
    {"code": "R11.0", "description": "Nausea"},
    {"code": "R11.2", "description": "Nausea with vomiting, unspecified"},
    {"code": "R19.7", "description": "Diarrhea, unspecified"},
    {"code": "R50.9", "description": "Fever, unspecified"},
    {"code": "R51.9", "description": "Headache, unspecified"},
    {"code": "R53.83", "description": "Other fatigue"},
    {"code": "R63.4", "description": "Abnormal weight loss"},
    {"code": "R73.09", "description": "Other abnormal glucose"},
    
    # Injury, poisoning and consequences of external causes (S00-T88)
    {"code": "S06.0X0A", "description": "Concussion without loss of consciousness, initial encounter"},
    {"code": "S13.4XXA", "description": "Sprain of ligaments of cervical spine, initial encounter"},
    {"code": "S43.401A", "description": "Unspecified sprain of right shoulder joint, initial encounter"},
    {"code": "S83.511A", "description": "Sprain of anterior cruciate ligament of right knee, initial encounter"},
    {"code": "S93.401A", "description": "Sprain of unspecified ligament of right ankle, initial encounter"},
    {"code": "T14.90XA", "description": "Injury, unspecified, initial encounter"},
    
    # External causes of morbidity (V00-Y99)
    {"code": "W19.XXXA", "description": "Unspecified fall, initial encounter"},
    
    # Additional common conditions
    {"code": "Z00.00", "description": "Encounter for general adult medical examination without abnormal findings"},
    {"code": "Z01.419", "description": "Encounter for gynecological examination (general) (routine) without abnormal findings"},
    {"code": "Z23", "description": "Encounter for immunization"},
    {"code": "Z79.4", "description": "Long term (current) use of insulin"},
    {"code": "Z79.899", "description": "Other long term (current) drug therapy"},
    {"code": "Z86.59", "description": "Personal history of other mental and behavioral disorders"},
    {"code": "Z87.891", "description": "Personal history of nicotine dependence"},
]
