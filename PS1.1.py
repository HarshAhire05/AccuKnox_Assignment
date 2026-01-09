import requests
import matplotlib.pyplot as plt
import pandas as pd

API_URL = "https://api.mockaroo.com/api/generate.json?key=hidden_key&schema=student_scores" # Placeholder
FALLBACK_DATA = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95},
    {"name": "Diana", "score": 81},
    {"name": "Ethan", "score": 68},
    {"name": "Fiona", "score": 91},
    {"name": "George", "score": 77}
]

def fetch_data(url):
    print("[-] Attempting to fetch data from API...")
    try:
        raise requests.exceptions.ConnectionError("Demo API not reachable")
        
    except requests.exceptions.RequestException as e:
        print(f"[!] API connection failed ({e}).")
        print("[-] Switching to local fallback data so you can see the graph.")
        return FALLBACK_DATA

def process_data(data):
    df = pd.DataFrame(data)
    average_score = df['score'].mean()
    print(f"\n--- Data Analysis ---")
    print(f"Number of Students: {len(df)}")
    print(f"Average Score: {average_score:.2f}")
    return df, average_score

def visualize_data(df, average):
    print("[-] Generating visualization...")
    plt.figure(figsize=(10, 6))
    colors = ['#4CAF50' if x >= average else '#FF5733' for x in df['score']]
    bars = plt.bar(df['name'], df['score'], color=colors)
    plt.axhline(y=average, color='blue', linestyle='--', linewidth=2, label=f'Average ({average:.1f})')
    
    plt.title('Student Test Scores', fontsize=16)
    plt.xlabel('Student Name', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.ylim(0, 100) 

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height}',
                 ha='center', va='bottom')

    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    student_data = fetch_data(API_URL)
    
    if student_data:
        df_students, avg_score = process_data(student_data)
        
        visualize_data(df_students, avg_score)
    else:
        print("[!] No data available to process.")