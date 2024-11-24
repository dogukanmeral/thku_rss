### Hakkında
THKÜ RSS, Türk Hava Kurumu Üniversitesi internet sayfalarında yapılan duyurularından RSS kaynağı oluşturan bir Python paketidir.

### Kurulumu
1. Klonlama: `git clone https://github.com/dogukanmeral/thku_rss`
2. Paketi oluşturma([Hatchling](https://pypi.org/project/hatchling/) ile): `hatchling build`
3. Kurulum: `pip install dist/*.whl`

### Kullanımı
Kurulum: 
`thku_rss -c`: config.json dosyasını açar.

Duyuruları Çekme:
`thku_rss -f`: config.json dosyasında varolan bağlantılardaki duyuruları çeker ve belirtilen dosya konumunda XML dosyalarını oluşturur.

### Katkıda Bulunun!
Yapılan duyurulardan daha hızlı ve pratik haberdar olunması için geliştirilen açık kaynaklı projede siz de geliştirici olarak katkıda bulunabilirsiniz. Önerileriniz, sorularınız ve iletişim için: dogukan.meral@hotmail.com
