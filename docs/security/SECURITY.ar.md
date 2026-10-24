# سياسة الأمان

[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/outline.svg)](../../README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](../README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](../README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](../README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/flat.svg)](../README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](../README.fr.md)

## الإبلاغ عن الثغرات

**الرجاء عدم فتح issue عام لمشكلة أمنية.**

استخدم الإبلاغ الخاص عن الثغرات من GitHub:

➡ <https://github.com/leejongyoung/egovframe-badge/security/advisories/new>

إذا لم يكن الإبلاغ الخاص عن الثغرات ممكّنًا في المستودع، يرجى الإبلاغ عبر البريد الإلكتروني بدلاً من فتح issue عام.

يرجى تضمين:

- ما هو المتأثر (إصدار الشارة، سكريبت التوليد، أو workflow)
- كيفية إعادة إنتاجه، والتأثير المتوقع
- أي شيء قمت به بالفعل للتحقق منه (hashes، URLs، logs)

يتم التعامل مع التقارير بشكل خاص حتى يتوفر إصلاح؛ يُمنح الفضل عند الطلب.

## النطاق

داخل النطاق:

- SVGs الشارات في [`badges/`](../badges/): المحتوى المولّد، الشعار المضمّن، بيانات الإصدار الوصفية
- الأتمتة: [`.github/workflows/`](../.github/workflows/) و [`scripts/`](../scripts/). يتم توليد الشارات الجديدة عبر workflow `generate-badges`؛ أي طريقة تجعل هذه الخطوة تنتج مخرجات خاطئة، أو تسرّب التوكن، أو تشغّل إدخالاً غير موثوق تُعتبر ثغرة.

خارج النطاق، يُرجى الإبلاغ للمالك:

- إطار عمل eGovFrame وخادم التحميل الخاص به → مشروع eGovFrame، <https://www.egovframe.go.kr/> و [eGovFramework](https://github.com/eGovFramework).
- GitHub نفسه → <https://github.com/github/github/security/policy>.
- shields.io → <https://github.com/badges/shields/security/policy>.

## الإصدارات المدعومة

فقط ما يوجد في `badges/` على الفرع الافتراضي هو ما يُحافظ عليه: جميع الإصدارات المدرجة في `versions.json`. الشارات التي تمت إزالتها عند وصول تصحيح أحدث من نفس السلسلة لا تُحافظ عليها.

## التحقق من الشارة بنفسك

كل شارة هي SVG مستقل بذاته مع شعار مضمّن. لإعادة التوليد والتحقق من إصدار مقابل المصدر من CI:

```bash
gh workflow run generate-badges.yml -R leejongyoung/egovframe-badge -f version=5.0.2
```