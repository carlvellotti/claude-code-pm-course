#!/usr/bin/env python3
"""
Generate realistic CSV data for Module 2.2: Data-Driven Feature Development
Uses only Python standard library (no pandas/numpy required)
"""

import csv
import random
from datetime import datetime, timedelta
from collections import defaultdict
import math

# Set seed for reproducibility
random.seed(42)

def weighted_choice(choices, weights):
    """Select from choices with given weights"""
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for choice, weight in zip(choices, weights):
        if upto + weight >= r:
            return choice
        upto += weight
    return choices[-1]

def gamma_sample(shape, scale):
    """Simple gamma distribution approximation"""
    # Using sum of exponentials approximation
    total = 0
    for _ in range(int(shape)):
        total += random.expovariate(1.0 / scale)
    return total

def normal_sample(mean, std):
    """Normal distribution using Box-Muller transform"""
    u1 = random.random()
    u2 = random.random()
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    return mean + z0 * std

print("Generating Module 2.2 data files...")

# ============================================================================
# FILE 1: taskflow-usage-data-q4.csv (1000 rows of event data)
# ============================================================================
print("\n1. Generating taskflow-usage-data-q4.csv...")

company_sizes = ['5-20', '21-99', '100+']
company_size_weights = [0.6, 0.3, 0.1]

user_roles = ['PM', 'Engineer', 'Designer', 'Manager', 'Founder']
industries = ['SaaS', 'E-commerce', 'FinTech', 'HealthTech', 'EdTech', 'Marketing']

start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 12, 31)

users_data = []
num_users = 250

for i in range(num_users):
    user_id = f"user_{i+1:04d}"
    company_size = weighted_choice(company_sizes, company_size_weights)
    user_role = random.choice(user_roles)
    industry = random.choice(industries)

    signup_time = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )

    users_data.append({
        'user_id': user_id,
        'event_type': 'signup',
        'timestamp': signup_time.isoformat(),
        'company_size': company_size,
        'user_role': user_role,
        'industry': industry
    })

    if random.random() < 0.72:
        task_created_time = signup_time + timedelta(minutes=random.randint(5, 60))
        users_data.append({
            'user_id': user_id,
            'event_type': 'first_task_created',
            'timestamp': task_created_time.isoformat(),
            'company_size': company_size,
            'user_role': user_role,
            'industry': industry
        })

        completion_prob = 0.38 if company_size == '5-20' else 0.42
        if random.random() < completion_prob:
            task_completed_time = task_created_time + timedelta(minutes=random.randint(10, 120))
            users_data.append({
                'user_id': user_id,
                'event_type': 'first_task_completed',
                'timestamp': task_completed_time.isoformat(),
                'company_size': company_size,
                'user_role': user_role,
                'industry': industry
            })

            if random.random() < 0.5:
                invite_time = task_completed_time + timedelta(hours=random.randint(1, 48))
                users_data.append({
                    'user_id': user_id,
                    'event_type': 'invite_sent',
                    'timestamp': invite_time.isoformat(),
                    'company_size': company_size,
                    'user_role': user_role,
                    'industry': industry
                })

