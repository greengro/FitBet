from django.contrib.auth import login
from django.shortcuts import redirect, render
from users.forms import CustomUserCreationForm


# TODO rename
def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        print('got the form')

        # TODO for some reason the form is always invalid (adding form validation feedback would help)
        if form.is_valid():
            print('the form was valid')

            user = form.save()
            login(request, user)

            # this was in the tutorial but I moved up to make sure always rendering
            # return redirect(reverse("dashboard"))

        return redirect("/dashboard")
