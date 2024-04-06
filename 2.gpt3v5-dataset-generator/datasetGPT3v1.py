import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Set the seed for reproducibility
random.seed(42)

# Initialize Faker for generating fake names
fake = Faker()

# Function to generate random dates within the specified range


def generate_random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Function to generate a random amount in a given range with two decimal places


def generate_random_amount(start, end):
    return round(random.uniform(start, end), 2)


# Set the date range
start_date = datetime(2020, 1, 1)
end_date = datetime(2022, 12, 30)

# Number of rows to generate
num_rows = 1000000

# Dictionary to track CustomerName to CustomerID mapping
customer_mapping = {}

# Dictionary to track EventName to EventID mapping
event_mapping = {}

# Initialize dictionaries to track used CustomerNames and dates
used_customer_names = {}
used_dates = {}

# List of CustomerNames and EventNames
customer_names = [fake.name() for _ in range(10000)]

# event_names = [fake.company() for _ in range(10)]
event_names = [
    "Tech Summit 2023", "Innovation Expo", "CodeCrafters Hackathon", "Future Trends Symposium",
    "Data Science Showcase", "Digital Marketing Forum", "Robotics Revolution", "Blockchain Bonanza", "AI Wonderland", "Space Exploration Expo",
    "HealthTech Symposium", "Eco-Friendly Innovations", "Virtual Reality Festival", "Cybersecurity Summit", "Game Developers Conference",
    "Startup Ignition", "Women in Tech Symposium", "FinTech Frontier", "Smart Cities Expo", "Global Hackfest", "Digital Arts Festival",
    "Quantum Computing Symposium", "Big Data Bash", "Wearable Tech Showcase", "Cloud Computing Carnival", "Genomics Gala",
    "Social Media Mastery", "Autonomous Vehicles Expo", "AR/VR Experience", "BioTech Breakthroughs", "Future of Work Conference",
    "Sustainable Energy Summit", "EdTech Extravaganza", "Agile Development Sprint",
    "SpaceX Launch Celebration", "Open Source Odyssey", "Gaming Galaxy",
    "Tech for Good Summit", "DevOps Days",
    "Internet of Things Expo",
    "Healthcare Hackathon",
    "Digital Transformation Forum",
    "Quantified Self Conference",
    "Cryptocurrency Carnival",
    "Mobile App Marathon",
    "Cyberpunk Coding Challenge",
    "Drones & Robotics Expo",
    "UX/UI Design Summit",
    "Data Privacy Symposium",
    "E-commerce Evolution",
    "Biohacking Bonanza",
    "Smart Agriculture Showcase",
    "Tech Talent Expo",
    "Cloud Security Congress",
    "Virtual Classroom Revolution",
    "Space Tourism Symposium",
    "Blockchain Revolution",
    "Tech Diversity & Inclusion Summit",
    "Human-Computer Interaction Expo",
    "Innovative Retail Solutions",
    "Health and Wellness Tech Fair",
    "Digital Accessibility Symposium",
    "Renewable Energy Expo",
    "Mobile Payments Summit",
    "Augmented Reality Adventure",
    "Data Ethics Symposium",
    "Future of Transportation Expo",
    "Gaming for Good Marathon",
    "Social Impact Tech Forum",
    "Neurotech Nexus",
    "Code for Climate Hackathon",
    "Industry 4.0 Expo",
    "VR for Education Symposium",
    "The Quantum Leap",
    "Space Colonization Conference",
    "Inclusive Design Showcase",
    "Blockchain for Social Impact",
    "Tech for Sustainable Cities",
    "Future of Retail Summit",
    "Human Augmentation Expo",
    "Digital Citizenship Symposium",
    "AI for Good Forum",
    "Zero Waste Tech Expo",
    "Smart Home Innovations",
    "AR in Healthcare Symposium",
    "Tech Ethics Roundtable",
    "Data for Democracy Hackathon",
    "Future of Finance Forum",
    "Voice Technology Showcase",
    "Space Innovation Challenge",
    "Green Tech Revolution",
    "Digital Inclusion Summit",
    "Gen Z Tech Festival",
    "Bioinformatics Bash",
    "Blockchain for Healthcare",
    "Tech for Mental Health Symposium",
    "Digital Nomad Expo",
    "Future of Food Tech",
    "Code for Equality Hackathon",
    "Quantum Networking Symposium",
]

# Initialize CSV data
data = []

# Generate CSV data
for _ in range(num_rows):
    customer_name = random.choice(customer_names)

    # Ensure each CustomerName is mapped to a unique CustomerID
    if customer_name not in customer_mapping:
        customer_mapping[customer_name] = fake.uuid4()

    # customer_id = customer_mapping[customer_name]
    customer_id = 'C' + \
        str(customer_mapping[customer_name]).replace('-', '')[:7].rjust(7, '0')

    sale_date = generate_random_date(start_date, end_date).strftime('%d/%m/%Y')

    event_name = random.choice(event_names)

    # Ensure each EventName is mapped to a unique EventID
    if event_name not in event_mapping:
        event_mapping[event_name] = fake.uuid4()

    event_id = event_mapping[event_name]
    event_id = 'E' + \
        str(event_mapping[event_name]).replace('-', '')[:7].rjust(7, '0')

    ticket_quantity_per_event = random.randint(1, 10)

    # Generate TotalPrice in Vietnamese Dong (VND)
    # total_price_vnd = round(generate_random_amount(10000, 1000000))
    total_price_vnd = '{:,.0f}'.format(
        round(generate_random_amount(100000, 5000000)))
    # Adjust the range as needed

    payment_type = random.choice(['Cash', 'Transaction'])

    # Append data to the list
    data.append([customer_name, customer_id, sale_date, event_name,
                event_id, ticket_quantity_per_event, total_price_vnd, payment_type])

# Specify the CSV file path
csv_file_path = r'C:\Users\mtbv\Documents\1.tdtu\3.da-cntt\python-dataset\online_ticket_sales.csv'

# Write data to CSV file
with open(csv_file_path, 'w', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header
    csv_writer.writerow(['CustomerName', 'CustomerID', 'SaleDate', 'EventName',
                        'EventID', 'TicketQuantyPerEvent', 'TotalPrice', 'PaymentType'])

    # Write data rows
    csv_writer.writerows(data)

print(f"CSV file has been generated at: {csv_file_path}")
