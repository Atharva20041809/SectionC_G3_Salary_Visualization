"""
Automated ETL Pipeline: Adult Census Income
This script extracts raw data, cleans it thoroughly (snake_case conversion, removing NaN leakage by executing explicit mode substitution, handling drops), and transforms variables before pipelining it straight to our processed architecture.
"""

import os
import logging
import pandas as pd
import numpy as np

# Configure Logging Console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AdultDataPipeline:
    def __init__(self, raw_path: str, processed_path: str):
        self.raw_path = raw_path
        self.processed_path = processed_path
        self.df = None

    def extract(self):
        """Phase 1: Ingest RAW data."""
        logging.info(f"Extracting data from {self.raw_path}...")
        try:
            self.df = pd.read_csv(self.raw_path, skipinitialspace=True)
            logging.info(f"Extraction successful. Received {self.df.shape[0]} rows and {self.df.shape[1]} columns.")
        except FileNotFoundError:
            logging.error(f"Failed to find raw dataset at {self.raw_path}. Is it available?")
            raise

    def transform_and_clean(self):
        """Phase 2: Perform Data Cleaning and Semantic Transformations."""
        logging.info("Initiating Data Cleaning and Transformations...")
        
        # 1. Standardize Schema
        self.df.columns = self.df.columns.str.lower().str.replace('-', '_')
        logging.info("Standardized column names to snake_case format.")
        
        # 2. Structural Drops
        if 'fnlwgt' in self.df.columns:
            self.df.drop('fnlwgt', axis=1, inplace=True)
            logging.info("Dropped irrelevant statistical weight column ('fnlwgt').")

        # 3. Handle Strict Missing Patterns Natively
        logging.info("Imputing system missing categorical values with modes...")
        self.df.replace('?', np.nan, inplace=True)
        for col in self.df.columns:
            # We strictly fill to avoid np.nan leakage across any dataset serialization boundaries.
            mode_value = self.df[col].mode()[0]
            self.df[col] = self.df[col].fillna(mode_value)
            
        # 4. Whitespace Trimming
        for col in self.df.select_dtypes(include=['object']).columns:
            self.df[col] = self.df[col].str.strip()

        # Deduplication
        initial_count = len(self.df)
        self.df.drop_duplicates(inplace=True)
        dropped_count = initial_count - len(self.df)
        logging.info(f"Removed {dropped_count} duplicate records.")

        # 5. Semantic Transformations
        logging.info("Performing analytical feature transformations...")
        
        # Binary target transform
        self.df['income'] = self.df['income'].apply(lambda x: 1 if x in ['>50K', '>50K.'] else 0)
        
        # Demographics Engine Bucketizing
        bins = [16, 25, 45, 65, 100]
        labels = ['Youth', 'YoungAdult', 'Adult', 'Senior']
        self.df['age_group'] = pd.cut(self.df['age'], bins=bins, labels=labels)
        
        logging.info("Transformations complete.")

    def load(self):
        """Phase 3: Safely output analytical clean data."""
        os.makedirs(os.path.dirname(self.processed_path), exist_ok=True)
        self.df.to_csv(self.processed_path, index=False)
        logging.info(f"Pipeline successfully finalized. Processed data resides at [{self.processed_path}] with schema shape {self.df.shape}")

    def run_pipeline(self):
        """Execute end to end Pipeline."""
        logging.info("=== STARTING ETL BATCH RUN ===")
        self.extract()
        self.transform_and_clean()
        self.load()
        logging.info("=== BATCH RUN COMPLETED ===")

if __name__ == "__main__":
    # Path Configuration mapping execution from script directly properly
    WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RAW_PATH = os.path.join(WORKSPACE_DIR, 'data', 'raw', 'adult.csv')
    PROCESSED_PATH = os.path.join(WORKSPACE_DIR, 'data', 'processed', 'adult_cleaned.csv')

    pipeline = AdultDataPipeline(raw_path=RAW_PATH, processed_path=PROCESSED_PATH)
    pipeline.run_pipeline()
