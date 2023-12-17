from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .newgpt import ChatSession

from django.shortcuts import render, get_object_or_404

def index(request, theme_id=None):
    themelist = ThemeTest.objects.all().order_by('id')
    theme = None
    conversations = []

    if theme_id:
        theme = get_object_or_404(ThemeTest, id=theme_id)
        conversation_objects = ConversationTest.objects.filter(theme=theme).order_by('id')

        # Process conversation_objects to pair questions with answers
        temp_conversations = []
        for conversation in conversation_objects:
            if conversation.role == 'user':
                temp_conversations.append((conversation, None))  # Add user question with a placeholder for the answer
            elif conversation.role == 'assistant' and temp_conversations:
                # Assuming each user input is followed by an assistant response
                last_conversation = temp_conversations[-1]
                if last_conversation[1] is None:  # If the last item has no answer
                    temp_conversations[-1] = (last_conversation[0], conversation)  # Pair the last question with this answer

        conversations = [conv for conv in temp_conversations if conv[1] is not None]  # Filter out unanswered questions

    if request.method == 'POST':
        user_input = request.POST.get('message')
        chat_session = ChatSession(theme_id=theme_id)
        chat_session.store_message('user', user_input)
        gpt_response = chat_session.get_response(user_input)
        conversations.append((user_input, gpt_response))
        return HttpResponseRedirect(f'/ktalk/init/{theme_id}' if theme_id else '/ktalk/init/')

    context = {
        'themelist': themelist,
        'theme': theme,
        'conversations': conversations,
    }

    return render(request, 'ktalk/new_index.html', context)



def theme(request):
    themelist = ThemeTest.objects.all().order_by('id')
    
    if request.method == 'POST':
        return HttpResponseRedirect('/ktalk/add_theme/')
    
    context = {
        'themelist' : themelist,
    }

    return render(request, 'ktalk/theme.html', context)

def add_theme(request):
    if request.method == 'POST':
        new_theme = request.POST.get('new_theme')
        new_assistant_role = request.POST.get('new_assistant_role', '')  # Default to empty string if not provided
        if new_theme:
            ThemeTest.objects.create(name=new_theme, assistantrole=new_assistant_role)
    return redirect('ktalk:theme')


def delete_theme(request, theme_id):
    if request.method == 'POST':
        theme = ThemeTest.objects.get(id=theme_id)
        theme.delete()
    return redirect('ktalk:theme')

def delete_theme_conversation(request):
    if request.method == 'POST':
        theme_id = request.POST.get('theme_id')
        found_theme = ThemeTest.objects.get(id = theme_id)
        theme = ConversationTest.objects.get(theme = found_theme)
        theme.delete()
    return redirect('ktalk:index')