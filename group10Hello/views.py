from django.shortcuts import render , redirect
from .models import investment
# Create your views here.
def home(request):
    return render(request, 'home.html')

def funding(request):
    if request.method == 'POST':
        membername = request.POST.get('member_name')
        membercpm = request.POST.get('member_cpm')
        investmentamount = request.POST.get('investment_amount')
        

        # Save the data to the database
        investment.objects.create(
            membername=membername,
            membercpm=membercpm,
            invetsmentamount=investmentamount,
            
        )
    
        return redirect('funding')  

    member_list=investment.objects.all()
    overall_total=sum(investment.objects.all().values_list('invetsmentamount',flat=True))

    return render(request, 'funding.html', {
        'member_list': member_list,  
        'overall_total': overall_total,
    })

def info(request, membername1):
    memberinvestment = investment.objects.filter(membername=membername1)
    membertotal = sum(investment.objects.filter(membername=membername1).values_list('invetsmentamount',flat=True))
    return render(request, 'info.html', {
        'memberinvestment': memberinvestment,
        'membertotal': membertotal
    })