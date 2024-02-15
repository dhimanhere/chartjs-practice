import json
from myapp.models import myModel
from django.utils.dateparse import parse_datetime
from datetime import datetime

def parse_datetime_custom(date_string):
    try:
        return datetime.strptime(date_string, '%B, %d %Y %H:%M:%S')
    except ValueError:
        return None

def populate_database(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Bulk create instances to minimize database queries
    instances_to_create = []
    for item in data:
        instance = myModel(
            end_year=int(item.get('end_year')) if item.get('end_year') is not None and item.get('end_year') != '' else None,
            intensity=item.get('intensity') if item.get('intensity') is not None and item.get('intensity') != '' else None,
            sector=item.get('sector') if item.get('sector') is not None and item.get('sector') != '' else None,
            topic=item.get('topic') if item.get('topic') is not None and item.get('topic') != '' else None,
            insight=item.get('insight') if item.get('insight') is not None and item.get('insight') != '' else None,
            url=item.get('url') if item.get('url') is not None and item.get('url') != '' else None,
            region=item.get('region') if item.get('region') is not None and item.get('region') != '' else None,
            start_year=int(item.get('start_year')) if item.get('start_year') is not None and item.get('start_year') != '' else None,
            impact=item.get('impact') if item.get('impact') is not None and item.get('impact') != '' else None,
            added=parse_datetime_custom(item.get('added', '')) if item.get('added') is not None and item.get('added') != '' else None,
            published=parse_datetime_custom(item.get('published', '')) if item.get('published') is not None and item.get('published') != '' else None,
            country=item.get('country') if item.get('country') is not None and item.get('country') != '' else None,
            relevance=item.get('relevance') if item.get('relevance') is not None and item.get('relevance') != '' else None,
            pestle=item.get('pestle') if item.get('pestle') is not None and item.get('pestle') != '' else None,
            source=item.get('source') if item.get('source') is not None and item.get('source') != '' else None,
            title=item.get('title') if item.get('title') is not None and item.get('title') != '' else None,
            likelihood=item.get('likelihood') if item.get('likelihood') is not None and item.get('likelihood') != '' else None,
        )
        instances_to_create.append(instance)

    myModel.objects.bulk_create(instances_to_create)

# call it where required