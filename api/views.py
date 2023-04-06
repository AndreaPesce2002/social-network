from django.http import Http404
from rest_framework.response import Response
from frontend.models import Utente, Post
from .serializars import PostSerializer,UtenteSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ------------------------------- UTENTI -----------------------------------------------
class UtenteList(APIView):
    """
    List all Utentes, or create a new Utente.
    """
    def get(self, request, format=None):
        Utentes = Utente.objects.all()
        serializer = UtenteSerializer(Utentes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UtenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        Utente.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UtenteDetail(APIView):
    """
    Retrieve, update or delete a Utente instance.
    """
    def get_object(self, pk):
        try:
            return Utente.objects.get(pk=pk)
        except Utente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Utente = self.get_object(pk)
        serializer = UtenteSerializer(Utente)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Utente = self.get_object(pk)
        serializer = UtenteSerializer(Utente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Utente = self.get_object(pk)
        Utente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------- POST -----------------------------------------------
class PostList(APIView):
    """
    List all posts, or create a new post.
    """
    def get(self, request, format=None):
        contenuto=request.GET.get('contenuto',False)
        seguiti=request.GET.get('seguiti',False)
        creatore=request.GET.get('creatore',False)
        ordine=request.GET.get('ordineLike',False)
        if contenuto:
            posts=Post.objects.filter(post__icontains=contenuto)
        elif creatore:
            posts=Post.objects.filter(creatore=creatore)
        elif seguiti:
            follower_ids = Utente.objects.filter(id=seguiti).values_list('followers__id', flat=True)
            posts = Post.objects.filter(creatore_id__in=follower_ids)

        else:
            posts = Post.objects.all()

        if ordine:
            posts.order_by('like').values()
            
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        # elimina tutti gli oggetti del modello Post
        Post.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PostDetail(APIView):
    """
    Retrieve, update or delete a post instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        print('PUT request:', request)
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
