from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.utils import timezone
from . models import user,admin,Contact,Quote,Job,Worker,Project,Feedback

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST ['password']
        users=user(username=username,email=email,password=password)
        users.save()
        return redirect('Naachiyar:login')
    return render(request,"login.html")

""" 
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password: 
            try:
                users = user.objects.get(email=email, password=password)
                request.session['email'] = email
                request.session.set_expiry(28800)
                return redirect('Naachiyar:home')
            except user.DoesNotExist:
                error = 'Incorrect Email/Password'
        else:
            error = 'Please provide both email and password'
        return render(request, "quote.html", {'error': error})
    else:
        if 'email' in request.session:
            return redirect('Naachiyar:home')
        else:
            return render(request, "login.html")
        
 """
def login(request):
     if request.method == 'POST':
        email = request.POST['email']
        password = request.POST ['password']
        authenticated = True 
    
        try:

            users = user.objects.get(email=email, password=password)
            
            request.session['email'] = email
            request.session.set_expiry(28800)
            
            return redirect('Naachiyar:home')  
        except user.DoesNotExist:
             error_message = 'Invalid email or password'
             return render(request, 'login.html', {'error': error_message})
     else:
        if  'email' in request.session:


            return redirect('Naachiyar:home') 
        else:
            return render(request,'login.html')
        
def alogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        authenticated = True 
    
        try:

            admins = admin.objects.get(email=email, password=password)
            
            request.session['email'] = email
            request.session.set_expiry(28800)
            
            return redirect('Naachiyar:dashboard')  
        except admin.DoesNotExist:
             error_message = 'Invalid email or password'
             return render(request, 'alogin.html', {'error': error_message})
    else:
        if  'email' in request.session:


            return redirect('Naachiyar:dashboard') 
        else:
            return render(request,'alogin.html')
def home(request):
    return render (request,"index.html")
def dashboard(request):
    """ email = request.session.get('email')
 
    if not email:
        return redirect('Naachiyar:alogin')
    else: """
    return render (request,"admin.html")
def projects(request):
    return render (request,"projects.html")
def temple(request):
    return render (request,"temple.html")
def church(request):
    return render (request,"church.html")
def mosque(request):
    return render (request,"mosqe.html")
def school(request):
    return render (request,"school.html")
def office(request):
    return render (request,"office.html")
def factory(request):
    return render (request,"factory.html")
def hospital(request):
    return render (request,"hospital.html")
def mall(request):
    return render (request,"mall.html")


def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return render(request,"index.html")
    return render(request,"contact.html")

def quote(request):

    email = request.session.get('email')
 
    if not email:
        return redirect('Naachiyar:login')
    else:

        if request.method=="POST":
            quote=Quote()
            name=request.POST.get("name")
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            description=request.POST.get("description")
            budget=request.POST.get("budget")
            s_date=request.POST.get("s_date")
            e_date=request.POST.get("e_date")
            location=request.POST.get("location")
            quote.name=name
            quote.email=email
            quote.phone=phone
            quote.description=description
            quote.budget=budget
            quote.s_date=s_date
            quote.e_date=e_date
            quote.location=location
            quote.save()
            return render(request,"index.html")
        return render(request,"quote.html")

def job(request):
    email = request.session.get('email')
 
    if not email:
        return redirect('Naachiyar:login')
    else:

        if request.method=="POST":
            job=Job()
            name=request.POST.get("name")
            age=request.POST.get("age")
            email=request.POST.get("email")
            mobile=request.POST.get("mobile")
            role=request.POST.get("role")
            experience=request.POST.get("experience")
            city=request.POST.get("city")
            pincode=request.POST.get("pincode")
            date=request.POST.get("date")
            job.name=name
            job.email=email
            job.age=age
            job.mobile=mobile
            job.role=role
            job.experience=experience
            job.city=city
            job.pincode=pincode
            job.date=date
            job.save()
            return render(request,"index.html")
        return render(request,"job.html")



def feedback(request):
    if request.method=="POST":
        feedback=Feedback()
        Name=request.POST.get("Name")
        Email=request.POST.get("Email")
        Age=request.POST.get("Age")
        Phone=request.POST.get("Phone")
        Message=request.POST.get("Message")
        Rate=request.POST.get("Rate")
        feedback.Name=Name
        feedback.Email=Email
        feedback.Age=Age
        feedback.Phone=Phone
        feedback.Message=Message
        feedback.Rate=Rate
        feedback.save()
        return render(request,"index.html")
    return render(request,"feedback.html")



