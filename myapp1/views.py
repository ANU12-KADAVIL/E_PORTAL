from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Faculty,Attendance,Leave
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def function1(request):
    return HttpResponse("<h1>SUNSHINE COLLEGE OF ENGINEERING E_PORTAL</h1>")
    


def about(request):
    return render(request,"about.html")

    
    
def course(request):
    return render(request,"course.html")
    

def frontpage(request):
    return HttpResponse("<p>Founded in 1950, St. Thomas College, Palai, has to its credit almost seventy years of distinguished service in the field of higher education in the state of Kerala sending out many graduates maxima cum laude to carve out their destinies in diverse spheres. It is a college located in a semi-urban area catering to the needs of the students mainly coming from the rural background. The idea of establishing an Arts and Science College at Palai lay dormant for a long time in the minds of the Syrian Catholic community of the area. The year 1950 was remarkable in that, true to Taine’s dictum, man, moment and milieu conspired to make history. The Diocese of Palai was born and Fr. Mani Sebastian Vayalilkalapura, president of the college committee, was made the first Bishop of the Diocese and the Patron of the college. Veteran leaders like Mr. George Thomas Kottukapally, Mr. Cherian Kappen, Mr. R.V. Thomas, Mr. K. M. Chandy et.al. joined hands with the Bishop in founding the college for fulfilling the educational dreams of the hardworking agrarian people of Meenachil.The sanction for starting the college had, in fact, been obtained from the erstwhile Travancore University two years earlier and a committee for the construction of the college building had been constituted. We were singularly fortunate in having Dr. P.J. Thomas, the renowned economist and advisor and representative of the Govt. of India to the U.N., as the first Principal of the college. Prof. V.J. Joseph, who was appointed Vice Principal, was also an academician endowed with a vision of the college growing like the mighty king of the forest, an evergreen oak with its branches reaching out far and wide. Between 1950 and 1960, apart from the intermediate course, Undergraduate courses in Mathematics, Botany, Economics, Chemistry, Zoology, Politics and Postgraduate courses in Hindi, Politics and Statistics were started. At present the college is situated in a lush green campus with a complex of ten multi-storeyed and over eight single storeyed buildings accommodating all Class Rooms, a Modern Library, University Study Centre, Modern Seminar Halls, Laboratories, Staff and Students’ Hostels, Auditoriums, Indoor Stadium, Civil Service Training Institute, IGNOU Study centre, Entrance Coaching Centres, Bank Test Coaching Centre, Career Guidance Centre, Student Amenity Centre, Fitness Centre and having over 10 acres of fields exclusively earmarked for sports and games along with a swimming pool. Besides, the college also has land earmarked for agriculture. The green campus adorned with a variety of trees and plants also adds to the glory and legacy of St. Thomas.In the year 1952, Rev. Fr. Joseph Kureethadom was appointed the Principal of the college. During his tenure the college expanded rapidly and reached its high watermark of growth with an array of undergraduate and postgraduate courses with arts and science subjects as majors, and an expansive campus conveniently and aesthetically studded with impressive college buildings, grassy playgrounds, hostels and ancillary facilities. The main block called A-block stoutly built with an enormous roof span and massive columns was ready to house the administration, classrooms, laboratories and libraries in 1953. The first Prime Minister of India, Pandit Jawaharlal Nehru, visited the college in 1954.In 1981 Rt. Rev. Dr. Joseph Pallikaparambil took over as the Bishop of Palai and the Patron of St. Thomas College. He contributed immensely for the growth of the college by giving a value system to the college. Since 2004, H.E. Bishop Mar Joseph Kallarangatt, a great visionary, scholar, theologian and an orator, has been the Bishop of Palai and the Patron of the college. The college was fortunate to have able and visionary managers such as Msgr. Emmanuel Mecherikunnel, Msgr. Philip Valiyil, Bishop Mar Joseph Pallikaparampil, Msgr. Kurian Vanchipurackal,Msgr. Joseph Mattam, Msgr. Philip Njaralakkatt, Msgr. Enas Ottathengumkal and Msgr. Joseph Kollamparampil. Under the present Manager H.E. Mar Jacob Muricken, the Auxiliary Bishop of Palai, a great visionary and a philanthropist, who has donated one of his kidneys to a deserving patient, the college is heading towards greater glories.The college celebrated its Silver Jubilee in 1976 with Prime Minister Mrs. Indira Gandhi as the chief guest. The preceding decade had been one of hectic academic activity during which more Postgraduate courses - English, Physics, Economics and Mathematics were started, new hostels inaugurated, more blocks added to the cluster of buildings in the campus etc. Rev. Dr. N.M. Thomas, who succeeded Fr. Joseph Kureethadam as Principal in 1968, retired from service in the jubilee year passing the baton to Prof. P.M. Chacko. Rev. Fr. James Vellankal followed Prof. Chacko in 1984. The successors of Fr. Vellankal included an illustrious line of academic administrators combining erudition with sharp acumen - Rev. Fr. O.P. Eanas (1986-1991), Rev. Fr. Philip Njaralakkatt (1991-1995), Rev. Dr. Kurian Mattam (1995-2001), Rev. Dr. M.M. Mathew Maleparampil (2001-2006), Rev. Dr. Mathew John Kokkatt (2006-2009), Dr. K. K. Jose (2009-2014), Rev. Fr. N.V. Joseph Njarakkattil (2014-15), Dr. Sunny Joseph (2015-2017) and Dr. Joy George (2017-2018). Rev. Dr. James John (Mangalathu) was appointed Principal in 2018 and the college is marching to greater glory under his dynamic and innovative leadership.</p>")



