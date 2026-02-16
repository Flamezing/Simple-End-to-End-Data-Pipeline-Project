📊 Simple End-to-End Data Pipeline Project
📌 Project Overview

This project demonstrates a complete end-to-end data pipeline, from raw CSV ingestion to cleaned data output and analytical visualization.

The goal is to simulate a real-world data engineering workflow:

1. Load raw data
2. Validate and transform structured fields
3. Generate clean dataset
4. Perform exploratory data analysis (EDA)
5. Visualize insights



📊 Data Pipeline (pipeline.py)

The pipeline performs structured data validation and transformation.

🔹 Step 1 — Load Raw Data
  Reads background_noise_focus_dataset.csv

🔹 Step 2 — Data Cleaning
  Remove duplicate rows

🔹 Step 3 — Field Validation & Transformation
  Each numeric column is:
    Parsed using pd.to_numeric(errors="coerce")
    Checked for invalid values
    Enforced within logical range constraints
    Validated for monotonic and uniqueness where necessary

🔹 Step 4 — Export Clean Data

  

📈 Data Analysis (analysis.py)

After cleaning, visualization is performed using Matplotlib.

🔹 Role Distribution

  Aggregates participant roles
  Displays frequency distribution via bar chart

<img src="images/role_count_bar.png" alt="role_count_bar" title="role_count_bar" width="400">



🔹 Noise Type vs Focus Score

For each background noise type:
  Groups dataset
  Counts perceived focus scores
  Generates individual subplots
  Displays score distribution trends

<img src="images/noise_focus_plot.png" alt="noise_focus_plot" title="noise_focus_plot" width="400">



🛠️ Tech Stack

  Python
  
  Pandas
  
  NumPy
  
  Matplotlib


🎯 Project Purpose
This project is designed to:

  Practice structured data engineering workflow
  
  Strengthen data validation logic design
  
  Demonstrate end-to-end reproducibility
  
  Serve as a portfolio-ready project for internships


📌 Future Improvements
Add logging instead of print statements
  
  Introduce unit testing
  
  Convert pipeline into reusable class structure
  
  Add configuration file support
  
  Containerize with Docker
