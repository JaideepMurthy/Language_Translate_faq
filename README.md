# README.md

## Installation Steps
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## API Usage Examples
- Fetch FAQs in English (default): `curl http://localhost:8000/api/faqs/`
- Fetch FAQs in Hindi: `curl http://localhost:8000/api/faqs/?lang=hi`
- Fetch FAQs in Bengali: `curl http://localhost:8000/api/faqs/?lang=bn`

## Contribution Guidelines
- Follow PEP8 guidelines.
- Use conventional commit messages.
- Ensure tests pass before submitting a PR.