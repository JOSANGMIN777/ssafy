from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
            model = Actor
            fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class ActorDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    class Meta:
        model = Actor
        fields = ('id','name','movies',)

    movies = ActorDetailSerializer(read_only=True, many=True)

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
         model = Movie
         fields = ('title', 'overview')

class MovieSerializer(serializers.ModelSerializer):
    class MovieDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'
    
    class Meta:
        model = Movie
        fields = ('id','title','actors','review_set','title','overview','release_date','poster_path')
        # fields = '__all__'
    review_set = MovieDetailSerializer(read_only=True, many=True)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields=('movie',)
    class ReviewDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = ReviewDetailSerializer(read_only = True)