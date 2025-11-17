# full_assignment_pdf.py
from fpdf import FPDF
from graphviz import Digraph
import os

# -------------------------------------------------------
# Step 1: Generate the workflow diagram as PNG
# -------------------------------------------------------
dot = Digraph(comment='Hospital Readmission Prediction Workflow')

# Define nodes
dot.node('A', 'Data Collection\n(EHR, Labs, Demographics)')
dot.node('B', 'Data Preprocessing\n(Cleaning, Encoding, Feature Engineering)')
dot.node('C', 'Model Development\n(XGBoost, Train/Test Split, Hyperparameter Tuning)')
dot.node('D', 'Evaluation & Validation\n(Precision, Recall, Confusion Matrix)')
dot.node('E', 'Deployment\n(API, EHR Integration, Monitoring)')
dot.node('F', 'Monitoring & Feedback\n(Concept Drift, Model Retraining)')

# Define edges
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])

# Save as PDF first
diagram_pdf = 'hospital_workflow.pdf'
dot.render('hospital_workflow', format='pdf', cleanup=True)

# Convert PDF to PNG for embedding in FPDF (requires ImageMagick installed)
diagram_png = 'hospital_workflow.png'
os.system(f'magick {diagram_pdf} {diagram_png}')  # Windows or Linux

# -------------------------------------------------------
# Step 2: Prepare the PDF with assignment text
# -------------------------------------------------------
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# -------------------------------
# Cover Page
# -------------------------------
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Hospital Readmission Prediction Using the AI Development Workflow", align='C')
pdf.ln(10)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Course: AI for Software Engineering\n"
    "Student: [Your Name]\n"
    "Duration: 7 Days\n"
    "Total Points: 100\n"
)
pdf.add_page()

# -------------------------------
# Table of Contents
# -------------------------------
pdf.set_font("Arial", 'B', 14)
pdf.multi_cell(0, 10, "Table of Contents")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "1. Part 1 — Short Answers\n"
    "2. Part 2 — Case Study Application\n"
    "3. Part 3 — Critical Thinking\n"
    "4. Part 4 — Reflection & Workflow Diagram\n"
    "5. Appendix (Python Code & Diagrams)\n"
)
pdf.add_page()

