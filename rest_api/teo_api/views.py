# -*- coding: utf-8 -*-
from .models import Data
from collections import Counter
from rest_framework.views import APIView
from collections import OrderedDict
from rest_framework.response import Response
from trans import trans
import re
from rest_framework import status


# View for /stats/ request

class Stats(APIView):

    def get(self, request):

        text = list(Data.objects.values_list("text", flat=True))
        word_list = [word for line in text for word in line.split()]
        counts = OrderedDict(Counter(word_list).most_common(10))

        return Response(counts)


# View for /stats/<autor>/ request

class Author(APIView):

    def get(self, request, req):

        # Creating dict, like: {"lukaszpilatowski": "Łukasz Piłatowski"}

        keys = []

        values = list(Data.objects.values_list("author", flat="True").distinct())

        for a in values:
            keys.append(trans(a).lower().replace(" ", ""))

        dictionary = dict(zip(keys, values))

        # If author doesn't exist

        if not req in dictionary.keys():
            content = 'Author does not exist'
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        # Change request to authors name

        qreq = dictionary[req]

        # 10 most used words in text

        text = list(Data.objects.values_list("text", flat=True))
        word_list = [word for line in text for word in line.split()]
        counts = OrderedDict(Counter(word_list).most_common(10))

        # Creating stats for author

        words = Data.objects.values_list("text", flat="True").filter(author=qreq)
        list_of_words = [x.split() for x in words]
        flat_list = [re.sub(r'[^\w\s]','',item) for sublist in list_of_words for item in sublist]

        word_counts = Counter(flat_list)
        y = OrderedDict((k, word_counts[k]) for k in counts.keys())

        return Response(y)
