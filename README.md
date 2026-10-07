# search-results

A backend that takes a query, fetches Google results, attaches tags and a category, stores them in Postgres, and looks them up again by filter.

## Data

Table `search_results_searchresult`

| Column | Meaning |
|---|---|
| title | Search result title |
| category | `job`, `event`, `welfare`, `other` |
| state | `Wisconsin` at collection time |
| summary | Search snippet |
| source_url | Original link. Duplicate links are stored again |
| publish_date | Result date. The collection date is used when parsing fails |
| tags | Keyword array (jsonb) |

## API

- `GET /api/search-google/?q=` — collect the top 5 results and save them. Requires `SERPAPI_KEY`
- `GET /api/search/?keyword=&field=&hashtags=&category=&start_date=&end_date=&page=` — filter. 10 results per page, newest first
- `GET /api/search/<tag>/` — rows whose `tags` contain that tag

`field` is `title`, `summary`, `tags`, or `all`. A date range applies only when both the start and the end are given.

## Local setup

Postgres 15 is already running on this Mac on port 5432. The database name is `search_results`.

```bash
cp .env.example .env
cd backend
python3.12 -m venv ../.venv
source ../.venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The admin site is `/admin/`. If there is no account yet, run `python manage.py createsuperuser`.

For Docker, run `docker compose up --build` from the project root. Inside the container the database host is `db`, and the host port is `15432`.
