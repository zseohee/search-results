from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import SearchResult
from ..serializers import SearchResultSerializer

class TagSearchView(APIView):
    def get(self, request, tag):
        results = SearchResult.objects.filter(tags__contains=[tag])
        serializer = SearchResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def multi_filter_search(request):
    keyword = request.GET.get("keyword", "")
    field = request.GET.get("field", "all")
    hashtags = request.GET.getlist("hashtags")
    category = request.GET.get("category")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    page = request.GET.get("page", 1)

    query = Q()

    if keyword:
        if field == "title":
            query &= Q(title__icontains=keyword)
        elif field == "summary":
            query &= Q(summary__icontains=keyword)
        elif field == "tags":
            query &= Q(tags__contains=[keyword])
        else:
            query &= (
                Q(title__icontains=keyword)
                | Q(summary__icontains=keyword)
                | Q(tags__contains=[keyword])
                | Q(state__icontains=keyword)
            )

    if hashtags:
        hashtag_query = Q()
        for tag in hashtags:
            hashtag_query |= (
                Q(title__icontains=tag)
                | Q(summary__icontains=tag)
                | Q(tags__contains=[tag])
            )
        query &= hashtag_query

    if category:
        query &= Q(category__iexact=category)

    if start_date and end_date:
        query &= Q(publish_date__range=[start_date, end_date])

    results = SearchResult.objects.filter(query).order_by("-publish_date")
    paginator = Paginator(results, 10)
    paginated_results = paginator.get_page(page)

    data = [
        {
            "title": result.title,
            "summary": result.summary,
            "source_url": result.source_url,
            "publish_date": result.publish_date.strftime("%Y-%m-%d"),
            "tags": result.tags,
            "category": result.category,
            "state": result.state,
        }
        for result in paginated_results
    ]

    return JsonResponse({"results": data, "has_next": paginated_results.has_next()})
