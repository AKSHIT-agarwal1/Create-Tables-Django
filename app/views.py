from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from eav.models import Attribute
from app.models import Table_Manager
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    context ={}
    if request.method== 'GET':
        try:
            size  = int(request.GET.get('size',2))
        except ValueError:
            return render(request,'app/home.html')
        context["size"] = range(size)
        return render(request,'app/home.html',context)
    else:
        x=1
        for i in request.POST:
            x=x+1
        x=x-2
        context['x'] = x
        try:
            Table_Manager.objects.all().delete()
            new_entry = Table_Manager(schema=request.POST["schema"],table=request.POST["table"])
            new_entry.save()
            Attribute.objects.all().delete()
            # Attribute.objects.create(name=request.POST["schema"], datatype=Attribute.TYPE_TEXT)
            # Attribute.objects.create(name=request.POST["table"], datatype=Attribute.TYPE_TEXT)
            j=0
            y=0
            for i in request.POST:
                if y>=x-1:
                    break
                if y>=2 and y%2==0:
                    if request.POST["DataType{temp}".format(temp = str((y-2)//2))].lower() == "text":
                        Attribute.objects.create(name=request.POST["ColumnName{temp}".format(temp = str((y-2)//2))], datatype=Attribute.TYPE_TEXT)
                        j=j+1
                    elif request.POST["DataType{temp}".format(temp = str((y-2)//2))].lower() == "int":
                        Attribute.objects.create(name=request.POST["ColumnName{temp}".format(temp = str((y-2)//2))], datatype=Attribute.TYPE_INT)
                        j=j+1
                    elif request.POST["DataType{temp}".format(temp = str((y-2)//2))].lower() == "float":
                        Attribute.objects.create(name=request.POST["ColumnName{temp}".format(temp = str((y-2)//2))], datatype=Attribute.TYPE_FLOAT)
                        j=j+1
                    elif request.POST["DataType{temp}".format(temp = str((y-2)//2))].lower() == "bool":
                        Attribute.objects.create(name=request.POST["ColumnName{temp}".format(temp = str((y-2)//2))], datatype=Attribute.TYPE_BOOLEAN)
                        j=j+1
                    elif request.POST["DataType{temp}".format(temp = str((y-2)//2))].lower() == "date":
                        Attribute.objects.create(name=request.POST["ColumnName{temp}".format(temp = str((y-2)//2))], datatype=Attribute.TYPE_DATE)
                        j=j+1
                    elif request.POST["DataType{temp}".format(temp = str((y-2)//2))].lower() == "object":
                        Attribute.objects.create(name=request.POST["ColumnName{temp}".format(temp = str((y-2)//2))], datatype=Attribute.TYPE_OBJECT)
                        j=j+1
                    elif request.POST["DataType{temp}".format(temp = str((y-2)//2))].lower() == "enum":
                        Attribute.objects.create(name=request.POST["ColumnName{temp}".format(temp = str((y-2)//2))], datatype=Attribute.TYPE_ENUM)
                        j=j+1
                    else:
                        context['error'] = "Add a Valid Data Type"
                        return render(request,'app/home.html',context)
                y=y+1
        except ValidationError as e:
            context['error'] = e
            return render(request,'app/home.html',context)
        context['error'] = "Successfully"
        return render(request,'app/home.html',context)