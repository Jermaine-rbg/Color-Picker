from django.urls import path

from paintapp.views import ColorPickerView

urlpatterns = [
    # paintapp/
    path('', ColorPickerView.as_view(), name='paint'),
]