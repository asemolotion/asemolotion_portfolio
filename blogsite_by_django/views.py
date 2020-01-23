from django.views.generic import RedirectView

class TopView(RedirectView):
    """
    ページは持たずに、ブログサイト(asemolotion-blog.herokuapp.com/)にリダイレクトするだけ。
    """
    permanent = True
    url = 'https://asemolotion-blog.herokuapp.com/'
