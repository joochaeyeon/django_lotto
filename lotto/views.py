from django.shortcuts import render
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
from django.shortcuts import render, redirect 


# Create your views here.
def index(request):

    # user_input_name = request.POST['name'] #html에서 name이 'name'인 input tag에 대해 USER가 입력한 값
    # user_input_text = request.POST['text']

    # new_row= GuessNumbers(name=user_input_name, text = user_input_text)

    # print(new_row.num_lotto) #5
    # print(new_row.name) 

    # new_row.name = new_row.upper()
    # new_row.lottos = [np.randint(1,50) for i in range(6)]

    # new_row.save() #db에 저장
 
    # return HttpResponse('<h1>Hello, world!</h1>')
    
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달 
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음 

    lottos = GuessNumbers.objects.all() 
    return render(request, 'lotto/default.html', {'lottos':lottos}) 

def hello(request):

    return HttpResponse("<h1 style='color:red;'>Hello,world!</h1>")

def post(request):

    PostForm(request.POST) 

    if form.is_valid():

        lotto = form.save(commit=False)

        print(type(lotto))
        print(lotto)
        lotto.generate()
        return redirect('index') # urls.py의 name='index'에 해당
    else:
        form = PostForm() # empty form
        return render(request, "lotto/form.html", {"form": form})
    
    
def detail(request, lottokey): 
    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key 
    return render(request, "lotto/detail.html", {"lotto": lotto}) 