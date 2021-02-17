from django.shortcuts import redirect, render

def root(request):
    return render(request, "index.html")

def survey_complete(request):
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_from_template": name_from_form,
        "email_from_template": email_from_form
    }
    return redirect("/result")

def result(request):
    return render(request, "result.html")


