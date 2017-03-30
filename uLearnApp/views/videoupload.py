from django.http import HttpResponseRedirect
from django.shortcuts import render
from uLearnApp.forms import uploadForm
from django.core.files.storage import FileSystemStorage

# Imaginary function to handle an uploaded file.

def videoupload(request):
    if request.method == 'POST':
        form = uploadForm(request.POST,request.FILES)
        if form.is_valid():
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return HttpResponseRedirect('/')
    else:
        form = uploadForm()
    return render(request, 'upload.html', {'form': form})
