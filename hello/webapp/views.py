from django.shortcuts import render


class ErrorValueRange(Exception):
    pass


class ErrorValueSet(Exception):
    pass


class ErrorValueDeficiency(Exception):
    pass


# Create your views here.
NUMBERS1 = []
TOTAL = 0


def check1(num):
    values = num.split()
    check2 = []
    for i in values:
        i = int(i)
        check2.append(i)
    return check2


def check2(num):
    for ii in num:
        if ii not in range(1, 9 + 1):
            raise ErrorValueRange()
        return ii


def index_view(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        try:
            num = request.POST.get('number')
            secret_numbers = [5, 1, 2, 9]
            checker = check1(num)
            check2(checker)
        except ValueError:
            checker = "Error value not int"
        except ErrorValueRange:
            checker = "Error value not range 1,9"
