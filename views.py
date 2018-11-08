from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Authors, Users, ReadBooks
from app1.generaterecs import doshit
from itertools import chain
from django.db import connection, transaction
cursor = connection.cursor()
globaluser = None
viewbook = None

# Create your views here.

def search(request):
    if request.method == 'POST':
        book_name =  request.POST.get('search')
        book = Books.objects.filter(title__icontains=book_name)
        author = Authors.objects.filter(a_name__icontains=book_name)
        return render(request,"mysite3/search.html",{'data':book,'data2':author})
    if request.method == 'GET':
        return render(request,'mysite3/recs.html',{})

def index(request):
    return render(request,'mysite3/login.html')
	
def sign_up(request):
    if request.method == 'POST':
        uname =  request.POST.get('username')
        upwd =  request.POST.get('password')
        upwdag =  request.POST.get('passwordagain')
        if upwd == upwdag and not Users.objects.filter( u_name = uname ).exists():
            data = Users(u_name=uname,pwd=upwd)
            data.save()
            return render(request,"mysite3/login.html",{})
        else :
            return render(request,'mysite3/sign_up.html',{})
    if request.method == 'GET':
        return render(request,'mysite3/sign_up.html',{})
		
def l_recs(request):
    if request.method == 'POST':
        uname =  request.POST.get('username')
        upwd =  request.POST.get('password')
        tuname = Users.objects.raw('SELECT * from Users')
        for i in tuname:
            if Users.objects.filter( u_name = uname, pwd = upwd ).exists() :
                global globaluser
                globaluser = uname
                data  = Books.objects.raw('SELECT * from Books')
                return render(request,'mysite3/recs.html',{'data':data})
        return render(request,'mysite3/login_again.html')
    if request.method == 'GET':
        return render(request,'mysite3/login.html',{})
	
def recs(request):
    titles = []
    global globaluser
    cursor.execute('SELECT title FROM Books')
    #cursor.execute('SELECT b.title FROM Books b, Read_Books r WHERE b.b_id=r.b_id AND r.u_id in (SELECT u.u_id FROM Users u WHERE u.u_name=%s) AND r.rating>2.99',[globaluser])
    titles = cursor.fetchall()
    flag = doshit(titles)
    if flag == True:
        return render(request,'mysite3/discover.html')#recs = Books.objects.raw('SELECT * FROM Recs r, Books b WHERE r.title=b.title order by r.title')
    else:
        return render(request,'mysite3/contact.html')#recs = Books.objects.raw('SELECT * FROM Books WHERE avg_rat>4 order by title')
    return render(request,'mysite3/recs.html',{'data':recs})
	
def discover(request):
    data = Books.objects.raw('SELECT * FROM Books order by avg_rat desc');
    return render(request,'mysite3/discover.html',{'data':data})
	
def about(request):
    return render(request,'mysite3/about.html')
	
def contact(request):
    return render(request,'mysite3/contact.html')
	
def ftgenres(request):
    return render(request,'mysite3/first_time_genres.html')
	
def genres(request):
    return render(request,'mysite3/genres.html')

def categories(request):
    return render(request,'mysite3/categories.html')
	
#categories
def youngadult(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE cat="Young Adult" order by title');
    return render(request,'mysite3/category_s/youngadult.html',{'yadata':yadata})
	
def kids(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE cat="Kids" order by title');
    return render(request,'mysite3/category_s/kids.html',{'yadata':yadata})
	
def newadult(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE cat="New Adult" order by title');
    return render(request,'mysite3/category_s/newadult.html',{'yadata':yadata})
	
def adult(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE cat="Adult" order by title');
    return render(request,'mysite3/category_s/adult.html',{'yadata':yadata})

#genres	
def contemporary(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="Contemporary" order by title');
    return render(request,'mysite3/genre_s/contemporary.html',{'data':data})
	
def mysteryandcrime(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="mystery & crime" order by title');
    return render(request,'mysite3/genre_s/mysteryandcrime.html',{'data':data})
	
def thriller(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="thriller" order by title');
    return render(request,'mysite3/genre_s/thriller.html',{'data':data})

def sciencefiction(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="science fiction" order by title');
    return render(request,'mysite3/genre_s/sciencefiction.html',{'data':data})
	
def humour(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="humour" order by title');
    return render(request,'mysite3/genre_s/humour.html',{'data':data})
	
def fantasy(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="fantasy" order by title');
    return render(request,'mysite3/genre_s/fantasy.html',{'data':data})
	
def romance(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="romance" order by title');
    return render(request,'mysite3/genre_s/romance.html',{'data':data})
	
def chicklit(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="chick lit" order by title');
    return render(request,'mysite3/genre_s/chicklit.html',{'data':data})
	
def dystopia(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="dystopia" order by title');
    return render(request,'mysite3/genre_s/dystopia.html',{'data':data})
	
def nonfiction(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="non fiction" order by title');
    return render(request,'mysite3/genre_s/nonfiction.html',{'data':data})
	
def horror(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="horror" order by title');
    return render(request,'mysite3/genre_s/horror.html',{'data':data})
	
def textbooks(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="textbooks" order by title');
    return render(request,'mysite3/genre_s/textbooks.html',{'data':data})
	
def poetry(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="poetry" order by title');
    return render(request,'mysite3/genre_s/poetry.html',{'data':data})
	
def comics(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="comics" order by title');
    return render(request,'mysite3/genre_s/comics.html',{'data':data})
	
#books
def book(request, *args, **kwargs):
    global viewbook
    viewbook = kwargs['bookname']
    global globaluser
    if ReadBooks.objects.filter( b_id = viewbook ).exists() and Users.objects.filter( u_name = globaluser ).exists() :
        data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS natural join Read_Books WHERE b_id=%s',[viewbook]);
        return render(request,'mysite3/book2.html',{'data':data})
    else :
        data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE b_id=%s',[viewbook]);
        return render(request,'mysite3/book.html',{'data':data})
	
def book2(request):
    if request.method == 'POST':
        rat =  request.POST.get('rating')
        global viewbook
        global globaluser
        cursor.execute('INSERT INTO Read_Books values(%s,(SELECT u_id FROM Users WHERE u_name=%s),%s)',[viewbook,globaluser,rat])
        data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS natural join Read_Books WHERE b_id=%s',[viewbook]);
        return render(request,'mysite3/book2.html',{'data':data})
    if request.method == 'GET':
        return render(request,'mysite3/book.html',{})