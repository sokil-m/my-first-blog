"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

    Правила створення  regex тобто взаємозвязок відображення певного url
    ^ для початку тексту
    $ для кінця тексту
    \d для цифри
    + щоб позначити, що попередній символ має бути повторений мінімум один раз
    () для захоплення частини шаблону

Приклад:
Тепер уявіть, що у вас є сайт з такою адресою: http://www.mysite.com/post/12345/, де 12345 - це номер вашого посту.

Написання окремих відображень для усіх номерів постів було б дійсно нестерпним. За допомогою регулярних виразів ми можемо створити шаблон, який відповідає url і витягти номер для нас: ^post/(\d+)/$. Давайте розберемо його по частинах, щоб побачити, що ми тут робимо:

^post/ говорить Django взяти що-небудь, що має post/ на початку url (зразу після ^)
(\d+) означає, що буде число (одне або декілька цифр), і ми хочемо, щоб число захопилось і вибралось
/ вказує Django, що наступним символом має бути /
$ далі позначає кінець URL-адреси, а це означає, що під шаблон підходять лише ті рядки, які закінчуються на /


"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
