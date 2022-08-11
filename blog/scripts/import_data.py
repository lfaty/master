from blog.models import Article
def run():
    for i in range(5,15):
        article=Article()
        article.title="Article n° #%d" % i
        article.desc="Desciption article n° #%d % i"
        article.image="http://default"
        article.save()

print("Opération réussie")