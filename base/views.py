from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Movie,Rezervation
from .forms import RezervationForm
from rest_framework.decorators import api_view
# from .serializers import MovieSerializer,RezervationSerializer

@api_view(['GET'])
def home(request):
    movies= Movie.objects.all()
    # normally i would serialize the data for react app 
    # serializer=MovieSerializer(movies, many=True)
    # context={'movies':serializer.data}
    #return Response(context)

    context={'movies':movies}
    return render(request, 'movies.html', context)

def movie(request,pk):
    movie=Movie.objects.get(id=pk)
    movie_row=movie.salon_rows
    movie_column=movie.salon_columns
    reserved_seats=movie.rezervation_set.all()
    reserved_num=len(reserved_seats)-1
    form = RezervationForm()
    if request.method == 'POST' and request.POST.get('seats') :
        form = RezervationForm(request.POST)
        if form.is_valid():
            
            newrezervation = request.POST.get('seats').replace(',',  " ").split()
        for rezervation in newrezervation:
            seat= rezervation.split("-")
            rezerv=Rezervation(movie=movie,rows=seat[0], columns=seat[1])
            rezerv.save()
        context={'seats':request.POST.get('seats')[:-1],'movie':movie}
        return render(request, 'ticket.html',context)
    print(reserved_num)
    context={'reserved_num':reserved_num,'movie':movie,'reserved_seats':reserved_seats,'rows':range(movie_row), 'columns' : range(movie_column)}
    return render(request, 'movie.html', context)
    


