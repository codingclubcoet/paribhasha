from django.shortcuts import render

# Create your views here.
from googletrans import Translator

def translation_app(request):
    if request.method == "POST":
        language = request.POST.get("language", None)
        txt = request.POST.get("text", None)

        translator = Translator()

        tr = translator.translate(txt, dest=language)
        return render(request, 'index.html', {"result":tr.text})

    return render(request, 'index.html')
