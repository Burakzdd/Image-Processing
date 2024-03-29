Bu çalışmada çeşitli nesne tespit ve takip yöntemleri üzerine çalışmalar yapılmaktadır.

## 1- Template Matching (Şablon eşitleme)
Template Matching (Şablon Eşleştirme) yöntemi ile nesne tanıma daha çok kaynak bir görüntü üzerinde bir şablonu aramak için kullanılır. Nesneleri ayırt etmede çok fazla başarılı değildir. Mesela masa üzerinde duran bir bardak görüntüsünde bardağı bulmak için kullanılabilir. Ancak kaynak üzerine verdiğimiz şablon birebir olarak arandı için bu masa bu şablonun direk masa üzerindeki bardak görüntüsünden kırpılmış olması gerekebilir. Yani çok kullanışlı değilir anlık bir görüntü üzerinde işe yaramaz.
Bu yöndemin çalışma mantığı şu şekildir; tespit edilmek istenilen nesne sliding window (kayan, sürgülü pencere) yöntemi ile aranır. Şablon aranacak görsel üzerine yerleştirilir ve her bir piksel üzerinde döndürülür. Kullanılan benzerlik yöntemine göre bir benzerlik oranı oluşturulur ve şablon ile o anki dönülen şablon benzer ise sonuç olarak pikseller döndürür ve işaretlenir. Bu yöntem openCV’de cv2 kütüphanesi içerisinde yüklü olan matchTemplate komutu ile gerçekleştirilir.

## 2- Optical Flow
### 2.1- Lucas-Kanade Optik Akış
Optik akış, bir gözlemci ile bir sahne arasındaki göreceli hareketin neden olduğu görsel bir sahnedeki nesnelerin, yüzeylerin ve kenarların görünür hareket modelidir. Optik akış, bir görüntüdeki parlaklık modelinin görünür hareket hızlarının dağılımı olarak da tanımlanabilir. Görüntü işlemede, nesnenin veya kameranın hareketinin neden olduğu iki ardışık kare arasındaki değişimde görülen hareket modelidir. Mesela nesne üzerinde bir nokta belirlensin bu nesne hareket ettikçe nokta da nesne ile birlikte sürekli harekt eder. Bu hareket sonucunda dabaşlangıç noktasından bitiş noktasına bir çizgi oluşmuş olur.
Bütün bu işlemler OpennCV’de tek bir komut ile kolaylıkla yapılabilrmektedir. Bu komut cv2 kütüphanesi içerisinde kayıtlı olan calcOpticalFlowPyrLK() ‘dir. Bu komut kullanılırken görüntü üzerindeki noktalara karar vermek için cv.goodFeaturesToTrack () komutu kullanılır.

### 2.2- Yoğun Optik Akış
Lucas-Kanade yöntemi, seyrek bir veri kümesi için optik akış hesaplar. Eğer daha yoğun bir optik akış hesaplamak yani takibi yapılacak olan noktaların daha sık olması olması isteniyorsa başka bir algoritma kullanılır. Bu algoritmada sadece komşu noktalar için değil çerçeve içerisindeki tüm noktalar için optik akış sağlanır. Bu yöntem opencv de yine cv2 kütüphanesi içerisindeki calcOpticalFlowPyrLK() komutu ile gerçekleştirilir. Yöntemde şu aşamalar izlenir; İlk olarak optik akış vektörlerine sahip 2 kanallı bir dizi elde edilir(u,v). Bu vektörlerin büyüklükleri ve yönleri bulunur. Görselleştirmenin anlaşılır olması için sonuç renklendirilir. Görüntü HSV formatında renklendirilirken; yön, görüntünün ton (hue) değerine, büyüklük ise değer(value) düzlemine karşılık gelir.

## 3- Mean Shift (Ortalama Kaydırma) Algoritması
Bu algoritma basitçe veri kümesi (görüntü) üzerindeki veri dağılımının en yüksek olduğu yerl bulmayı sağlar. Bu yüksek dağılımlı yerler (tepe noktaları) , takip edilmek istenen nesne olacaktır. Yani alnınan ve devam eden görselde sürekli olarak tepe noktaları belirlenip işaretlendiğinde cisimle beraber işaretlerde yerdeğiştirecek e bu şekilde nesne takip işlemi gerçekleştirilmiş olacaktır.
OpenCV'de meanhift'i kullanmak için, önce hedefi ayarlamalı, histogramını bulmalıyız, böylece ortalama kaymanın hesaplanması için hedefi her çerçevede geri projelendirebiliriz. Ayrıca, pencerenin başlangıç konumunu da sağlamamız gerekir. Histogram için burada yalnızca ton(hue) dikkate alınır. Ayrıca, düşük ışık nedeniyle yanlış değerlerden kaçınmak için, düşük ışık değerleri cv.inRange () işlevi kullanılarak atılır. Yeni konumu (tepe noktaları) almak için yani meanshifti uygulamak için ise cv2 kütüphanesi içerisinde kayıtlı meanShift() komutu kullanılır.

## 4- CamShift Algoritması
Neredeyse meanshift ile aynıdır, ancak döndürülmüş bir dikdörtgen ve kutu parametreleri döndürür. Yani nensenin hareketine göre takip eden kutu da büyüyüp küçülür ve yönünü değiştirebilir.

## 5- Arka Plan Bölümleme (Background Segmantation)
Bir video içerindeki arka arkaya gelen video iki video çerçevesinin birbirinden çıkarılması yönetimidir. Bu yöntem ile nesneleri bulup takip ettirebiliriz. Bu yöntem oldukça hızlı çalışır ancak ışık ve gürültülere karşı çok hassastır.
Bu yöntem opencv de cv2 kütüphanesi içerisindeki createBackgroundSubtractorMOG2 komutu ile kullanılır. Bu komut ile birlikte daha iyi sonuç alınabilmek için gürültü azaltmaya yarayan cv2 kütüphanesi içerisinde tanımlı medianBlur komutu ile kullanılabilir.
