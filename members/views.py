from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member

def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member-success")
    else:
        form = MemberForm()
    return render(request, "members/member_form.html", {"form": form})

def member_success(request):
    return render(request, "members/member_success.html")

def member_list(request):
    members = Member.objects.order_by('-joined_date')
    return render(request, "members/member_list.html", {"members": members})