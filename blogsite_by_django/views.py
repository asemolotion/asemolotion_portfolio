from django.views.generic import RedirectView

class TopView(RedirectView):
    """
    ページは持たずに、ブログサイトにリダイレクトするだけ。
    """
    permanent = True
    url = 'https://asemolotion-blog.herokuapp.com/'
