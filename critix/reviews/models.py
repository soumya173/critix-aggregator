from django.db import models
from django.utils import timezone

LANGUAGE_OPTIONS = (
    ('english', 'ENGLISH'),
)
REL_STATUS_OPTIONS = (
    ('released', 'RELEASED'),
    ('upcoming', 'UPCOMING'),
)
GENRE_OPTIONS = (
    ('action', 'ACTION'),
)
GENDER_OPTIONS = (
    ('female', 'FEMALE'),
    ('male', 'MALE'),
    ('transgender', 'TRANSGENDER'),
    ('other', 'OTHER'),
)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    poster = models.ImageField(upload_to='media')
    language = models.CharField(choices=LANGUAGE_OPTIONS, max_length=100)
    release_date = models.DateTimeField()
    release_status = models.CharField(choices=REL_STATUS_OPTIONS, max_length=100)
    added = models.DateTimeField()

    @property
    def avg_rating(self):
        return

    def save(self, *args, **kwargs):
        # On save update the added field with current timestamp
        self.added = timezone.now()
        return super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.release_status}"

    class Meta:
        ordering = ['title', 'release_date']

class Genre(models.Model):
    movie = models.ForeignKey(Movie, related_name="movie_genre", on_delete=models.CASCADE)
    genre = models.CharField(choices=GENRE_OPTIONS, max_length=20)

    def __str__(self):
        return self.genre

    class Meta:
        ordering = ['genre']

class Rating(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_rating', on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.rating

    class Meta:
        ordering = ['rating']

class Review(models.Model):
    rating = models.OneToOneField(Rating, related_name='rating_review', on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)

    def __str__(self):
        return self.review

    class Meta:
        ordering = ['review']

class Cast(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_cast', on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    character_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.role} - {self.character_name}"

    class Meta:
        ordering = ['character_name', 'role']

class Artist(models.Model):
    cast = models.OneToOneField(Cast, related_name='cast_artist', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.gender}"

    class Meta:
        ordering = ['first_name', 'last_name']
