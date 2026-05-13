from django.shortcuts import render, redirect
from .models import Photo, LoveMessage, BirthdayWish, PickupLine

def birthday_home(request):
    photos = Photo.objects.all()
    love_message = LoveMessage.objects.last()
    # Get all active pickup lines, ordered by the 'order' field
    pickup_lines = PickupLine.objects.filter(is_active=True).order_by('order')
    
    if request.method == 'POST':
        name = request.POST.get('name', 'Someone who loves you')
        message = request.POST.get('message')
        if message:
            BirthdayWish.objects.create(name=name, message=message)
        return redirect('birthday_home')
    
    wishes = BirthdayWish.objects.order_by('-created_at')[:50]
    
    # Convert pickup lines to JSON for JavaScript
    pickup_lines_data = []
    for line in pickup_lines:
        pickup_lines_data.append({
            'id': line.id,
            'question': line.question,
            'expectedAnswers': line.get_keywords_list(),
            'response': line.sweet_response,
            'hint': line.hint
        })
    
    context = {
        'photos': photos,
        'love_message': love_message,
        'wishes': wishes,
        'pickup_lines': pickup_lines_data,
        'girl_name': 'Faith ♥',  # Change to her name
        'your_name': 'Ezekiel',  # Change to your name
}                                           
    return render(request, 'birthday_app/birthday.html', context)


from .models import Photo, LoveMessage, BirthdayWish, PickupLine, Music

def birthday_home(request):
    photos = Photo.objects.all()
    love_message = LoveMessage.objects.last()
    pickup_lines = PickupLine.objects.filter(is_active=True).order_by('order')
    # Get active music
    music_list = Music.objects.filter(is_active=True).order_by('order')
    
    if request.method == 'POST':
        name = request.POST.get('name', 'Someone who loves you')
        message = request.POST.get('message')
        if message:
            BirthdayWish.objects.create(name=name, message=message)
        return redirect('birthday_home')
    
    wishes = BirthdayWish.objects.order_by('-created_at')[:50]
    
    # Convert pickup lines to JSON
    pickup_lines_data = []
    for line in pickup_lines:
        pickup_lines_data.append({
            'id': line.id,
            'question': line.question,
            'expectedAnswers': line.get_keywords_list(),
            'response': line.sweet_response,
            'hint': line.hint
        })
    
    context = {
        'photos': photos,
        'love_message': love_message,
        'wishes': wishes,
        'pickup_lines': pickup_lines_data,
        'music_list': music_list,  # Add this
        'girl_name': 'My Love',
        'your_name': 'Your Name',
    }
    return render(request, 'birthday_app/birthday.html', context)