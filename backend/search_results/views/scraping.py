import os
from datetime import date, datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from serpapi import GoogleSearch

from ..models import SearchResult
from .tagging import classify_category, extract_tags

load_dotenv()

@csrf_exempt
def search_google(request):
    if request.method != "GET":
        return JsonResponse({"error": "GET request required"}, status=405)

    query = request.GET.get("q")
    if not query:
        return JsonResponse({"error": "Missing query parameter"}, status=400)

    api_key = os.getenv("SERPAPI_KEY", "")
    if not api_key:
        return JsonResponse({"error": "SERPAPI_KEY is not set"}, status=500)

    params = {
        "engine": "google",
        "q": query,
        "location": "Wisconsin, United States",
        "hl": "en",
        "gl": "us",
        "api_key": api_key,
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        top_results = results.get("organic_results", [])[:5]

        if not top_results:
            return JsonResponse({"message": "No results from SerpAPI"}, status=204)

        saved = 0
        for item in top_results:
            title = item.get("title")
            link = item.get("link")
            snippet = item.get("snippet", "")
            date_str = item.get("date")

            if not title or not link:
                continue

            text = f"{title} {snippet}".lower()
            try:
                publish_date = datetime.strptime(date_str, "%b %d, %Y").date() if date_str else date.today()
            except (TypeError, ValueError):
                publish_date = date.today()

            SearchResult.objects.create(
                title=title,
                category=classify_category(text),
                state="Wisconsin",
                summary=snippet,
                source_url=link,
                publish_date=publish_date,
                tags=extract_tags(text),
            )
            saved += 1

        return JsonResponse({"message": "Scraped and Saved in DB!", "saved": saved}, status=201)
    except Exception as exc:
        return JsonResponse({"error": str(exc)}, status=500)
