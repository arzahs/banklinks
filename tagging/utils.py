from .models import Tag


def parse(text):
    tag_strings = []
    for tag in text.split():
        if tag.startswith("#"):
            tag_strings.append(tag.strip('#'))
    return tag_strings


def create(link):
    text = link.comment
    tag_strings = parse(text)
    tags_objects = []
    for tag in tag_strings:
        tags_objects.append(Tag.objects.get_or_create(user=link.user, name=tag))
    return tags_objects
