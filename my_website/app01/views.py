from django.shortcuts import render, HttpResponse
# import pymysql
# Create your views here.

def test_view(request):
    # You have to put the request in the ()
    print("Execute.")

    return HttpResponse("<h1 style='color:red'> My salary goal is $50/per hour!</h1>")

def login_view(request):
    # check settings-> template
    # html = """
    #     <form method="post">
    #
    #         <input type="text" name="username">
    #         <input type="text" name="password">
    #
    #         <input type="submit" value="Login">
    #     </form>
    # """
    # return HttpResponse(html)

    # render() is to call the other file, before run this step, make the form.html file
    print(request.GET,request.POST)   # get the info from from.html and when the method is GET
    print(request.FILES)
    return render(request, 'form.html')

def article_year(request,year, version):
    return HttpResponse("article archive %s %s" % (year, version))

def article_2021(requetst):
    return HttpResponse("This is article 2021")

def article_archive(request,year,month):
    return HttpResponse("article archive %s -%s" % (year,month))

def article_str(request, name):
    return HttpResponse("The name is : " +name)

def article_archive3(request, arg1, arg2, slug):
    return HttpResponse("article archive3 %s - %s %s" % (arg1, arg2, slug))

def download_file(request):
    f = open("static_data/cell_errors.xlsx","rb")
    response = HttpResponse(f.read(), content_type="application/vnd.ms_excel", )
    response['Content-Disposition'] = 'attachment; filename="cell_errors.xlsx"'
    return response