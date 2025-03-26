import streamlit as st
import hashlib

# Initialize an empty hospital ledger (a dictionary where keys are patient names)
hospital_ledger_advanced = {}

# Function to generate a hash (assuming it is based on the patient name, treatment, cost, and date of visit)
def generate_hash(patient_name, treatment, cost, date_of_visit):
    data_string = f"{patient_name}{treatment}{cost}{date_of_visit}"
    return hashlib.sha256(data_string.encode()).hexdigest()

# Function to add or update patient visits
def add_patient_visit_advanced(patient_name, treatment, cost, date_of_visit):
    # Check if the patient already exists
    if patient_name in hospital_ledger_advanced:
        st.write(f"Updating visit record for {patient_name}.")
    else:
        st.write(f"Adding new visit record for {patient_name}.")

    # Generate a hash for this visit record
    visit_hash = generate_hash(patient_name, treatment, cost, date_of_visit)

    # Create a dictionary for the visit with the hash
    visit = {
        "treatment": treatment,
        "cost": cost,
        "date_of_visit": date_of_visit,
        "visit_hash": visit_hash  # Store the hash to verify data integrity
    }

    # Add the visit to the patient's list of visits (using a dictionary)
    if patient_name not in hospital_ledger_advanced:
        hospital_ledger_advanced[patient_name] = []

    hospital_ledger_advanced[patient_name].append(visit)
    st.write(f"Visit added for {patient_name} on {date_of_visit} for treatment {treatment} costing ${cost}.")
    st.write(f"Visit hash: {visit_hash}")

# Streamlit user interface
st.title("Hospital  System")

# Inputs for patient visit
patient_name = st.text_input("Enter the patient's name:").lower()
treatment = st.text_input("Enter the treatment received:")
cost = st.number_input("Enter the cost of the treatment: $", min_value=0.0, step=0.1)
date_of_visit = st.date_input("Enter the date of visit:")

# Add patient visit when button is clicked
if st.button("Add Patient Visit"):
    if patient_name and treatment and cost and date_of_visit:
        add_patient_visit_advanced(patient_name, treatment, cost, date_of_visit)
    else:
        st.write("Please fill in all fields.")

# Searching for a patient’s visit
search_patient = st.text_input("\nEnter patient name to search for:").lower()

if search_patient:
    if search_patient in hospital_ledger_advanced:
        st.write(f"\nVisit records for {search_patient}:")
        for visit in hospital_ledger_advanced[search_patient]:
            st.write(f"  Treatment: {visit['treatment']}, Cost: ${visit['cost']}, Date: {visit['date_of_visit']}, Hash: {visit['visit_hash']}")
    else:
        st.write(f"Patient {search_patient} not found in the ledger.")
