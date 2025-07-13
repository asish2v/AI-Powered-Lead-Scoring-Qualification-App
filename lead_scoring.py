import random

def score_lead(row):
    score = 0

    # Job title scoring
    if 'CEO' in row['job_title'] or 'Founder' in row['job_title']:
        score += 40
    elif 'CTO' in row['job_title'] or 'VP' in row['job_title']:
        score += 30
    elif 'Manager' in row['job_title']:
        score += 20
    else:
        score += 10

    # Domain scoring
    if ".ai" in row['domain'] or ".tech" in row['domain']:
        score += 20
    elif ".com" in row['domain']:
        score += 10

    # Location scoring
    major_cities = ['New York', 'San Francisco', 'Chicago', 'Boston']
    if row['location'] in major_cities:
        score += 10

    # LinkedIn presence
    if isinstance(row['linkedin'], str) and "linkedin.com" in row['linkedin']:
        score += 20

    return min(score, 100)

def confidence_level(score):
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"

def estimate_revenue(row):
    if "CEO" in row['job_title'] or "VP" in row['job_title']:
        return "$50K+"
    elif "Manager" in row['job_title']:
        return "$10K–$25K"
    else:
        return "$5K–$10K"

def verify_email(email):
    # Mocked logic – simulate real API response
    return random.choice(["Valid", "Invalid", "Unknown"])
