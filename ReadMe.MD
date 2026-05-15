# UK Companies Explorer

This is a small Flask web application that lets you browse a sample of UK companies
from the Companies House open data. It uses two linked tables:

- `Status` – the type of company status (e.g. Active, Dissolved)
- `Company` – basic company information linked to a status

The app is meant as a simple database-driven site for learning Flask, SQLAlchemy,
and basic testing.

## Features

- Browse a list of companies with pagination
- View detailed information for individual companies
- Explore company statuses
- Responsive web interface using HTML templates

## Open Data Source

The data comes from the UK Companies House open data:

- Companies House basic company data (CSV)
- Download page: https://download.companieshouse.gov.uk/en_output.html

I created a smaller CSV sample (around 5000–7000 rows) from the original file and
stored it in `data/companies_sample.csv`. I also created a small `statuses.csv`
file listing the different status names.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Simisolaoluuk/advanced_programming_assignment2.git
   cd advanced_programming_assignment2
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Load the data into the database:

   ```bash
   python load_data.py
   ```

   This will create a SQLite database file (`companies.db`) in the `instance/` directory and populate it with the sample data.

## Running the Application

To run the application locally:

```bash
python app.py
```

The application will be available at `http://localhost:5000`.

## Project Structure

- `app.py` – Main Flask application and routes
- `models.py` – SQLAlchemy models for `Status` and `Company`
- `load_data.py` – Script to load CSV data into the SQLite database
- `templates/` – HTML templates (no JavaScript)
  - `base.html` – Base template
  - `index.html` – Home page
  - `companies.html` – Companies list page
  - `company_detail.html` – Individual company details
  - `statuses.html` – Statuses list page
  - `error.html` – Error pages
- `data/` – CSV files for companies and statuses
  - `companies_sample.csv` – Sample company data
  - `statuses.csv` – Company status types
- `instance/` – Directory for SQLite database file
- `tests/` – Basic tests using pytest
  - `test_basic.py` – Test cases for routes and basic functionality
- `requirements.txt` – Python dependencies
- `ReadMe.MD` – This file

## Testing

To run the tests:

```bash
pytest
```

## Deployment

This application was deployed to Render (https://simisola-olu-uk-companies-explorer-site.onrender.com). 

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- UK Companies House for providing the open data
- Flask and SQLAlchemy communities for excellent documentation and tools
