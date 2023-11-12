from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Review, Movie
from .serializers import ActorListSerializer,ActorSerializer,MovieListSerializer,MovieSerializer,ReviewListSerializer,ReviewSerializer
from rest_framework import status

@api_view(['GET'])
def actor_list(request):
    # 전체 배우 목록 제공
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    # 단일 배우 정보 제공 (출연 영화 제목 포함)
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    # 전체 영화 목록 제공
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    # 단일 영화 정보 제공(출연 배우 이름과 리뷰 목록포함)
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    # 전체 리뷰 목록 제공
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request, review_pk):
    # 단일 리뷰 조회 & 수정 & 삭제 (출연 영화제목포함)
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)    
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(data=f'message:{review_pk} is deleted',status=status.HTTP_204_NO_CONTENT)
    


@api_view(['POST'])
def create_review(request, movie_pk):
    # 리뷰생성
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
