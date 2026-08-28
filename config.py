# In this file, you can set the configurations of the app.

from src.utils.constants import DEBUG, ERROR, LLM_MODEL, OPENAI
import os

#config related to logging must have prefix LOG_
LOG_LEVEL = 'INFO'
LOG_SELENIUM_LEVEL = ERROR
LOG_TO_FILE = True
LOG_TO_CONSOLE = True

MINIMUM_WAIT_TIME_IN_SECONDS = 60

JOB_APPLICATIONS_DIR = "job_applications"

# Job Suitability Score: 7 = 70% match threshold (0-10 scale)
# Only apply to jobs with 70% or higher match with job description
JOB_SUITABILITY_SCORE = 7

JOB_MAX_APPLICATIONS = 5
JOB_MIN_APPLICATIONS = 1

# ===== Groq Configuration =====
# Groq provides FREE API access with very fast inference
# Get your key from: https://console.groq.com/api-keys
# Store as GitHub Actions secret: ai_api_key
LLM_MODEL_TYPE = 'groq'
LLM_MODEL = 'mixtral-8x7b-32768'  # Fast, free model (recommended)
LLM_API_URL = 'https://api.groq.com/openai/v1'
