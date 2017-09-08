# -*- coding: utf-8 -*-
from .models import Dane
from collections import Counter
from rest_framework.views import APIView
from collections import OrderedDict
from rest_framework.response import Response
from trans import trans
import re
from rest_framework import status

# Widok zwracajacy statystyki przy zapytaniu /stats/

class Stats(APIView):

    def get(self, request):

        text = list(Dane.objects.values_list("text", flat=True))
        word_list = [word for line in text for word in line.split()]
        counts = OrderedDict(Counter(word_list).most_common(10))

        return Response(counts)


# Widok zwracajacy statystyki dla kazdego autora przy zapytaniu /stats/<autor>/

class Author(APIView):

    def get(self, request, cos):

        # Tworzenie slownika w formie {"lukaszpilatowski": "Łukasz Piłatowski"}

        keys = []

        values = list(Dane.objects.values_list("author", flat="True").distinct())

        for a in values:
            keys.append(trans(a).lower().replace(" ", ""))

        dictionary = dict(zip(keys, values))

        # Jesli autor nie istnieje zwroci blad

        if not cos in dictionary.keys():
            content = 'Podany autor nie istnieje'
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        # Zamiana zapytania na dane autora

        qcos = dictionary[cos]

        # 10 slow ktorych szukam u autora

        text = list(Dane.objects.values_list("text", flat=True))
        word_list = [word for line in text for word in line.split()]
        counts = OrderedDict(Counter(word_list).most_common(10))

        # Wyswietlenie danych dla autora

        words = Dane.objects.values_list("text", flat="True").filter(author=qcos)
        list_of_words = [x.split() for x in words]
        flat_list = [re.sub(r'[^\w\s]','',item) for sublist in list_of_words for item in sublist]

        word_counts = Counter(flat_list)
        y = OrderedDict((k, word_counts[k]) for k in counts.keys())

        return Response(y)
