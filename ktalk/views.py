from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import ThemeTest, QuestionTest, AnswerTest
# import gpt_api  # Replace this with your actual GPT API integration

from django.shortcuts import render, get_object_or_404

def index(request, theme_id=1):
    themelist = ThemeTest.objects.all().order_by('id')

    # Check if a specific theme's conversations are to be displayed
    if theme_id:
        theme = get_object_or_404(ThemeTest, id=theme_id)
        questions = QuestionTest.objects.filter(theme=theme)
        conversations = []
        for question in questions:
            try:
                answer = AnswerTest.objects.get(question=question)
                conversations.append((question, answer))
            except AnswerTest.DoesNotExist:
                continue
    else:
        theme = None
        conversations = []

    if request.method == 'POST':
        user_input = request.POST.get('message')
        theme = ThemeTest.objects.get(id=theme_id)

        # Create a new question associated with the theme
        question = QuestionTest.objects.create(theme=theme, content=user_input)

        # Get response from GPT
        gpt_response = "test answer"
        # gpt_response = gpt_api.get_response(user_input)  # Replace with actual GPT API call

        # Save the answer associated with the question
        AnswerTest.objects.create(question=question, content=gpt_response)

        return HttpResponseRedirect(f'/ktalk/init/{theme_id}')

    context = {
        'themelist': themelist,
        'theme': theme,
        'conversations': conversations,
    }

    return render(request, 'ktalk/index.html', context)

def theme(request):
    themelist = ThemeTest.objects.all().order_by('id')
    
    if request.method == 'POST':
        return HttpResponseRedirect('/ktalk/addtheme/')
    
    context = {
        'themelist' : themelist,
    }

    return render(request, 'ktalk/theme.html', context)

def add_theme(request):
    if request.method == 'POST':
        new_theme = request.POST.get('new_theme')
        if new_theme:
            ThemeTest.objects.create(name=new_theme)
    return redirect('theme')

def delete_theme(request, theme_id):
    if request.method == 'POST':
        theme = ThemeTest.objects.get(id=theme_id)
        theme.delete()
    return redirect('theme')
