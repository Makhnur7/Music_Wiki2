from django.shortcuts import render, get_object_or_404
from .models import Group, Album, Song, GroupMember
from django.db.models import Q


# Главная страница
def index(request):
    query = request.GET.get('q', '').strip()
    if query:
        groups = Group.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).order_by('-pk')

        albums = Album.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).order_by('-pk')

        songs = Song.objects.filter(
            Q(name__icontains=query) | Q(lyrics__icontains=query)
        ).order_by('-pk')
        

        members = GroupMember.objects.filter(
            Q(name__icontains=query) | Q(biography__icontains=query)
        ).order_by('-pk')
    else:
        groups = Group.objects.all().order_by('-pk')[:5]
        albums = Album.objects.all().order_by('-pk')[:5]
        songs = Song.objects.all().order_by('-pk')[:5]
        members = GroupMember.objects.all().order_by('-pk')[:5]

    return render(request, 'index.html', {  
        'query': query,
        'groups': groups,
        'albums': albums,
        'songs': songs,
        'members': members,
    })



def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

def member_list(request):
    members = GroupMember.objects.all()
    return render(request, 'member_list.html', {'members': members})

# Детальная информация о группе
def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk) 
    albums = Album.objects.filter(group=group)  
    songs = Song.objects.filter(group=group)  
    members = GroupMember.objects.filter(group=group)

    return render(request, 'music/group_detail.html', {  
        'group': group,
        'albums': albums,
        'songs': songs,
        'members': members,
    })

# Детальная информация об альбоме
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    songs = Song.objects.filter(album=album)  

    return render(request, 'music/album_detail.html', {  
        'album': album,
        'songs': songs,
    })


# Детальная информация о песне
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)  

    return render(request, 'song_detail.html', {  
        'song': song,
    })

# Детальная информация об участнике группы
def member_detail(request, pk):
    member = get_object_or_404(GroupMember, pk=pk)  
    group = member.group

    return render(request, 'member_detail.html', {  
        'member': member,
        'group': group,
    })

def search(request):
    query = request.GET.get('query', '')
    groups = Group.objects.filter(Q(name__icontains=query))
    albums = Album.objects.filter(Q(name__icontains=query))
    songs = Song.objects.filter(Q(name__icontains=query))
    members = GroupMember.objects.filter(Q(name__icontains=query))

    context = {
        'query': query,
        'groups': groups,
        'albums': albums,
        'songs': songs,
        'members': members,
    }
    return render(request, 'search.html', context)