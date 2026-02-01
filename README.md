Overview

This project is an end-to-end Machine Learning pipeline designed for Network Security Data analysis. The pipeline involves data ingestion from a MongoDB database, data validation, transformation, model training, evaluation, and model deployment. The objective is to predict network security events using a trained machine learning model.

Key components used in this project:

    Database: MongoDB
    Experiment Tracking: MLFlow
    Remote Repository: Dagshub
    Web Interface: FastAPI

Pipeline Components
Data Ingestion

The Data Ingestion phase is crucial for setting up the initial dataset required for the Machine Learning workflow. This step ingests data from a MongoDB database and structures it for further processing. Below is a breakdown of the Data Ingestion process:

Data Ingestion
Key Steps:

    Configuration:
        The Data Ingestion Config specifies various paths:
            Data Ingestion Directory: Directory where the ingested data will be stored.
            Feature Store File Path: Path for the feature store which holds the raw data.
            Training and Testing File Paths: Paths where training and testing datasets will be saved.
            Collection Name: Name of the MongoDB collection from which data will be ingested.
            Train-Test Split Ratio: Defines the proportion of data allocated for training versus testing.

    Initiate Data Ingestion:
        The process begins by calling the data ingestion function, which connects to the specified MongoDB database.

    Export Data to Feature Store:
        The data is exported to the feature store as a CSV file. This is the raw data and serves as the baseline for all subsequent processes.

    Data Ingestion Artifact:
        Finally, a Data Ingestion Artifact is created to maintain metadata about the ingestion process, including timestamps and paths to the ingested files.

Output:

    The end result of the Data Ingestion process is the creation of:
        Feature Store containing the raw dataset as CSV.
        Ingested Data folders containing train.csv and test.csv files for subsequent processing.

This structured approach ensures that the data flow into the pipeline is efficient, clean, and well-documented, providing a strong foundation for further stages of the data processing pipeline.
Data Validation

The Data Validation phase ensures that the ingested data meets the necessary quality standards before proceeding to the next steps in the Machine Learning pipeline. The following diagram outlines the key aspects of this process:

Data Validation
Overview of the Process:

    Configuration:
        The process starts with a Data Validation Config that defines directories for valid and invalid data, as well as paths for drift reports.

    Initiate Validation:
        Data validation is initiated, starting with reading the ingested CSV files (train.csv and test.csv).

    Column Validation:
        The number of columns and their data types is validated against the predefined schema. This includes checks to ensure the correct columns are present and that numerical columns exist.

    Validation Status:
        The validation status is recorded, indicating whether any columns are missing or if there are issues with the data types.

    Dataset Drift Detection:
        If the initial validation passes, the process checks for dataset drift, which helps ensure that the data remains consistent with the training parameters.

    Data Validation Artifact:
        Finally, a Data Validation Artifact is created, summarizing the validation status and producing a drift report in JSON format.
