from django.shortcuts import redirect, render

def root(request):
    return render(request, "index.html")

def result(request):
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    radio_btn_from_form = request.POST['radio_btn']
    drop_down_from_form = request.POST['drop_down_selection']
    comment_from_form = request.POST['comment_section']
    context = {
        "name_from_template": name_from_form,
        "email_from_template": email_from_form,
        "radio_btn_from_template": radio_btn_from_form,
        "drop_down_selection": drop_down_from_form,
        "comment_section": comment_from_form
    }
    return render(request, "result.html", context)


