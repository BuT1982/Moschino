from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/recent.html')
def recent(cnt=3):
    posts = Post.objects.order_by('-created_at')[:cnt]
    return {'posts': posts}