from django.shortcuts import render, redirect,get_object_or_404
from .models import Worker,Project
from django.contrib import messages

def show_workers(request):
    workers = Worker.objects.all()
    return render(request, "workers.html", {'workers': workers})

def add_worker(request):
    if request.method == "POST":
        worker = Worker()

        name = request.POST.get("name")
        age = request.POST.get("age")
        contact = request.POST.get("contact")
        designation = request.POST.get("designation")

        
        worker = Worker(name=name, age=age, contact=contact, designation=designation)
        worker.save()
        
        workers = Worker.objects.all()
        return render(request, "workers.html", {'workers': workers})
    
    return render(request, "workers.html")

def project_list(request):
    """ email = request.session.get('email')
    print(email)
    if not email:
        return redirect('Naachiyar:alogin') #return render(request, 'admin_panel.html', {'email': email})
    else: """
    if request.method == 'POST':
        project_name = request.POST.get("pname")
        client_name = request.POST.get("cname")
        mobile = request.POST.get("contact")
        location = request.POST.get("location")
        budget = request.POST.get("budget")
        s_date = request.POST.get("sdate")
        status = request.POST.get("status")
        e_date = request.POST.get("edate")

        Project.objects.create(
            project_name=project_name,
            client_name=client_name, 
            mobile=mobile, 
            location=location, 
            budget=budget, 
            s_date=s_date, 
            status=status, 
            e_date=e_date
        )
        return redirect('Naachiyar:project_list')
    
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

def update_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':
        project_name = request.POST.get("pname")
        client_name = request.POST.get("cname")
        mobile = request.POST.get("contact")
        location = request.POST.get("location")
        budget = request.POST.get("budget")
        s_date = request.POST.get("sdate")
        status = request.POST.get("status")
        e_date = request.POST.get("edate")

        # Update project fields
        project.project_name = project_name
        project.client_name = client_name
        project.mobile = mobile
        project.location = location
        project.budget = budget
        project.s_date = s_date
        project.status = status
        project.e_date = e_date

        # Save the updated project
        project.save()

        messages.success(request, 'Project updated successfully.')
        return redirect('Naachiyar:project_list')

    # Pass the project instance to the template
    return render(request, 'project.html', {'project': project})

def delete_project(request,id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('Naachiyar:project_list')

""" def show_project(request):
    project = Project.objects.all()
    return render(request, "project.html", {'project': project})

def delete_project (request , id):
    project=Project.objects.get(id=id)
    project.delete()
    return redirect(request,"/show_project")



def add_project(request):
    if request.method == "POST":
        project = Project()
        project_name = request.POST.get("pname")
        client_name = request.POST.get("cname")
        contact = request.POST.get("contact")
        location = request.POST.get("location")
        budget = request.POST.get("budget")
        sdate = request.POST.get("sdate")
        status = request.POST.get("status")
        edate = request.POST.get("edate")
        print(project_name,client_name,contact)
        project = Project(project_name=project_name, client_name=client_name, contact=contact, location=location, budget=budget, sdate=sdate, status=status, edate=edate)
        project.save()
        
        project = Project.objects.all()
        return render(request, "project.html", {'project': project})
    print("page load")
    return render(request, "project.html")
 """



def Feedback_show(request):
    feedback= Feedback.objects.all()
    return render(request, "adminfeedback.html", {'feedback': feedback})

def Quote_show(request):
    quote= Quote.objects.all()
    return render(request, "adminquote.html", {'quote': quote})

def hiering(request):
    job= Job.objects.all()
    return render(request, "hiering.html", {'job': job})

""" def employee_list(request):
    employees = Employee.objects.all()
    
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        attendance_status = request.POST.get('attendance_status')
        employee = Employee.objects.get(id=employee_id)
        Attendance.objects.create(employee=employee, date=timezone.now().date(), status=attendance_status)
        return redirect('employee_list')
    
    return render(request, 'attendance.html', {'employees': employees})
 """
def footer(request):
    return render(request,'footer.html')