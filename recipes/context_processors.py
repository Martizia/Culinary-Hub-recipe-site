from django.db.models import Count
from .models import Tag


def tag_cloud(request):
    tags = Tag.objects.annotate(num_times=Count("recipes")).order_by("name")

    min_count = min(tag.num_times for tag in tags) if tags else 0
    max_count = max(tag.num_times for tag in tags) if tags else 0
    range_count = max_count - min_count

    for tag in tags:
        if range_count == 0:
            tag.size = 1
        else:
            tag.size = ((tag.num_times - min_count) / range_count) * 2 + 1  # sizes 1-3

    return {"tags": tags}
