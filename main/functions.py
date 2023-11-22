from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def generate_form_errors(form):
    message = ""

    for field in form:
        if field.errors:
            message += f"{field.label}: {', '.join([str(error) for error in field.errors])}\n"

    for err in form.non_field_errors():
        message += str(err) + "\n"

    return message


def paginate_instances(posts, per_page=6, request=None):
    paginator = Paginator(posts, per_page)
    page = request.GET.get('page', 1) if request else 1

    try:
        instances = paginator.page(page)
    except PageNotAnInteger:
        instances = paginator.page(1)
    except EmptyPage:
        instances = paginator.page(paginator.num_pages)

    return instances