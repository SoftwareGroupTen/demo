from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from comment import models as commentModels
from upload import models as uploadModels
from .forms import CommentForm

# Create your views here.

def comment(request):
    uploadFile=uploadModels.userfile.objects.all()
    context = {'uploadFile': uploadFile}
    return render(request, 'hwlist.html', context)

def postComment(request):
    fileId=request.GET.get('fileId')
    context = {'fileId': fileId}
    return render(request, 'postComment.html', context)

def showComment(request):
    if request.method == 'POST':
        fileId=request.POST.get('fileId')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            point=request.POST.get('point')
            body=request.POST.get('body')
            newComment=commentModels.Comment()
            newComment.userfile_id=fileId
            newComment.point=point
            newComment.body=body
            newComment.save()
        else:
            comment=commentModels.Comment.objects.filter(userfile=fileId)
            context = {'error': '输入内容有误或为空，请重新填写。', 'fileId': fileId, 'comment': comment}
            return render(request, 'postComment.html', context)
    else:
        fileId=request.GET.get('fileId')
    comment=commentModels.Comment.objects.filter(userfile=fileId)
    context = {'comment': comment}
    return render(request, 'showComment.html', context)

def deleteComment(request):
    commentId=request.GET.get('commentId')
    deleComment=commentModels.Comment.objects.filter(id=int(commentId))
    deleComment.delete()
    fileId=request.GET.get('fileId')
    comment=commentModels.Comment.objects.filter(userfile=fileId)
    context = {'comment': comment}
    return render(request, 'showComment.html', context)