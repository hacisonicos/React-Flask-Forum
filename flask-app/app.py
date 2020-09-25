from flask import Flask

app = Flask(__name__, static_folder='../build', static_url_path='/')


""" @app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html') """


@app.route('/api')
def get_news_data():
    data = dict()

    data["title"] = "İstanbul Eczacı Odası, zatürre aşısı olması gereken risk gruplarını açıkladı"
    data["url"] = "https://static.birgun.net/resim/haber-detay-resim/2020/09/24/istanbul-eczaci-odasi-zaturre-asisi-olmasi-gereken-risk-gruplarini-acikladi-784561-5.jpg"
    data["alt"] = "news"
    data["context"] = """İstanbul Eczacı Odası, zatürre aşısı (pnömokok) hakkında Hasta Bilgilendirme Broşürü hazırladı. Odadan yapılan açıklamaya göre broşürde, yeni tip koronavirüs (Covid-19) pandemisi nedeniyle kamuoyunun gündeminde yer alan zatürre aşısına ilişkin merak edilen konulara yer verildi. Broşürde aşılamanın, hastalıkların ve buna bağlı ölümlerin önlenmesi açısından en önemli ve en etkili toplum sağlığı hizmeti olduğu belirtilerek, aşı uygulamalarıyla hastalıkların ve hastalıklara bağlı ölüm ve sakatlıkların önlenmesi, hastalıkların hafif atlatılmasının sağlanması, toplumsal bağışıklık kazanılmasının hedeflendiği aktarıldı.
        """
    return data
