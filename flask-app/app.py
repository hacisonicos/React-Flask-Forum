from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__, static_folder='../build', static_url_path='/')
api = Api(app)


global news_data  # Şimdilik global olarak. Sonrasında sql databaseden alınacak
news_data = [{
    "title": "İstanbul Eczacı Odası, zatürre aşısı olması gereken risk gruplarını açıkladı",
    "url": "https://static.birgun.net/resim/haber-detay-resim/2020/09/24/istanbul-eczaci-odasi-zaturre-asisi-olmasi-gereken-risk-gruplarini-acikladi-784561-5.jpg",
    "alt": "news",
    "context": """İstanbul Eczacı Odası, zatürre aşısı (pnömokok) hakkında Hasta Bilgilendirme Broşürü hazırladı.

    Odadan yapılan açıklamaya göre broşürde, yeni tip koronavirüs (Covid-19) pandemisi nedeniyle kamuoyunun gündeminde yer alan zatürre aşısına ilişkin merak edilen konulara yer verildi.

    Broşürde aşılamanın, hastalıkların ve buna bağlı ölümlerin önlenmesi açısından en önemli ve en etkili toplum sağlığı hizmeti olduğu belirtilerek, aşı uygulamalarıyla hastalıkların ve hastalıklara bağlı ölüm ve sakatlıkların önlenmesi, hastalıkların hafif atlatılmasının sağlanması, toplumsal bağışıklık kazanılmasının hedeflendiği aktarıldı.
    """,
},

    {
    "title": "Erdoğan'dan il kongresi uyarısı: Eften püften adaylar gelmesin",
    "url": "https://static.birgun.net/resim/haber-detay-resim/2020/09/24/erdogan-dan-il-kongresi-uyarisi-eften-puften-adaylar-gelmesin-784498-5.jpg",
    "alt": "news",
    "context": """
    AKP'de ekim ayında başlaması planlanan il kongreleriyle ilgili uyarıda bulunan Cumhurbaşkanı ve AKP Genel Başkanı Recep Tayyip Erdoğan, Eften püften adaylar gelmesin dedi.

    Hürriyet'ten Gizem Karakış'ın haberine göre, AKP MKYK toplantısında üyeler, Cumhurbaşkanı Erdoğan'a pandemi ile birlikte esnafın zarar ettiğini örneklerle anlattı. Kurmaylar, Sadece üniversite ve üniversite öğrencileri ile geçinen bazı iller var, esnaf sıkıntıda, üniversiteler, yurtlar ve okullar tamamı açılmalı” dediler.
        
    Koronavirüs'te çocukların ‘süper taşıyıcı’ olmadığını gösteren bir çalışma da Erdoğan’a sunuldu. Kurmaylar, çalışmaya göre 10 yaş ve altındaki çocukların da taşıyıcı olmadığını, okulların tamamının açılması ile pandeminin yayılma riskinin anlatıldığı kadar yüksek olmayabileceğini söylediler.
    """,
}]


<<<<<<< Updated upstream
    data["title"] = "İstanbul Eczacı Odası, zatürre aşısı olması gereken risk gruplarını açıkladı"
    data["url"] = "https://static.birgun.net/resim/haber-detay-resim/2020/09/24/istanbul-eczaci-odasi-zaturre-asisi-olmasi-gereken-risk-gruplarini-acikladi-784561-5.jpg"
    data["alt"] = "news"
    data["context"] = """İstanbul Eczacı Odası, zatürre aşısı (pnömokok) hakkında Hasta Bilgilendirme Broşürü hazırladı. Odadan yapılan açıklamaya göre broşürde, yeni tip koronavirüs (Covid-19) pandemisi nedeniyle kamuoyunun gündeminde yer alan zatürre aşısına ilişkin merak edilen konulara yer verildi. Broşürde aşılamanın, hastalıkların ve buna bağlı ölümlerin önlenmesi açısından en önemli ve en etkili toplum sağlığı hizmeti olduğu belirtilerek, aşı uygulamalarıyla hastalıkların ve hastalıklara bağlı ölüm ve sakatlıkların önlenmesi, hastalıkların hafif atlatılmasının sağlanması, toplumsal bağışıklık kazanılmasının hedeflendiği aktarıldı.
        """
    return data
=======
class News(Resource):
    def get(self):
        return news_data


api.add_resource(News, "/news")
>>>>>>> Stashed changes
