from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def removepunc(request):
    newtext = request.GET.get('textarea', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')

    result = newtext  # Start with original text

    # Remove Punctuation
    if removepunc == 'on':
        punc = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        result = "".join(char for char in result if char not in punc)

    # Remove Extra Spaces
    if extraspaceremover == 'on':
        result = " ".join(result.split())  # Splitting & joining removes extra spaces

    # Capitalize First Letter of Each Word
    if capitalize == 'on':
        result = result.title()

    # Convert to Uppercase
    if uppercase == 'on':
        result = result.upper()

    # Remove New Lines
    if newlineremover == 'on':
        result = result.replace("\n", "").replace("\r", "")

    # If no option is selected, return an error
    if newtext == result:
        return HttpResponse("<h1>Error: Please Select at Least One Option!</h1>")

    param = {'analyzed': result}
    return render(request, 'analyzed.html', param)

def favSites(request):
    return HttpResponse('''
        <a href="https://leetcode.com/studyplan/leetcode-75/"><h3>My LeetCode Profile</h3></a>
        <a href="https://github.com/Shivampanwar11"><h3>My GitHub Profile</h3></a>
    ''')
