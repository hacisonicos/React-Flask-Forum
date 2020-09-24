import React from "react";
import "./App.css";
import Navbar from "./components/navbar/navbar";
import News from "./components/News/news";
import { useState, useEffect } from "react";

function App() {
  const [newsData, setnewsData] = useState(0);

  useEffect(() => {
    fetch("/api")
      .then((res) => res.json())
      .then((data) => {
        setnewsData(data);
      });
  }, []);

  return (
    <div className="App">
      <Navbar />
      <header className="App-header">
        <News
          title={newsData.title}
          url={newsData.url}
          alt={newsData.alt}
          context={newsData.context}
        />
        <News
          title="Erdoğan'dan il kongresi uyarısı: Eften püften adaylar gelmesin"
          url={
            "https://static.birgun.net/resim/haber-detay-resim/2020/09/24/erdogan-dan-il-kongresi-uyarisi-eften-puften-adaylar-gelmesin-784498-5.jpg"
          }
          alt="news"
          context="AKP'de ekim ayında başlaması planlanan il kongreleriyle ilgili uyarıda bulunan Cumhurbaşkanı ve AKP Genel Başkanı Recep Tayyip Erdoğan, Eften püften adaylar gelmesin dedi.

        Hürriyet'ten Gizem Karakış'ın haberine göre, AKP MKYK toplantısında üyeler, Cumhurbaşkanı Erdoğan'a pandemi ile birlikte esnafın zarar ettiğini örneklerle anlattı. Kurmaylar, Sadece üniversite ve üniversite öğrencileri ile geçinen bazı iller var, esnaf sıkıntıda, üniversiteler, yurtlar ve okullar tamamı açılmalı” dediler.
        
        Koronavirüs'te çocukların ‘süper taşıyıcı’ olmadığını gösteren bir çalışma da Erdoğan’a sunuldu. Kurmaylar, çalışmaya göre 10 yaş ve altındaki çocukların da taşıyıcı olmadığını, okulların tamamının açılması ile pandeminin yayılma riskinin anlatıldığı kadar yüksek olmayabileceğini söylediler.
        "
        />
      </header>
    </div>
  );
}

export default App;
