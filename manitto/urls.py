from django.urls import path

from manitto import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result',views.result, name='result')
    # path('download', views.download, name="download"),
    # path('download-check', views.download, name="download-check"),
    # # path('attachTs', views.attachTs, name="attachTs"),
    # # path('downloadTemp', views.downloadTemp, name="downloadTemp"),
    # # path('uploadA', views.uploadA, name="uploadA"),
    # # path('uploadB', views.uploadB, name="uploadB"),
    # # path('checkDif', views.checkDif, name="checkDif"),
    # # path('finalUpload', views.finalUpload, name="finalUpload"),
    # path('checkDif', views.upload, name="checkDif"),
    # path('finalUpload', views.upload, name="finalUpload"),

    # path('download_fake', views.download_fake, name="download_fake"),
]