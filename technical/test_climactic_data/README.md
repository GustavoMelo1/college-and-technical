#  Technical Test – Python & SQL

##  Project Structure

```
technical-test/
├── test_1/              # Logic and Loops
│   ├── ex-1.py
│   └── ex-2.py
├── test_2/              # Database
│   ├── ex-1.sql         # Extraction queries and JOINs
│   └── table.py         # Local validation script with Pandas and SQLite
└── test_3/              # API Integration
    └── alert_climates.py  # Interactive weather forecast terminal
```

---

## Getting Started

### Clone the Repository

```bash
git clone <REPOSITORY_URL>
cd technical-test
```

### Create a Virtual Environment (Venv)

It is recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
```

### Activate the Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On Linux or Mac:**
```bash
source venv/bin/activate
```

### Install Dependencies

Install the required libraries (pandas and requests):

```bash
pip install pandas requests
```

### Run the Application

To start the interactive weather terminal (Test 3), run:

```bash
python test_3/alert_climates.py
```