# -------------------------------
# PART 1 — Short Answers
# -------------------------------
pdf.set_font("Arial", 'B', 14)
pdf.multi_cell(0, 10, "Part 1 — Short Answers (30 points)")

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "1. Problem Definition (6 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Hypothetical AI Problem: Predicting early student dropout in an online learning platform.\n\n"
    "Objectives:\n"
    "1. Identify students at high dropout risk within the first 4 weeks.\n"
    "2. Provide actionable insights for instructors and advisors.\n"
    "3. Reduce overall dropout rate by enabling targeted interventions.\n\n"
    "Stakeholders:\n"
    "- Students: directly affected by predictions and interventions.\n"
    "- Instructors & Academic Advisors: use predictions to support struggling learners.\n\n"
    "KPI (Key Performance Indicator): Area Under the ROC Curve (AUC) — evaluates ability to distinguish likely dropouts from non-dropouts.\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "2. Data Collection & Preprocessing (8 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Two data sources:\n"
    "1. Learning Management System logs (activity time, quiz attempts).\n"
    "2. Student demographic & enrollment data.\n\n"
    "Potential bias:\n"
    "Students with limited internet connectivity may appear disengaged, skewing risk scores unfairly.\n\n"
    "Three preprocessing steps:\n"
    "1. Handle missing log data by imputation.\n"
    "2. Normalize engagement metrics (min-max scaling).\n"
    "3. One-hot encode categorical program/major fields.\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "3. Model Development (8 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Model Choice: Random Forest — handles mixed data types, robust against noise, interpretable via feature importance.\n\n"
    "Data Split:\n- 70% training\n- 15% validation\n- 15% test\n\n"
    "Two hyperparameters to tune:\n- n_estimators: controls number of trees.\n- max_depth: prevents overfitting by limiting tree depth.\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "4. Evaluation & Deployment (8 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Two evaluation metrics:\n- Precision: crucial to avoid incorrectly flagging many low-risk students.\n- Recall: ensures the model catches most actual dropouts.\n\n"
    "Concept drift: occurs when data patterns change (e.g., new platform features).\nMonitoring: real-time performance dashboards comparing expected vs. actual behavior.\n\n"
    "Technical deployment challenge: Scalability — handling tens of thousands of predictions per hour during peak usage.\n"
)
pdf.add_page()

# -------------------------------
# PART 2 — Case Study
# -------------------------------
pdf.set_font("Arial", 'B', 14)
pdf.multi_cell(0, 10, "Part 2 — Case Study Application (40 points)")

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "1. Problem Scope (5 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Definition: Build a predictive model that estimates whether a patient will be readmitted within 30 days.\n\n"
    "Objectives:\n1. Reduce preventable readmissions.\n2. Optimize resource allocation.\n3. Improve quality-of-care metrics.\n\n"
    "Stakeholders:\n- Hospital administration\n- Physicians & medical staff\n- Insurance providers\n- Patients\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "2. Data Strategy (10 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Data Sources:\n1. Electronic Health Records (EHRs)\n2. Patient demographics & medical history\n3. Lab tests, diagnosis codes, medications\n\n"
    "Ethical Concerns:\n1. Privacy & HIPAA compliance — misuse of sensitive patient health data.\n"
    "2. Bias against minority groups — unequal readmission predictions.\n\n"
    "Preprocessing Pipeline:\n1. Remove '?' markers, standardize missing values.\n2. Convert diagnosis codes to categorical.\n3. Standardize numeric fields.\n4. One-hot encode categorical variables.\n"
    "5. Feature engineer: total visits, chronic condition scores.\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "3. Model Development (10 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Selected Model: XGBoost Classifier — high performance, handles class imbalance well.\n\n"
    "Hypothetical Confusion Matrix:\n"
    "Actual vs Predicted:\n"
    "--------------------------\n"
    "Actual Yes | Predicted Yes: 180 | Predicted No: 70\n"
    "Actual No  | Predicted Yes: 120 | Predicted No: 1320\n\n"
    "Precision: 180 / (180 + 120) = 0.60\n"
    "Recall: 180 / (180 + 70) = 0.72\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "4. Deployment (10 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Integration Steps:\n1. Save trained model as .pkl\n2. Wrap in a FastAPI or Flask microservice\n"
    "3. Expose /predict endpoint\n4. Integrate into hospital EHR system UI\n5. Log predictions for audit and drift detection\n\n"
    "Regulatory Compliance:\n- Encrypt data at rest and in transit\n- Access control (RBAC)\n- Audit logs for all predictions\n- Follow HIPAA minimum necessary rule\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "5. Optimization (5 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Method to reduce overfitting: Apply early stopping during XGBoost training.\n"
)
pdf.add_page()

# -------------------------------
# PART 3 — Critical Thinking
# -------------------------------
pdf.set_font("Arial", 'B', 14)
pdf.multi_cell(0, 10, "Part 3 — Critical Thinking (20 points)")

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "1. Ethics & Bias (10 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Impact of biased data: If minority patients historically received poorer care, the model may mislabel them as high-risk, influencing treatment unfairly.\n\n"
    "Mitigation Strategy: Implement fairness-aware reweighting or equal opportunity metrics during evaluation.\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "2. Trade-offs (10 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "Interpretability vs Accuracy: Highly accurate models (XGBoost, NN) are less transparent.\n"
    "Interpretable models (Logistic Regression) may have lower accuracy.\n"
    "Healthcare tends to favor interpretability, but hybrid approaches like SHAP explanations are ideal.\n\n"
    "Limited computational resources: Hospitals may lack GPUs; therefore simpler, lighter models may be required (Random Forest, Logistic Regression).\n"
)
pdf.add_page()

# -------------------------------
# PART 4 — Reflection & Diagram
# -------------------------------
pdf.set_font("Arial", 'B', 14)
pdf.multi_cell(0, 10, "Part 4 — Reflection & Workflow Diagram (10 points)")

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "Reflection (5 points)")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8,
    "The hardest part of the workflow was data preprocessing, especially handling mixed-format diagnosis codes and missing data. "
    "With more resources, I would implement automated data validation, a feature store, and a CI/CD pipeline for ML models.\n"
)
pdf.add_page()

pdf.set_font("Arial", 'B', 12)
pdf.multi_cell(0, 8, "Workflow Diagram (5 points)")

# Add diagram PNG
if os.path.exists(diagram_png):
    pdf.image(diagram_png, x=15, y=None, w=180)

# -------------------------------
# Save final PDF
# -------------------------------
output_pdf = "full_assignment.pdf"
pdf.output(output_pdf)
print(f"Full assignment PDF generated: {output_pdf}")
