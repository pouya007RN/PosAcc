from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Device, Payment, Costs
from .forms import ClientForm, PaymentForm, SearchForm, Loginform
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate



def index(request):

    return render(request,'index.html')



@login_required
def devices(request):

    query = Device.objects.filter(count__gt=0)

    if request.method == "POST":
        search_form = SearchForm(request.POST or None)

        if search_form.is_valid():
            inp = request.POST.get('search')

            res1 = Device.objects.filter(name__icontains=inp).filter(count__gt=0)
            res2 = Device.objects.filter(app__icontains=inp).filter(count__gt=0)

            result = res1 | res2

            return render(request, 'stock.html', {'Q': result, 'form': search_form})
    else:
        search_form = SearchForm()

    return render(request,'stock.html',{'Q':query,'form':search_form})



@login_required
def order(request):

    if request.method == "POST":
        client_form = ClientForm(request.POST or None)

        if client_form.is_valid():
            device = request.POST.get('device')
            terminal = request.POST.get('terminal')
            serial_no = request.POST.get('serial_no')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            melli_id  = request.POST.get('melli_id')
            shop = request.POST.get('shop')
            phone_stat = request.POST.get('phone_stat')

            date = request.POST.get('date')

            dev = Device.objects.get(id=device)

            user_mail = Client.objects.create( name=name, device=dev,
                                               terminal=terminal, phone=phone,
                                              serial_no=serial_no,
                                               melli_id=melli_id, shop=shop,
                                                phone_stat=phone_stat, date=date)


            dev.count -= 1
            user_mail.save()
            dev.save()
            return render(request,'accepted.html')

    else:
        client_form = ClientForm()

    return render(request, 'order.html', {'Con_form':client_form})

@login_required
def client(request):

    list = Client.objects.all()

    if request.method == "POST":
        search_form = SearchForm(request.POST or None)

        if search_form.is_valid():
            inp = request.POST.get('search')

            res1 = Client.objects.filter(name__icontains=inp)
            res2 = Client.objects.filter(melli_id__icontains=inp)

            result = res1 | res2


            return render(request,'clients.html',{'clients':result,'form':search_form})
    else:
        search_form = SearchForm()

    return render(request,'clients.html',{'clients':list,'form':search_form})


@login_required
def client_detail(request,slug):

    detail = get_object_or_404(Client,id=slug)

    pay = Payment.objects.filter(client=detail)

    total = Payment.objects.filter(client=detail).aggregate(amount=Sum('amount'))

    if request.method == "POST":
        client_form = PaymentForm(request.POST or None)

        if client_form.is_valid():
            paid = request.POST.get('amount')
            date = request.POST.get('date')

            submit = Payment.objects.create(client=detail, amount=paid, date=date)
            submit.save()

            return redirect('/clients/{}'.format(slug))

    else:
        client_form = PaymentForm()

    tot = list(total.values())[0]
    if tot is None:
        tot = 0

    return render(request,'details.html',{'detail':detail,'form':client_form,'paid':pay,
                                          'total':tot})
@login_required
def cost(request):

    query = Costs.objects.all()

    total = Costs.objects.all().aggregate(Sum('amount'))

    tot = list(total.values())[0]
    if tot is None:
        tot = 0
    return render(request,'costs.html',{'cost':query,'total':tot})



@login_required
def bank(request):

    cost_q   = Costs.objects.all().aggregate(Sum('amount'))
    earned_q = Payment.objects.all().aggregate(Sum('amount'))

    cost   = list(cost_q.values())[0]
    earned = list(earned_q.values())[0]

    if cost is None:
        cost = 0
    if earned is None:
        earned = 0

    profit = int(earned) - int(cost)

    return render(request,'bank.html',{'earned':earned,'profit':profit,'cost':cost})






def loginPage(request):

    form = Loginform(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context = {'form': form,
                       'error': 'با موفقیت وارد شدید !'}

            return render(request, 'index.html', context)
        else:
            context = {'form': form,
                       'error': '!!! نام کاربری یا رمز عبور اشتباه می باشد'}

            return render(request, 'login.html', context)

    else:
        context = {'form': form}
        return render(request, 'login.html', context)




@login_required
def logout_request(request):
    logout(request)
    return redirect("/")
