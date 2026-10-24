# شارة الإطار القياسي للحكومة الإلكترونية

<!-- latest-badge:start -->
[![الإطار القياسي للحكومة الإلكترونية](../badges/unversioned/flat-ar.svg)](https://www.egovframe.go.kr/)
[![CI](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml)
[![Generate badges](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)
<!-- latest-badge:end -->

[![English](../badges/lang/en/outline.svg)](README.en.md)
[![한국어](../badges/lang/ko/outline.svg)](README.ko.md)
[![Español](../badges/lang/es/outline.svg)](README.es.md)
[![Tiếng Việt](../badges/lang/vi/outline.svg)](README.vi.md)
[![العربية](../badges/lang/ar/flat.svg)](README.ar.md)
[![Français](../badges/lang/fr/outline.svg)](README.fr.md)

**شارة SVG واحدة** لكل مشروع يستخدم الإطار القياسي للحكومة الإلكترونية. بدلاً من تضمين الشعارات يدويًا في كل مستودع، يتم الرجوع إلى شارة تتم صيانتها مركزيًا عبر عنوان URL خام. صيغة SVG ثابتة — لا حاجة لـ JavaScript، ولا لخادم نشر، ولا لعناوين URL Base64 طويلة.

## الاستخدام في سطر واحد

اختر الإصدار والأسلوب واللغة (`en`، `ko`، `es`، `vi`، `ar`، `fr`) من مسار URL. الأمثلة أدناه ترتبط بالبوابة الرسمية.

**الإنجليزية**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**العربية**
```md
[![الإطار القياسي للحكومة الإلكترونية 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
```

**شارات الإصدارات متعددة اللغات (`es` الإسبانية · `vi` الفيتنامية · `fr` الفرنسية)**
```md
[![Marco Estándar de Gobierno Electrónico 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![Khung chuẩn Chính phủ điện tử 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![Cadre standard de l'administration électronique 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(جميع الشارات متعددة اللغات تدعم كلاً من مسارات `badges/5.0.2/flat-<lang>.svg` و `badges/5.0.2/<lang>/flat.svg`.)*

## الكشف التلقائي عن الإصدارات

يمكن لملف README أن يعرض الإصدارات التي تعلنها ملفات بناء المشروع. يجدها `scripts/detect_version.py` ويعيد كتابة الكتل المعلَّمة في README، ويمكن لـ workflow تشغيله عند كل push.

### أين تُوجد الإصدارات

| البيئة | المكوّن | مُعلَن في |
| --- | --- | --- |
| بيئة التشغيل | الإطار القياسي للحكومة الإلكترونية | `pom.xml`: `org.egovframe.rte.version`, `egovframework.rte.version`, `<parent>` · `<dependency>`: `org.egovframe.boot`, `org.egovframe.web`, `org.egovframe.rte`<br>`build.gradle(.kts)`: `egovframeBootParentVersion`, `org.egovframe.*:artifact:version`<br>`settings.gradle(.kts)`, `gradle.properties`, `libs.versions.toml` |
| بيئة التطوير | Java | `pom.xml`: `java.version`, `maven.compiler.release`, `maven.compiler.source`, `maven.compiler.target`<br>`build.gradle(.kts)`: `sourceCompatibility`, `JavaLanguageVersion.of(17)` |
| بيئة التطوير | Spring Boot | `pom.xml`: `<parent>` `spring-boot-starter-parent`<br>`build.gradle(.kts)`: `id 'org.springframework.boot' version '3.5.6'` |
| بيئة التطوير | Gradle | `gradle/wrapper/gradle-wrapper.properties`: `distributionUrl` (`gradle-8.5-bin.zip`) |

- إذا أعلنت عدة وحدات عن إصدار، يُختار الأعلى.
- تُتجاهل التعليقات، وتُتخطى مجلدات مخرجات البناء والاعتماديات (`target` و`build` و`node_modules` ...).
- يُعرض فقط ما يعلنه المشروع بنفسه: تأتي الأصول (parent) في الإصدارات 4.x/5.x بنسخها الخاصة من Spring Boot وJava، فلا تظهر ما لم يذكرها ملف البناء.
- المشروع الذي لا يعلن عن أي إصدار يحصل على الشارة الاسمية فقط؛ والإصدار المعلن دون شارة منشورة (غير موجود في `versions.json`) يحصل على الشارة الاسمية مع تحذير.

### علامات README

ضع العلامات حيث يجب أن يظهر المحتوى. كل كتلة اختيارية لكن يلزم واحدة على الأقل: الأولى تصبح الشارة (شارة الإصدار، أو الشارة الاسمية فقط عندما لا يُعلَن أي إصدار)، والثانية تصبح جدولًا بالإصدارات المكتشفة مع الملف الذي يعلن عن كل منها.

```md
<!-- egovframe-badge:start -->
[![الإطار القياسي للحكومة الإلكترونية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/unversioned/flat-ar.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

<!-- egovframe-environment:start -->
<!-- egovframe-environment:end -->
```

النتيجة لـ `examples/sample-gradle-project`:

| الفئة | المكوّن | الإصدار | المصدر |
| --- | --- | --- | --- |
| بيئة التشغيل | الإطار القياسي للحكومة الإلكترونية | 5.0.0 | `build.gradle` |
| بيئة التطوير | Java | 17 | `build.gradle` |
| بيئة التطوير | Spring Boot | 3.5.6 | `build.gradle` |
| بيئة التطوير | Gradle | 8.5 | `gradle/wrapper/gradle-wrapper.properties` |

### التشغيل

شغّله محليًا (أضف `--check` ليفشل بدل الكتابة، مناسب لـ CI يتحقق فقط):

```bash
python3 scripts/detect_version.py --project . --readme README.md --language ar --style flat --write
```

### التشغيل في CI

[`.github/workflows/example-egovframe-badge.yml`](../.github/workflows/example-egovframe-badge.yml) مثال عملي: عند كل push يمس المشاريع يشغّل السكربت ويثبّت ملفات README المعاد كتابتها في الفرع. يعمل على `examples/sample-project` (Maven) و`examples/sample-gradle-project` (Gradle: Java وSpring Boot وGradle) و`examples/sample-project-unversioned` (بلا إعلان). انسخ `scripts/detect_version.py` وملف workflow إلى مشروعك، واضبط `PROJECT_DIRS` على `.` وأضف العلامات. للخطوات المخصصة يكتب `--github-output` القيم `version` و`badge_version` و`source` و`java` و`spring_boot` و`gradle` و`changed` في `$GITHUB_OUTPUT`.

## أزرار شارة محدد اللغة (`badges/lang/`)

أزرار شارة مستقلة لتبديل اللغة في ملفات `README` متعددة اللغات (`en`، `ko`، `es`، `vi`، `ar`، `fr`، `mn`، `bg`، `ne`). اللغة الحالية تستخدم `flat.svg`؛ اللغات الأخرى تستخدم `outline.svg` (أو كلها `flat.svg`).

```md
[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/flat.svg)](README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](docs/README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](docs/README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](docs/README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](docs/README.fr.md)
```

جميع إصدارات وقت التشغيل الرئيسية من [دليل بيئة التشغيل للإطار القياسي للحكومة الإلكترونية](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — من 1.0 إلى 5.x (إجمالي 53 إصدار) — مع خمسة أنماط لكل منها: `flat`، `flat-square`، `plastic`، `for-the-badge`، والأسلوب المخصص `outline` (تم استبعاد أسلوب `social` من shields.io لأنه يعتمد على تأثيرات hover).

| الأسلوب | مثال (الإنجليزية) | مثال (العربية) | أزرار اللغة |
| --- | --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (العربية)](../badges/5.0.1/flat-ar.svg) | ![English](../badges/lang/en/flat.svg) ![한국어](../badges/lang/ko/flat.svg) ![Español](../badges/lang/es/flat.svg) ![Tiếng Việt](../badges/lang/vi/flat.svg) ![العربية](../badges/lang/ar/flat.svg) ![Français](../badges/lang/fr/flat.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (العربية)](../badges/5.0.1/flat-square-ar.svg) | ![English](../badges/lang/en/flat-square.svg) ![한국어](../badges/lang/ko/flat-square.svg) ![Español](../badges/lang/es/flat-square.svg) ![Tiếng Việt](../badges/lang/vi/flat-square.svg) ![العربية](../badges/lang/ar/flat-square.svg) ![Français](../badges/lang/fr/flat-square.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (العربية)](../badges/5.0.1/plastic-ar.svg) | ![English](../badges/lang/en/plastic.svg) ![한국어](../badges/lang/ko/plastic.svg) ![Español](../badges/lang/es/plastic.svg) ![Tiếng Việt](../badges/lang/vi/plastic.svg) ![العربية](../badges/lang/ar/plastic.svg) ![Français](../badges/lang/fr/plastic.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (العربية)](../badges/5.0.1/for-the-badge-ar.svg) | ![English](../badges/lang/en/for-the-badge.svg) ![한국어](../badges/lang/ko/for-the-badge.svg) ![Español](../badges/lang/es/for-the-badge.svg) ![Tiếng Việt](../badges/lang/vi/for-the-badge.svg) ![العربية](../badges/lang/ar/for-the-badge.svg) ![Français](../badges/lang/fr/for-the-badge.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (العربية)](../badges/5.0.1/outline-ar.svg) | ![English](../badges/lang/en/outline.svg) ![한국어](../badges/lang/ko/outline.svg) ![Español](../badges/lang/es/outline.svg) ![Tiếng Việt](../badges/lang/vi/outline.svg) ![العربية](../badges/lang/ar/outline.svg) ![Français](../badges/lang/fr/outline.svg) |

## الإصدارات المدعومة

جميع إصدارات دليل بيئة التشغيل للإطار القياسي للحكومة الإلكترونية الـ 53:

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`, `5.0.7`
- **4.x**: `4.3`، `4.3.0`، `4.3.1`، `4.3.2`، `4.2`، `4.2.0`، `4.2.1`، `4.2.2`، `4.1`، `4.1.0`، `4.1.1`، `4.1.2`، `4.0`، `4.0.0`، `4.0.1`
- **3.x**: `3.10`، `3.10.0`، `3.10.1`، `3.10.2`، `3.9`، `3.9.0`، `3.8`، `3.8.0`، `3.7`، `3.7.0`، `3.6`، `3.6.0`، `3.5`، `3.5.0`، `3.5.1`، `3.1`، `3.1.0`، `3.0`، `3.0.0`
- **2.x**: `2.7`، `2.7.0`، `2.6`، `2.6.0`، `2.5`، `2.5.0`، `2.0`، `2.0.0`
- **1.x**: `1.0`، `1.0.0`

## إضافة الإصدارات وإنشاء الشارات

لإضافة إصدار جديد، حرر `versions.json` وشغّل المولّد (إصدار المشروع نفسه يكتشفه السكربت الموصوف أعلاه):

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

## التصميم

- يتم تأكيد ملفات SVG وتقديمها عبر عناوين URL الخام الخاصة بـ GitHub. محركات عرض README تحملها مباشرة؛ لا حاجة لخادم نشر.
- مصدر شعار واحد في `assets/egovframe-mark.svg`. جميع الشارات المولّدة تضمّن الشعار — لا توجد تبعيات صور خارجية.
- يتم تثبيت الإصدار والأسلوب في مسار الملف بحيث لا تتغير شارات README الحالية بشكل غير متوقع عند وصول إصدارات جديدة.
- `scripts/generate.py --check` و CI يتحققان من أن المخرجات المولّدة تطابق المصدر. يتم تطبيق تغييرات الأسلوب بشكل متسق عبر جميع الإصدارات.
- أسلوب `plastic` يستخدم نفس نقاط توقف التدرج اللامع مثل shields.io. `for-the-badge` يستخدم زوايا حادة (`rx="0"`) مثل shields.io.

تم استخراج الشعار من شارة README الحالية لـ eGovFramework. حقوق الشعار واسم الإطار القياسي للحكومة الإلكترونية تعود لأصحابها المعنيين.

## الترخيص

الكود (برنامج التوليد، الاختبارات، workflows) مرخص تحت [رخصة MIT](../LICENSE). أصل الشعار (`assets/egovframe-mark.svg`) والشعارات المضمنة في الشارات المولّدة **غير** مشمولة بهذه الرخصة وتعود لأصحابها الأصليين كما هو مذكور أعلاه.