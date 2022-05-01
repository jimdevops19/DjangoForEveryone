from django.shortcuts import render, redirect

# Create your views here.
def redirect_home_page(request):
    return redirect('home_page')

def home_page(request):
    data = [
        {
            "id" : 1,
            "name" : "Update Software",
            "progress_pct" : 100
        },
        {
            "id": 2,
            "name": "Deploy the Website",
            "progress_pct": 80
        }
    ]
    return render(
        request,
        template_name='main/home.html',
        context={"data" : data}
    )

def done_tasks_page(request):
    done_tasks_data = [
        {
            "id" : 3,
            "name" : "Complete Youtube Video",
            "progress_pct" : 100
        },
        {
            "id": 4,
            "name": "Write 2 hours of Python Code",
            "progress_pct": 100
        }
    ]
    return render(
        request,
        template_name="main/done_tasks.html",
        context={"done_tasks_data" : done_tasks_data}
    )