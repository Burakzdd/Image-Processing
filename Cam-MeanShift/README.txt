Bu çalışmada yüz ve göz sınıflandırma işlemlerinde kullanılan haarcascade sınıflandırma modeli kullanılmaktadır. Çalışmada bu model openCV'nin MeanShift ve CamShift fonksiyonları ile kullanılmıştır

MeanShift algoritması basitçe veri kümesi (görüntü) üzerindeki veri dağılımının en yüksek olduğu yerl
bulmayı sağlamaktadır. Bu yüksek dağılımlı yerler (tepe noktaları) , takip edilmek istenen nesne
olacaktır. Yani alnınan ve devam eden görselde sürekli olarak tepe noktaları belirlenip
işaretlendiğinde cisimle beraber işaretlerde yerdeğiştirecek e bu şekilde nesne takip işlemi
gerçekleştirilmiş olacaktır.

CamShift Algoristması ise neredeyse meanshift ile aynıdır, ancak döndürülmüş bir dikdörtgen ve kutu parametreleri
döndürür. Yani nensenin hareketine göre takip eden kutu da büyüyüp küçülür ve yönünü
değiştirebilir.
