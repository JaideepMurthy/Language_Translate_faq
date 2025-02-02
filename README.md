# README.md

## Installation Steps
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## API Usage
- Fetch FAQs in English (default): `curl http://localhost:8000/api/faqs/`
- Fetch FAQs in Hindi: `curl http://localhost:8000/api/faqs/?lang=hi`
- Fetch FAQs in Bengali: `curl http://localhost:8000/api/faqs/?lang=bn`

## Features
- Follow PEP8 guidelines.
- Use conventional commit messages.
- Ensure tests pass before submitting a PR.

## Installation Steps
1. Clone the Repository:

`git clone <repository_url>`
`cd Language_Translate_faq`

2. Create and Activate Virtual Environment:

 `python -m venv venv`

 On Windows: `.\venv\Scripts\activate`
 On macOS/Linux: `source venv/bin/activate`

3. Install Dependencies: `pip install -r requirements.txt`

4. Run Migrations:

`python manage.py makemigrations`
`python manage.py migrate`

5. Create Superuser: `python manage.py createsuperuser`

6. Start the Server: `python manage.py runserver`


## API Usage Examples
 Fetch FAQs in English (default): `curl http://localhost:8000/api/faqs/`

 Fetch FAQs in Hindi: `curl http://localhost:8000/api/faqs/?lang=hi`

 Fetch FAQs in Bengali: `curl http://localhost:8000/api/faqs/?lang=bn`

### Contribution Guidelines
In my project, I ensured that all contributions adhered to best practices and coding standards:

I followed PEP8 guidelines to maintain clean and readable code. I used tools like flake8 to check for style violations and ensure consistency.

I followed conventional commit messages to keep version control organized and meaningful:

`git commit -m "feat: Add multilingual FAQ model"`
`git commit -m "fix: Improve translation caching"`
`git commit -m "docs: Update README with API examples"`

I wrote unit tests using pytest to validate functionality and maintain reliability. Before every commit or pull request, I ensured that all tests passed successfully:

`pytest`

By following these practices, I maintained high code quality, clarity, and efficiency throughout the project.

## Docker Support 
1. Build and Run Docker Containers:
docker-compose up --build

2. Access the Application: Open your web browser and go to http://127.0.0.1:8000 to access your Django application.