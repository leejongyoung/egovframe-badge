# سياسة الأمان

[![English](../../badges/lang/en/outline.svg)](SECURITY.en.md)
[![한국어](../../badges/lang/ko/outline.svg)](SECURITY.ko.md)
[![Español](../../badges/lang/es/outline.svg)](SECURITY.es.md)
[![Tiếng Việt](../../badges/lang/vi/outline.svg)](SECURITY.vi.md)
[![العربية](../../badges/lang/ar/flat.svg)](SECURITY.ar.md)
[![Français](../../badges/lang/fr/outline.svg)](SECURITY.fr.md)

## الإبلاغ عن الثغرات

**الرجاء عدم فتح issue عام لمشكلة أمنية.**

استخدم الإبلاغ الخاص عن الثغرات من GitHub:

➡ <https://github.com/leejongyoung/egovframe-badge/security/advisories/new>

إذا لم يكن الإبلاغ الخاص عن الثغرات ممكّنًا في المستودع، يرجى التواصل مع المشرف بشكل خاص عبر وسائل الاتصال في ملف مالك المستودع على GitHub بدلاً من فتح issue عام.

يرجى تضمين:

- ما هو المتأثر (إصدار الشارة، سكريبت التوليد، أو workflow)
- كيفية إعادة إنتاجه، والتأثير المتوقع
- أي شيء قمت به بالفعل للتحقق منه (hashes، URLs، logs)

يتم التعامل مع التقارير بشكل خاص حتى يتوفر إصلاح؛ يُمنح الفضل عند الطلب.

## النطاق

داخل النطاق:

- SVGs الشارات في [`badges/`](../../badges/): المحتوى المولّد، الشعار المضمّن، بيانات الإصدار الوصفية
- الأتمتة: [`.github/workflows/`](../../.github/workflows/) و [`scripts/`](../../scripts/). يتم توليد الشارات الجديدة عبر workflow `generate-badges`؛ أي طريقة تجعل هذه الخطوة تنتج مخرجات خاطئة، أو تسرّب التوكن، أو تشغّل إدخالاً غير موثوق تُعتبر ثغرة.

خارج النطاق، يُرجى الإبلاغ للمالك:

- إطار عمل eGovFrame وخادم التحميل الخاص به → مشروع eGovFrame، <https://www.egovframe.go.kr/> و [eGovFramework](https://github.com/eGovFramework).
- GitHub نفسه → <https://github.com/github/github/security/policy>.
- shields.io → <https://github.com/badges/shields/security/policy>.

## الإصدارات المدعومة

فقط ما يوجد في `badges/` على الفرع الافتراضي هو ما يُحافظ عليه: جميع الإصدارات المدرجة في `versions.json`. الشارات التي تمت إزالتها عند وصول تصحيح أحدث من نفس السلسلة لا تُحافظ عليها.

## التحقق من الشارة بنفسك

كل شارة هي SVG مستقل بذاته مع شعار مضمّن. للتحقق من أن كل شارة مثبتة تطابق مخرجات المولّد:

```bash
python3 scripts/generate.py --check
```