def frontpage(request):
    if request.method=="POST":
        std_id1=request.POST.get("std_id")
        std_name1=request.POST.get("std_name")
        mark1=request.POST.get("mark")
        attendance1=request.POST.get("attendance")
        
        n=Student(std_id=std_id1,std_name=std_name1,mark=mark1,attendance=attendance1)
        n.save()
    return render(request,'frontpage.html')

def userlogin(request):
    if request.method=="POST":
        u=request.POST.get("user_name")
        p=request.POST.get("password")
        myuser=authenticate(username=u,password=p)
        if myuser is not None:
            login(request,myuser)
            return redirect("/myapp1/forms")
        else:
            return redirect("/myapp1/login")
        

    return render(request,"login.html")


def forms(request):
    if request.method=="POST":
        std_id1=request.POST.get("std_id")
        std_name1=request.POST.get("std_name")
        attendance1=request.POST.get("attendance")
        mark1=request.POST.get("mark")
        
        n=Student(std_id=std_id1,std_name=std_name1,attendance=attendance1,mark=mark1)
        n.save()
    return render(request,'forms.html')

def userlogin1(request):
    if request.method=="POST":
        u1=request.POST.get("user_name")
        p1=request.POST.get("password")
        myuser1=authenticate(username=u1,password=p1)
        if myuser1 is not None:
            login(request,myuser1)
            return redirect("/myapp1/forms1")
        else:
            return redirect("/myapp1/login")
        

    return render(request,"login.html")



def forms1(request):
    if request.method=="POST":
        tec_id1=request.POST.get("tec_id")
        tec_name1=request.POST.get("tec_name")
        subject1=request.POST.get("subject")
        salary1=request.POST.get("salary")
        
        n1=Faculty(tec_id=tec_id1,tec_name=tec_name1,subject=subject1,salary=salary1)
        n1.save()
    return render(request,'forms1.html')

def table(request):
    b=Student.objects.all()
    return render(request,'table.html',{'e':b})

def table1(request):
    b1=Faculty.objects.all()
    return render(request,'table1.html',{'e1':b1})

def signup(request):
    if request.method=="POST":
        u1=request.POST.get("username")
        e=request.POST.get("email")
        f=request.POST.get("firstname")
        l=request.POST.get("lastname")
        p1=request.POST.get("password")
        p2=request.POST.get("conformPassword")
        
        if(p1!=p2):
            return redirect("/myapp1/signup")
        try:
            if User.objects.get(username=u1):
                return redirect("/myapp1/signup")
        except:
            pass
        x=User.objects.create_user(u1,e,p1)
        x.first_name=f
        x.last_name=l
        x.save()
        return redirect("/myapp1/login")
                
    return render(request,"signup.html")
    
def signup1(request):
    if request.method=="POST":
        u1=request.POST.get("username")
        e=request.POST.get("email")
        f=request.POST.get("firstname")
        l=request.POST.get("lastname")
        p1=request.POST.get("password")
        p2=request.POST.get("conformPassword")
        
        if(p1!=p2):
            return redirect("/myapp1/signup1")
        try:
            if User.objects.get(username=u1):
                return redirect("/myapp1/signup1")
        except:
            pass
        x=User.objects.create_user(u1,e1,p1)
        x.first_name=f
        x.last_name=l
        x.save()
        return redirect("/myapp1/login1")
                
    return render(request,"signup1.html")


def myattendance(request):
   
    if request.method=="POST":
        std_name1=request.POST.get("full_name")
        attendance1=request.POST.get("attendance")
        o=Attendance(std_name=std_name1,attendance=attendance1)
        o.save()
    return render(request,'attendance.html')


def check(request):
    m=Attendance.objects.all()
    return render(request,'check.html',{'o':m})



def deletemyorder(request,id):
    d=Attendance.objects.get(id=id)
    d.delete()
    # return redirect('/myapp3/myorder')


def myleave(request):
   
    if request.method=="POST":
        std_name1=request.POST.get("full_name")
        leave1=request.POST.get("leave")
        o=Leave(std_name=std_name1,leave=leave1)
        o.save()
    return render(request,'leave.html')

def sanction(request):
    m=Leave.objects.all()
    return render(request,'sanction.html',{'o':m})


def deleteleave(request,id):
    d=Leave.objects.get(id=id)
    d.delete()    
