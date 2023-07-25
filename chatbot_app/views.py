from django.shortcuts import render, get_object_or_404, redirect
from .models import Message, Conversation
from .forms import MessageForm
from django.contrib.auth.models import AnonymousUser


def home_view(request):
    # Add your logic here to retrieve necessary data for the home page
    return render(request, 'home.html')


def home_view(request):
    # Add your logic here to retrieve necessary data for the home page
    return render(request, 'home.html')


def home_view(request):
    # Add your logic here to retrieve necessary data for the home page
    return render(request, 'home.html')


def chat_view(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    messages = Message.objects.filter(
        conversation_id=conversation_id).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # Save the new message to the database with the authenticated user as the sender
            if request.user.is_authenticated:
                message = Message.objects.create(
                    conversation=conversation, sender=request.user, content=content)
                message.save()
                # Redirect to the same chat page to display the new message
                return redirect('chat', conversation_id=conversation_id)
            else:
                # Handle the case when the user is not authenticated (e.g., show an error message)
                pass
    else:
        form = MessageForm()

    return render(request, 'chat.html', {'conversation': conversation, 'messages': messages, 'form': form})