with open('taskflow-usage-data-q4.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['user_id', 'event_type', 'timestamp', 'company_size', 'user_role', 'industry'])
    writer.writeheader()
    writer.writerows(users_data)

print(f"   ✓ Created {len(users_data)} rows")

# ============================================================================
# FILE 2: activation-funnel-q4.csv (aggregated funnel)
# ============================================================================
print("\n2. Generating activation-funnel-q4.csv...")

funnel_data = [
    ['Signup', 10000, 10000, 1.0, 0],
    ['First Task Created', 10000, 7200, 0.72, 18],
    ['First Task Completed', 7200, 2880, 0.40, 45],
    ['Invite Sent', 2880, 1440, 0.50, 24]
]

with open('activation-funnel-q4.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['step', 'users_entered', 'users_completed', 'completion_rate', 'median_time_to_complete'])
    writer.writerows(funnel_data)

print(f"   ✓ Created {len(funnel_data)} rows")

# ============================================================================
# FILE 3: user-survey-responses.csv (800 survey responses)
# ============================================================================
print("\n3. Generating user-survey-responses.csv...")

confusion_themes = {
    "didn't know what to create": [
        "I didn't know what to create",
        "Wasn't sure what kind of tasks to make",
        "Stared at empty project not knowing what to do",
        "Unclear what I should create first",
        "No idea what to put in the task"
    ],
    "needed examples": [
        "Needed examples to get started",
        "Wish there were templates or samples",
        "Would help to see what a good task looks like",
        "Examples would have been helpful",
        "Show me a sample project"
    ],
    "overwhelmed": [
        "Felt overwhelmed by the blank canvas",
        "Too many options, didn't know where to start",
        "Blank project was intimidating",
        "Paralyzed by all the empty fields",
        "Overwhelmed by all the customization options"
    ],
    "other": [
        "Navigation was confusing",
        "Couldn't find the features I needed",
        "Too many clicks to do simple things",
        "Interface wasn't intuitive",
        "Expected it to work differently"
    ]
}

feature_requests = {
    "didn't know what to create": "Templates or examples",
    "needed examples": "Sample projects or templates",
    "overwhelmed": "Simpler onboarding",
    "other": "Better help docs"
}

survey_data = []
for i in range(800):
    user_id = f"survey_user_{i+1:04d}"
    company_size = weighted_choice(company_sizes, company_size_weights)

    if company_size == '5-20':
        theme_weights = [0.42, 0.33, 0.20, 0.05]
    else:
        theme_weights = [0.25, 0.20, 0.25, 0.30]

    theme = weighted_choice(list(confusion_themes.keys()), theme_weights)
    confusion_text = random.choice(confusion_themes[theme])

    survey_data.append({
        'user_id': user_id,
        'company_size': company_size,
        'onboarding_rating': random.randint(2, 4),
        'biggest_confusion': confusion_text,
        'feature_request': feature_requests[theme],
        'would_recommend': random.choice(['No', 'Maybe', 'Maybe', 'Yes'])
    })

with open('user-survey-responses.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['user_id', 'company_size', 'onboarding_rating', 'biggest_confusion', 'feature_request', 'would_recommend'])
    writer.writeheader()
    writer.writerows(survey_data)

print(f"   ✓ Created {len(survey_data)} rows")

# ============================================================================
# FILE 4: onboarding-experiment-results.csv (8,000 rows - THE BIG ONE)
# ============================================================================
print("\n4. Generating onboarding-experiment-results.csv...")

experiment_data = []

company_size_dist = {
    '5-20': 2400,
    '21-99': 1200,
    '100+': 400
}

user_counter = 0

for cohort in ['control', 'treatment']:
    for company_size, count in company_size_dist.items():
        if cohort == 'control':
            if company_size == '5-20':
                activation_rate = 0.448
            elif company_size == '21-99':
                activation_rate = 0.455
            else:
                activation_rate = 0.456
        else:
            if company_size == '5-20':
                activation_rate = 0.562
            elif company_size == '21-99':
                activation_rate = 0.471
            else:
                activation_rate = 0.421

        for i in range(count):
            user_id = f"{cohort}_user_{user_counter:04d}"
            user_counter += 1
            user_role = random.choice(user_roles)

            signup_date = datetime(2024, 10, 1) + timedelta(days=random.randint(0, 60))
            completed_first_task = random.random() < activation_rate

            if completed_first_task:
                if cohort == 'treatment':
                    time_to_first_task = int(gamma_sample(2, 10))
                else:
                    time_to_first_task = int(gamma_sample(3, 15))
            else:
                time_to_first_task = None

            invited_teammate = random.random() < (0.348 if cohort == 'treatment' else 0.121)
            used_task_template = random.random() < (0.352 if cohort == 'treatment' else 0.109)

            if completed_first_task:
                if cohort == 'treatment':
                    days_active = min(7, max(0, int(normal_sample(5.5, 1.5))))
                    tasks_completed = max(1, int(gamma_sample(3, 2.3)))
                else:
                    days_active = min(7, max(0, int(normal_sample(4.2, 2))))
                    tasks_completed = max(1, int(gamma_sample(2, 1.5)))
            else:
                days_active = min(7, max(0, int(random.expovariate(1.0))))
                tasks_completed = 0

            experiment_data.append({
                'user_id': user_id,
                'cohort': cohort,
                'signup_date': signup_date.strftime('%Y-%m-%d'),
                'company_size': company_size,
                'user_role': user_role,
                'completed_first_task': str(completed_first_task),
                'time_to_first_task_minutes': time_to_first_task if time_to_first_task is not None else '',
                'invited_teammate': str(invited_teammate),
                'used_task_template': str(used_task_template),
                'days_active_week_1': days_active,
                'tasks_completed_week_1': tasks_completed
            })

with open('onboarding-experiment-results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['user_id', 'cohort', 'signup_date', 'company_size', 'user_role',
                                            'completed_first_task', 'time_to_first_task_minutes', 'invited_teammate',
                                            'used_task_template', 'days_active_week_1', 'tasks_completed_week_1'])
    writer.writeheader()
    writer.writerows(experiment_data)

print(f"   ✓ Created {len(experiment_data)} rows")

# ============================================================================
# VALIDATION: Print statistics to verify
# ============================================================================
print("\n" + "="*70)
print("VALIDATION: Checking experiment statistics")
print("="*70)

# Calculate statistics
control_data = [r for r in experiment_data if r['cohort'] == 'control']
treatment_data = [r for r in experiment_data if r['cohort'] == 'treatment']

control_activated = [r for r in control_data if r['completed_first_task'] == 'True']
treatment_activated = [r for r in treatment_data if r['completed_first_task'] == 'True']

control_rate = len(control_activated) / len(control_data)
treatment_rate = len(treatment_activated) / len(treatment_data)

print(f"\n📊 Overall Activation Rates:")
print(f"   Control:   {control_rate:.3f} (target: 0.452)")
print(f"   Treatment: {treatment_rate:.3f} (target: 0.478)")
print(f"   Lift:      {(treatment_rate - control_rate):.3f} (target: 0.026)")

print(f"\n📊 Activation Rates by Segment:")
for size in ['5-20', '21-99', '100+']:
    control_seg = [r for r in control_data if r['company_size'] == size]
    treatment_seg = [r for r in treatment_data if r['company_size'] == size]

    control_seg_activated = len([r for r in control_seg if r['completed_first_task'] == 'True'])
    treatment_seg_activated = len([r for r in treatment_seg if r['completed_first_task'] == 'True'])

    control_seg_rate = control_seg_activated / len(control_seg)
    treatment_seg_rate = treatment_seg_activated / len(treatment_seg)
    lift = treatment_seg_rate - control_seg_rate

    print(f"\n   {size:8s}")
    print(f"      Control:   {control_seg_rate:.3f}")
    print(f"      Treatment: {treatment_seg_rate:.3f}")
    print(f"      Lift:      {lift:+.3f}")

# Retention
control_retention = len([r for r in control_activated if int(r['days_active_week_1']) >= 3]) / len(control_activated)
treatment_retention = len([r for r in treatment_activated if int(r['days_active_week_1']) >= 3]) / len(treatment_activated)

print(f"\n📊 Week 1 Retention (Activated Users Only):")
print(f"   Control:   {control_retention:.3f} (target: ~0.601)")
print(f"   Treatment: {treatment_retention:.3f} (target: ~0.784)")
print(f"   Lift:      {(treatment_retention - control_retention):+.3f}")

# Tasks
control_tasks = sum(int(r['tasks_completed_week_1']) for r in control_activated) / len(control_activated)
treatment_tasks = sum(int(r['tasks_completed_week_1']) for r in treatment_activated) / len(treatment_activated)

print(f"\n📊 Tasks Completed (Week 1, Activated Users):")
print(f"   Control:   {control_tasks:.1f} tasks (target: ~2.9)")
print(f"   Treatment: {treatment_tasks:.1f} tasks (target: ~6.8)")
print(f"   Ratio:     {treatment_tasks/control_tasks:.1f}x")

# Feature adoption
control_templates = len([r for r in control_data if r['used_task_template'] == 'True']) / len(control_data)
treatment_templates = len([r for r in treatment_data if r['used_task_template'] == 'True']) / len(treatment_data)

control_invites = len([r for r in control_data if r['invited_teammate'] == 'True']) / len(control_data)
treatment_invites = len([r for r in treatment_data if r['invited_teammate'] == 'True']) / len(treatment_data)

print(f"\n📊 Feature Adoption:")
print(f"   Template Usage:")
print(f"      Control:   {control_templates:.3f} (target: ~0.109)")
print(f"      Treatment: {treatment_templates:.3f} (target: ~0.352)")
print(f"      Ratio:     {treatment_templates/control_templates:.1f}x")
print(f"\n   Invite Teammate:")
print(f"      Control:   {control_invites:.3f} (target: ~0.121)")
print(f"      Treatment: {treatment_invites:.3f} (target: ~0.348)")
print(f"      Ratio:     {treatment_invites/control_invites:.1f}x")

print("\n" + "="*70)
print("✅ All files generated successfully!")
print("="*70)
print("\nGenerated files:")
print("   1. taskflow-usage-data-q4.csv")
print("   2. activation-funnel-q4.csv")
print("   3. user-survey-responses.csv")
print("   4. onboarding-experiment-results.csv")
print("\nReady for Module 2.2! 🎉")
