# Python VulnLab

Python VulnLab, modern web uygulamalarında karşılaşılan güvenlik açıklarını eğitim amaçlı olarak göstermek üzere hazırlanmış kapsamlı bir zafiyet laboratuvarıdır. Proje; FastAPI, Flask ve Django tabanlı örneklerle kırılgan (insecure) ve güvenli (secure) kod karşılaştırmaları üzerinden hem geliştiricilere hem de güvenlik ekiplerine gerçek saldırı yüzeyini anlamaları için pratik bir ortam sunar.

<img width="1895" height="937" alt="Screenshot 2025-11-25 at 18 59 14" src="https://github.com/user-attachments/assets/74fa2e1d-671b-4f4d-bd65-92283be8c869" />

---

## 🎯 Amaç

Bu laboratuvarın temel amacı Python ekosisteminde sık karşılaşılan zafiyetleri **gerçekçi PoC senaryoları**, **açık kod örnekleri** ve **güvenli uygulama pratikleri** eşliğinde deneyimletmektir. Özellikle API güvenliği, framework seviyesinde ortaya çıkan 0-day/near-0-day riskleri ve modern saldırı tekniklerine yönelik görünürlük sağlamak hedeflenmiştir.

---

## 🔍 İçerik ve Modüller

Proje aşağıdaki güvenlik kategorilerine göre yapılandırılmıştır:

### **01 — Broken Authentication**

* Zayıf oturum yönetimi
* Sabit token yapıları
* Yanlış doğrulama akışları

### **02 — JWT Pitfalls**

* `alg: none` istismarı
* `kid` üzerinden dosya okuma
* Zayıf secret ile brute-force yapılabilmesi

### **03 — Injection Attacks**

* SQL/NoSQL Injection
* Command Injection
* Template Injection (SSTI)

### **04 — Serialization Issues**

* Güvensiz `pickle` kullanımı
* Arbitrary code execution örnekleri

### **05 — Rate Limiting Errors**

* Limit uygulanmayan endpointler
* IP spoofing ile rate-limit aşımı

### **06 — Misconfiguration**

* Debug modda çalışan üretim ortamı örnekleri
* Açık admin panelleri

### **07 — AI-Assisted Coding Risks**

* LLM’lerin ürettiği insecure snippet’ların etkisi
* Injection risklerini genişleten modeller

### **08 — API Sprawl & Shadow API’ler**

* Auto-doc kaynaklı bilgi sızıntısı
* Gizli endpointlerin ifşası

Her klasörde:

* `insecure.py` → Kasitli olarak zafiyet içeren örnek
* `secure.py` → Güvenli implementasyon
* `explain.md` → Zafiyet açıklaması ve sömürü mantığı

---

## 🛠 Kullanılan Teknolojiler

* **FastAPI**
* **Django ORM**
* **Flask**
* **Uvicorn**
* **slowlapi** (Rate limiting)
* **Python 3.10+**

---

## 🚀 Kurulum

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Her modül kendi içinde bağımsız çalışabilir. Örneğin:

```bash
uvicorn 01_broken_auth.insecure:app --reload
```

---

## ⚠️ Uyarı (Legal Disclaimer)

Bu proje yalnızca **eğitim**, **farkındalık** ve **demo** amaçlıdır. Gerçek sistemlerde, kurum içi ortamlarda veya izinsiz platformlarda test edilmesi **kesinlikle yasaktır**.


---

## 📫 İletişim

Her türlü geri bildirim, geliştirme önerisi veya katkı için:
**yusufdalbudak** — GitHub

Proje geliştirmeye açıktır. Pull request gönderebilirsiniz.
