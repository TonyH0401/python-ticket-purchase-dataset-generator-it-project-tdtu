import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Parameters for dataset generation
num_customers = 100000
num_records = 5000000  # Target size for the dataset
date_range_start = datetime(2021, 1, 1)
date_range_end = datetime(2022, 12, 31)
ticket_quantity_range = (1, 10)
payment_types = ['Cash', 'Transaction']

# Provided list of event names
event_names = [
    "Tech Summit 2023", "Innovation Expo", "CodeCrafters Hackathon", "Future Trends Symposium",
    "Data Science Showcase", "Digital Marketing Forum", "Robotics Revolution", "Blockchain Bonanza",
    "AI Wonderland", "Space Exploration Expo", "HealthTech Symposium", "Eco-Friendly Innovations",
    "Virtual Reality Festival", "Cybersecurity Summit", "Game Developers Conference", "Startup Ignition",
    "Women in Tech Symposium", "FinTech Frontier", "Smart Cities Expo", "Global Hackfest",
    "Digital Arts Festival", "Quantum Computing Symposium", "Big Data Bash", "Wearable Tech Showcase",
    "Cloud Computing Carnival", "Genomics Gala", "Social Media Mastery", "Autonomous Vehicles Expo",
    "AR/VR Experience", "BioTech Breakthroughs", "Future of Work Conference", "Sustainable Energy Summit",
    "EdTech Extravaganza", "Agile Development Sprint", "SpaceX Launch Celebration", "Open Source Odyssey",
    "Gaming Galaxy", "Tech for Good Summit", "DevOps Days", "Internet of Things Expo", "Healthcare Hackathon",
    "Digital Transformation Forum", "Quantified Self Conference", "Cryptocurrency Carnival", "Mobile App Marathon",
    "Cyberpunk Coding Challenge", "Drones & Robotics Expo", "UX/UI Design Summit", "Data Privacy Symposium",
    "E-commerce Evolution", "Biohacking Bonanza", "Smart Agriculture Showcase", "Tech Talent Expo",
    "Cloud Security Congress", "Virtual Classroom Revolution", "Space Tourism Symposium", "Blockchain Revolution",
    "Tech Diversity & Inclusion Summit", "Human-Computer Interaction Expo", "Innovative Retail Solutions",
    "Health and Wellness Tech Fair", "Digital Accessibility Symposium", "Renewable Energy Expo", "Mobile Payments Summit",
    "Augmented Reality Adventure", "Data Ethics Symposium", "Future of Transportation Expo", "Gaming for Good Marathon",
    "Social Impact Tech Forum", "Neurotech Nexus", "Code for Climate Hackathon", "Industry 4.0 Expo", "VR for Education Symposium",
    "The Quantum Leap", "Space Colonization Conference", "Inclusive Design Showcase", "Blockchain for Social Impact",
    "Tech for Sustainable Cities", "Future of Retail Summit", "Human Augmentation Expo", "Digital Citizenship Symposium",
    "AI for Good Forum", "Zero Waste Tech Expo", "Smart Home Innovations", "AR in Healthcare Symposium",
    "Tech Ethics Roundtable", "Data for Democracy Hackathon", "Future of Finance Forum", "Voice Technology Showcase",
    "Space Innovation Challenge", "Green Tech Revolution", "Digital Inclusion Summit", "Gen Z Tech Festival",
    "Bioinformatics Bash", "Blockchain for Healthcare", "Tech for Mental Health Symposium", "Digital Nomad Expo",
    "Future of Food Tech", "Code for Equality Hackathon", "Quantum Networking Symposium"
]

# Generating unique CustomerNames and CustomerIDs using Faker
customer_names = [fake.unique.name() for _ in range(num_customers)]
customer_ids = [f"C{i:07d}" for i in range(num_customers)]
customer_data = pd.DataFrame(
    {'CustomerName': customer_names, 'CustomerID': customer_ids})

# Generating EventIDs for the provided EventNames
event_ids = [f"E{i:07d}" for i in range(len(event_names))]
event_data = pd.DataFrame({'EventName': event_names, 'EventID': event_ids})

# Function to generate a random date within the specified range
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Function to format the price
def format_price(price):
    return "{:,.0f}".format(price)

# Initialize DataFrame to store the dataset
dataset = pd.DataFrame()

# Loop to generate dataset in chunks
for gh in range(num_records // 10000):
    print(gh)
    # Generating sales data with prices in Vietnamese Dong
    sales_data = pd.DataFrame({
        'SaleDate': [random_date(date_range_start, date_range_end) for _ in range(10000)],
        'TicketQuantyPerEvent': np.random.randint(ticket_quantity_range[0], ticket_quantity_range[1] + 1, 10000),
        # Prices in VND, with 2 decimals
        'TotalPrice': [format_price(price) for price in np.random.uniform(50000, 5000000, 10000)],
        'PaymentType': np.random.choice(payment_types, 10000)
    })

    # Merging data to create full records
    sales_data = sales_data.join(customer_data.sample(
        n=10000, replace=True).reset_index(drop=True))
    sales_data = sales_data.join(event_data.sample(
        n=10000, replace=True).reset_index(drop=True))

    # Ensuring CustomerName does not repeat for the same EventName on the same date
    sales_data['SaleDate'] = sales_data['SaleDate'].dt.strftime('%d/%m/%Y')
    sales_data.drop_duplicates(
        subset=['CustomerName', 'EventName', 'SaleDate'], inplace=True)

    # Append to the main dataset
    dataset = pd.concat([dataset, sales_data], ignore_index=True)

# Save the dataset to a CSV file
dataset.to_csv(
    'C:/Users\mtbv\Documents/1.tdtu/3.da-cntt-tdtu/python-dataset-generator/gpt4-dataset-generator/sales_data.csv', index=False)

print("Dataset generation complete. File saved as 'sales_data.csv'")
