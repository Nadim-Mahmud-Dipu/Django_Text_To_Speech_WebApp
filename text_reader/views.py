from django.shortcuts import render
from .forms import TextForm
from .reader import read

# Create your views here.
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    x = re.sub(clean, '', text)
    return x.strip('&nbsp;')

def home(request):
    if request.method == 'GET':
        form = TextForm()
        context = {
            'form': form,
        }
        return render(request, 'text_reader/home.html', context)
    else:
        form = TextForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text_input']
            text = remove_html_tags(text)
        else:
            text = ""

        context = {'text': text, }
        read(text)


        return render(request, 'text_reader/audio.html', context)
