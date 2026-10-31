# دليل المساهمة في شارة الإطار القياسي للحكومة الإلكترونية

[![العربية](../../badges/lang/ar/flat.svg)](CONTRIBUTING.ar.md)
[![English](../../badges/lang/en/outline.svg)](CONTRIBUTING.en.md)
[![한국어](../../badges/lang/ko/outline.svg)](CONTRIBUTING.ko.md)
[![Español](../../badges/lang/es/outline.svg)](CONTRIBUTING.es.md)
[![Tiếng Việt](../../badges/lang/vi/outline.svg)](CONTRIBUTING.vi.md)
[![Français](../../badges/lang/fr/outline.svg)](CONTRIBUTING.fr.md)

## قبل فتح طلب سحب

```bash
python3 -m pip install PyYAML==6.0.3
python3 -m unittest discover -s tests -v   # اختبارات البرامج النصية
```

يقوم CI بتشغيل الاختبارات والتحقق من اتساق إنشاء الشارات.

- تتبع رسائل الالتزام النمط الحالي: `feat(badges): add 5.1.0 badges`، `fix(generate): ...`، `docs(readme): ...`، `ci: ...`.
- لا تعدل ملفات SVG المولّدة مباشرة. تأتي الإصدارات الجديدة من `scripts/generate.py` (سير العمل `generate-badges`); لإعادة التحقق من الشارات الموجودة، شغّل `python3 scripts/generate.py --check`.
- مجموعة شارات واحدة لكل إصدار: إضافة `5.1.0` تولّد 5 أنماط × 6 لغات.
- يتم توليد نقاط دخول التوثيق: عدّل مصادر `docs/` ثم شغّل `python3 scripts/sync_readme.py` لتحديث `README.md` ونقاط الدخول في `.github/`. يجب أن تشير أزرار اللغة إلى المصادر المترجمة في `docs/`، بما فيها الإنجليزية.

## GitHub Actions والفوترة

- **مجاني في المستودعات العامة:** وفقًا لسياسة فوترة GitHub، فإن الـ runners القياسية المستضافة من GitHub (`ubuntu-latest`) **مجانية وغير محدودة الدقائق في المستودعات العامة**. يتم إنشاء الشارات أثناء `generate-badges.yml` وتثبيتها؛ لا يتم استهلاك مواد Actions أو تخزين Release.

## الأمان

لا تبلغ عن الثغرات الأمنية في issues؛ اتبع الإجراء في [SECURITY.ar.md](../security/SECURITY.ar.md).