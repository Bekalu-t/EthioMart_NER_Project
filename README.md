# EthioMart Amharic NER Project

## Overview
This project aims to build an Amharic Named Entity Recognition (NER) system for EthioMart, a centralized platform for Telegram-based e-commerce in Ethiopia. The system extracts key entities (e.g., Product, Price, Location) from Telegram messages to create a comprehensive e-commerce hub and support micro-lending decisions for vendors.

## Project Goals
- Develop a workflow for data ingestion, preprocessing, and labeling from Telegram channels.
- Fine-tune transformer-based models for Amharic NER tasks.
- Compare models and use interpretability tools (SHAP, LIME) to ensure accuracy and trust.
- Create a Vendor Analytics Engine for micro-lending scorecards.

## Tasks
1. **Data Ingestion and Preprocessing** - Collect and clean data from Telegram channels.
2. **Data Labeling** - Label data in CoNLL format for NER.
3. **Model Fine-Tuning** - Adapt pre-trained LLMs for Amharic NER.
4. **Model Comparison** - Evaluate and select the best model.
5. **Model Interpretability** - Analyze model predictions.
6. **Vendor Scorecard** - Develop metrics for micro-lending.

## Setup
- **Environment**: Visual Studio Code, Python 3.x
- **Dependencies**: Install required libraries (e.g., `telethon`, `transformers`, `pandas`) using:
  ```bash
  pip install telethon transformers pandas