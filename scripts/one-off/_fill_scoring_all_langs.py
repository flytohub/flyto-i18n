#!/usr/bin/env python3
"""Add scoring category/sub-vector translations for ALL 16 locales."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

T = {
    "code.scoring.cat.engineering": {
        "en": "Engineering", "zh-TW": "工程品質", "zh-CN": "工程质量",
        "ja": "エンジニアリング", "ko": "엔지니어링", "fr": "Ingénierie",
        "es": "Ingeniería", "de": "Engineering", "pt-BR": "Engenharia",
        "it": "Ingegneria", "vi": "Kỹ thuật", "th": "วิศวกรรม",
        "id": "Rekayasa", "hi": "इंजीनियरिंग", "tr": "Mühendislik", "pl": "Inżynieria",
    },
    "code.scoring.sv.errorHandling": {
        "en": "Error Handling", "zh-TW": "錯誤處理", "zh-CN": "错误处理",
        "ja": "エラーハンドリング", "ko": "에러 처리", "fr": "Gestion des erreurs",
        "es": "Manejo de errores", "de": "Fehlerbehandlung", "pt-BR": "Tratamento de erros",
        "it": "Gestione errori", "vi": "Xử lý lỗi", "th": "การจัดการข้อผิดพลาด",
        "id": "Penanganan Error", "hi": "त्रुटि प्रबंधन", "tr": "Hata Yönetimi", "pl": "Obsługa błędów",
    },
    "code.scoring.sv.techDebt": {
        "en": "Tech Debt", "zh-TW": "技術債", "zh-CN": "技术债",
        "ja": "技術的負債", "ko": "기술 부채", "fr": "Dette technique",
        "es": "Deuda técnica", "de": "Technische Schulden", "pt-BR": "Dívida técnica",
        "it": "Debito tecnico", "vi": "Nợ kỹ thuật", "th": "หนี้ทางเทคนิค",
        "id": "Utang Teknis", "hi": "तकनीकी ऋण", "tr": "Teknik Borç", "pl": "Dług techniczny",
    },
    "code.scoring.sv.perfPatterns": {
        "en": "Performance", "zh-TW": "效能模式", "zh-CN": "性能模式",
        "ja": "パフォーマンス", "ko": "성능 패턴", "fr": "Performance",
        "es": "Rendimiento", "de": "Leistung", "pt-BR": "Desempenho",
        "it": "Prestazioni", "vi": "Hiệu năng", "th": "ประสิทธิภาพ",
        "id": "Performa", "hi": "प्रदर्शन", "tr": "Performans", "pl": "Wydajność",
    },
    "code.scoring.sv.importHealth": {
        "en": "Module Health", "zh-TW": "模組健康度", "zh-CN": "模块健康度",
        "ja": "モジュール健全性", "ko": "모듈 상태", "fr": "Santé des modules",
        "es": "Salud de módulos", "de": "Modulgesundheit", "pt-BR": "Saúde dos módulos",
        "it": "Salute moduli", "vi": "Sức khỏe module", "th": "สุขภาพโมดูล",
        "id": "Kesehatan Modul", "hi": "मॉड्यूल स्वास्थ्य", "tr": "Modül Sağlığı", "pl": "Zdrowie modułów",
    },
    "code.scoring.sv.configDrift": {
        "en": "Config Drift", "zh-TW": "設定漂移", "zh-CN": "配置漂移",
        "ja": "設定ドリフト", "ko": "설정 드리프트", "fr": "Dérive de config",
        "es": "Deriva de config", "de": "Konfigurationsabweichung", "pt-BR": "Desvio de config",
        "it": "Deriva config", "vi": "Trôi dạt cấu hình", "th": "การเบี่ยงเบนค่า",
        "id": "Penyimpangan Konfigurasi", "hi": "कॉन्फ़िग ड्रिफ्ट", "tr": "Yapılandırma Sapması", "pl": "Dryf konfiguracji",
    },
    "code.scoring.sv.busFactor": {
        "en": "Bus Factor", "zh-TW": "巴士因子", "zh-CN": "巴士因子",
        "ja": "バスファクター", "ko": "버스 팩터", "fr": "Facteur bus",
        "es": "Factor bus", "de": "Bus-Faktor", "pt-BR": "Fator bus",
        "it": "Fattore bus", "vi": "Hệ số bus", "th": "Bus Factor",
        "id": "Bus Factor", "hi": "बस फ़ैक्टर", "tr": "Bus Faktörü", "pl": "Współczynnik bus",
    },
    "code.scoring.sv.apiDrift": {
        "en": "API Contract", "zh-TW": "API 契約", "zh-CN": "API 契约",
        "ja": "APIコントラクト", "ko": "API 계약", "fr": "Contrat API",
        "es": "Contrato API", "de": "API-Vertrag", "pt-BR": "Contrato de API",
        "it": "Contratto API", "vi": "Hợp đồng API", "th": "สัญญา API",
        "id": "Kontrak API", "hi": "API अनुबंध", "tr": "API Sözleşmesi", "pl": "Kontrakt API",
    },
    # Existing scoring keys — proper translations instead of English fallback
    "code.scoring.cat.vulnerabilities": {
        "en": "Vulnerabilities", "zh-TW": "弱點", "zh-CN": "漏洞",
        "ja": "脆弱性", "ko": "취약점", "fr": "Vulnérabilités",
        "es": "Vulnerabilidades", "de": "Schwachstellen", "pt-BR": "Vulnerabilidades",
        "it": "Vulnerabilità", "vi": "Lỗ hổng", "th": "ช่องโหว่",
        "id": "Kerentanan", "hi": "कमज़ोरियाँ", "tr": "Güvenlik Açıkları", "pl": "Podatności",
    },
    "code.scoring.cat.codeQuality": {
        "en": "Code Quality", "zh-TW": "程式碼品質", "zh-CN": "代码质量",
        "ja": "コード品質", "ko": "코드 품질", "fr": "Qualité du code",
        "es": "Calidad del código", "de": "Codequalität", "pt-BR": "Qualidade do código",
        "it": "Qualità del codice", "vi": "Chất lượng mã", "th": "คุณภาพโค้ด",
        "id": "Kualitas Kode", "hi": "कोड गुणवत्ता", "tr": "Kod Kalitesi", "pl": "Jakość kodu",
    },
    "code.scoring.cat.diligence": {
        "en": "Diligence", "zh-TW": "落實度", "zh-CN": "尽职度",
        "ja": "デューデリジェンス", "ko": "실사", "fr": "Diligence",
        "es": "Diligencia", "de": "Sorgfalt", "pt-BR": "Diligência",
        "it": "Diligenza", "vi": "Sự chuyên cần", "th": "ความขยัน",
        "id": "Kecermatan", "hi": "परिश्रम", "tr": "Özen", "pl": "Staranność",
    },
    "code.scoring.cat.documentation": {
        "en": "Documentation", "zh-TW": "文件", "zh-CN": "文档",
        "ja": "ドキュメント", "ko": "문서", "fr": "Documentation",
        "es": "Documentación", "de": "Dokumentation", "pt-BR": "Documentação",
        "it": "Documentazione", "vi": "Tài liệu", "th": "เอกสาร",
        "id": "Dokumentasi", "hi": "दस्तावेज़ीकरण", "tr": "Dokümantasyon", "pl": "Dokumentacja",
    },
    "code.scoring.sv.cveFindings": {
        "en": "CVE Findings", "zh-TW": "CVE 發現", "zh-CN": "CVE 发现",
        "ja": "CVE検出", "ko": "CVE 발견", "fr": "Résultats CVE",
        "es": "Hallazgos CVE", "de": "CVE-Funde", "pt-BR": "Achados CVE",
        "it": "Risultati CVE", "vi": "Phát hiện CVE", "th": "การค้นพบ CVE",
        "id": "Temuan CVE", "hi": "CVE खोज", "tr": "CVE Bulguları", "pl": "Wyniki CVE",
    },
    "code.scoring.sv.exposedSecrets": {
        "en": "Exposed Secrets", "zh-TW": "暴露的機密", "zh-CN": "暴露的密钥",
        "ja": "公開された秘密情報", "ko": "노출된 시크릿", "fr": "Secrets exposés",
        "es": "Secretos expuestos", "de": "Offene Geheimnisse", "pt-BR": "Segredos expostos",
        "it": "Segreti esposti", "vi": "Bí mật bị lộ", "th": "ข้อมูลลับที่เปิดเผย",
        "id": "Rahasia Terbuka", "hi": "उजागर रहस्य", "tr": "Açığa Çıkan Sırlar", "pl": "Ujawnione sekrety",
    },
    "code.scoring.sv.codeFindings": {
        "en": "Code Findings", "zh-TW": "程式碼發現", "zh-CN": "代码发现",
        "ja": "コード検出", "ko": "코드 발견", "fr": "Résultats du code",
        "es": "Hallazgos de código", "de": "Code-Funde", "pt-BR": "Achados de código",
        "it": "Risultati del codice", "vi": "Phát hiện mã", "th": "การค้นพบโค้ด",
        "id": "Temuan Kode", "hi": "कोड खोज", "tr": "Kod Bulguları", "pl": "Wyniki kodu",
    },
    "code.scoring.sv.complexFunctions": {
        "en": "Complex Functions", "zh-TW": "複雜函式", "zh-CN": "复杂函数",
        "ja": "複雑な関数", "ko": "복잡한 함수", "fr": "Fonctions complexes",
        "es": "Funciones complejas", "de": "Komplexe Funktionen", "pt-BR": "Funções complexas",
        "it": "Funzioni complesse", "vi": "Hàm phức tạp", "th": "ฟังก์ชันซับซ้อน",
        "id": "Fungsi Kompleks", "hi": "जटिल फ़ंक्शन", "tr": "Karmaşık Fonksiyonlar", "pl": "Złożone funkcje",
    },
    "code.scoring.sv.deadCode": {
        "en": "Dead Code", "zh-TW": "死碼", "zh-CN": "死代码",
        "ja": "デッドコード", "ko": "데드 코드", "fr": "Code mort",
        "es": "Código muerto", "de": "Toter Code", "pt-BR": "Código morto",
        "it": "Codice morto", "vi": "Mã chết", "th": "โค้ดตาย",
        "id": "Kode Mati", "hi": "डेड कोड", "tr": "Ölü Kod", "pl": "Martwy kod",
    },
    "code.scoring.sv.scanCoverage": {
        "en": "Scan Coverage", "zh-TW": "掃描覆蓋率", "zh-CN": "扫描覆盖率",
        "ja": "スキャンカバレッジ", "ko": "스캔 범위", "fr": "Couverture de scan",
        "es": "Cobertura de escaneo", "de": "Scan-Abdeckung", "pt-BR": "Cobertura de varredura",
        "it": "Copertura scansione", "vi": "Phạm vi quét", "th": "ความครอบคลุมการสแกน",
        "id": "Cakupan Pemindaian", "hi": "स्कैन कवरेज", "tr": "Tarama Kapsamı", "pl": "Pokrycie skanowania",
    },
    "code.scoring.sv.patchingSpeed": {
        "en": "Patching Speed", "zh-TW": "修補速度", "zh-CN": "修补速度",
        "ja": "パッチ速度", "ko": "패치 속도", "fr": "Vitesse de correctif",
        "es": "Velocidad de parcheo", "de": "Patch-Geschwindigkeit", "pt-BR": "Velocidade de correção",
        "it": "Velocità di patch", "vi": "Tốc độ vá lỗi", "th": "ความเร็วในการแพทช์",
        "id": "Kecepatan Patching", "hi": "पैचिंग गति", "tr": "Yama Hızı", "pl": "Szybkość łatania",
    },
    "code.scoring.sv.documentationScore": {
        "en": "Documentation Score", "zh-TW": "文件評分", "zh-CN": "文档评分",
        "ja": "ドキュメントスコア", "ko": "문서 점수", "fr": "Score de documentation",
        "es": "Puntuación de documentación", "de": "Dokumentationswert", "pt-BR": "Pontuação de documentação",
        "it": "Punteggio documentazione", "vi": "Điểm tài liệu", "th": "คะแนนเอกสาร",
        "id": "Skor Dokumentasi", "hi": "दस्तावेज़ीकरण स्कोर", "tr": "Dokümantasyon Puanı", "pl": "Wynik dokumentacji",
    },
}

locales = ["en", "zh-TW", "zh-CN", "ja", "ko", "fr", "es", "de", "pt-BR", "it", "vi", "th", "id", "hi", "tr", "pl"]

for locale in locales:
    fname = ROOT / "locales" / "code" / locale / "code.json"
    with open(fname, encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for key, translations in T.items():
        val = translations.get(locale, translations.get("en", ""))
        old = data["translations"].get(key, "")
        # Update if empty, or if non-en locale still has the English fallback
        if not old or (locale != "en" and old == translations.get("en", "")):
            data["translations"][key] = val
            updated += 1

    data["translations"] = dict(sorted(data["translations"].items()))
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write("\n")

    if updated:
        print(f"  {locale}: +{updated}")

print("Done")
