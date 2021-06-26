from collections import defaultdict
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Field

dates = list()

from .data import read


def index(request):
    if not dates:
        for field in Field.objects.all():
            if field.consult_date not in dates:
                dates.append(field.consult_date)

            dates.sort(reverse=True)

    return render(request, "index.html", {"dates": dates})


def dump(request):
    read.insert()
    return HttpResponse("Banco de dados preenchido.")


def ajax(request):
    all_data = defaultdict(list)

    for field in Field.objects.all():
        list_ = all_data[field.product_url]

        if not list_:
            list_ += [field.product_url,
                      field.product_created_at.date(),
                      field.count]

            for _ in dates:
                list_.append(0)  # contador para a data
        else:
            list_[2] += field.count

            index = dates.index(field.consult_date)
            index += 3
            list_[index] += field.count

    all_data = list(all_data.values())

    column = int(request.GET.get("order[0][column]", 0))
    reverse = request.GET.get("order[0][dir]") == "desc"

    search = request.GET.get("search[value]", None)
    if search:
        all_data = filter(lambda i: search in ''.join(map(str, i)), all_data)

    all_data = sorted(all_data, reverse=reverse, key=lambda i: i[column])

    start = int(request.GET.get("start", 0))
    length = int(request.GET.get("length", 10))

    data = all_data[start:start+length]

    return JsonResponse({
        "draw": int(request.GET.get("draw", 1)),

        "recordsFiltered": len(all_data),
        "recordsTotal": len(all_data),
        "data": data,
    })
