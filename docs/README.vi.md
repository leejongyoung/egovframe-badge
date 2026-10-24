# Huy hiệu Khung chuẩn Chính phủ điện tử

<!-- latest-badge:start -->
[![Khung chuẩn Chính phủ điện tử](../badges/unversioned/flat-vi.svg)](https://www.egovframe.go.kr/)
[![CI](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml)
[![Generate badges](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)
<!-- latest-badge:end -->

[![English](../badges/lang/en/outline.svg)](README.en.md)
[![한국어](../badges/lang/ko/outline.svg)](README.ko.md)
[![Español](../badges/lang/es/outline.svg)](README.es.md)
[![Tiếng Việt](../badges/lang/vi/flat.svg)](README.vi.md)
[![العربية](../badges/lang/ar/outline.svg)](README.ar.md)
[![Français](../badges/lang/fr/outline.svg)](README.fr.md)

Một **huy hiệu SVG đơn lẻ** cho mọi dự án sử dụng Khung chuẩn Chính phủ điện tử. Thay vì nhúng logo vào từng kho, hãy tham chiếu một huy hiệu được quản lý tập trung với một URL raw. SVG tĩnh — không cần JavaScript, không cần máy chủ triển khai, không cần URL Base64 dài.

## Sử dụng trong một dòng

Chọn phiên bản, kiểu dáng và ngôn ngữ (`en`, `ko`, `es`, `vi`, `ar`, `fr`) từ đường dẫn URL. Các ví dụ dưới đây liên kết đến cổng chính thức.

**Tiếng Anh**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**Tiếng Việt**
```md
[![Khung chuẩn Chính phủ điện tử 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
```

**Huy hiệu phiên bản đa ngôn ngữ (`es` tiếng Tây Ban Nha · `ar` tiếng Ả Rập · `fr` tiếng Pháp)**
```md
[![Marco Estándar de Gobierno Electrónico 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![الإطار القياسي للحكومة الإلكترونية 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
[![Cadre standard de l'administration électronique 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(Tất cả huy hiệu đa ngôn ngữ đều hỗ trợ cả hai đường dẫn `badges/5.0.2/flat-<lang>.svg` và `badges/5.0.2/<lang>/flat.svg`.)*

## Tự động phát hiện phiên bản

README có thể hiển thị các phiên bản mà tệp xây dựng của dự án khai báo. `scripts/detect_version.py` tìm chúng và viết lại các khối được đánh dấu trong README; workflow có thể chạy nó ở mỗi lần push.

### Nơi tìm thấy các phiên bản

| Môi trường | Thành phần | Khai báo tại |
| --- | --- | --- |
| Môi trường thực thi | Khung chuẩn Chính phủ điện tử | `pom.xml`: `org.egovframe.rte.version`, `egovframework.rte.version`, `<parent>` · `<dependency>`: `org.egovframe.boot`, `org.egovframe.web`, `org.egovframe.rte`<br>`build.gradle(.kts)`: `egovframeBootParentVersion`, `org.egovframe.*:artifact:version`<br>`settings.gradle(.kts)`, `gradle.properties`, `libs.versions.toml` |
| Môi trường phát triển | Java | `pom.xml`: `java.version`, `maven.compiler.release`, `maven.compiler.source`, `maven.compiler.target`<br>`build.gradle(.kts)`: `sourceCompatibility`, `JavaLanguageVersion.of(17)` |
| Môi trường phát triển | Spring Boot | `pom.xml`: `<parent>` `spring-boot-starter-parent`<br>`build.gradle(.kts)`: `id 'org.springframework.boot' version '3.5.6'` |
| Môi trường phát triển | Gradle | `gradle/wrapper/gradle-wrapper.properties`: `distributionUrl` (`gradle-8.5-bin.zip`) |

- Nếu nhiều mô-đun cùng khai báo, phiên bản cao nhất được chọn.
- Bỏ qua chú thích; bỏ qua thư mục kết quả build và thư viện (`target`, `build`, `node_modules`, ...).
- Chỉ hiển thị những gì dự án tự khai báo: parent của phiên bản 4.x/5.x mang theo Spring Boot và Java riêng, nên sẽ không xuất hiện nếu tệp build không ghi rõ.
- Dự án không khai báo phiên bản dùng huy hiệu chỉ có tên; phiên bản đã khai báo nhưng chưa có huy hiệu (không có trong `versions.json`) dùng huy hiệu chỉ có tên kèm cảnh báo.

### Dấu đánh dấu trong README

Đặt các dấu đánh dấu ở nơi nội dung cần xuất hiện. Mỗi khối là tùy chọn nhưng cần ít nhất một khối: khối đầu thành huy hiệu (huy hiệu phiên bản, hoặc huy hiệu chỉ có tên khi không khai báo phiên bản), khối thứ hai thành bảng các phiên bản đã phát hiện kèm tệp khai báo từng phiên bản.

```md
<!-- egovframe-badge:start -->
[![Khung chuẩn Chính phủ điện tử](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/unversioned/flat-vi.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

<!-- egovframe-environment:start -->
<!-- egovframe-environment:end -->
```

Kết quả cho `examples/sample-gradle-project`:

| Phân loại | Thành phần | Phiên bản | Nguồn |
| --- | --- | --- | --- |
| Môi trường thực thi | Khung chuẩn Chính phủ điện tử | 5.0.0 | `build.gradle` |
| Môi trường phát triển | Java | 17 | `build.gradle` |
| Môi trường phát triển | Spring Boot | 3.5.6 | `build.gradle` |
| Môi trường phát triển | Gradle | 8.5 | `gradle/wrapper/gradle-wrapper.properties` |

### Chạy

Chạy cục bộ (thêm `--check` để báo lỗi thay vì ghi tệp, phù hợp với CI chỉ kiểm tra):

```bash
python3 scripts/detect_version.py --project . --readme README.md --language vi --style flat --write
```

### Chạy trong CI

[`.github/workflows/example-egovframe-badge.yml`](../.github/workflows/example-egovframe-badge.yml) là một ví dụ hoạt động: ở mỗi lần push chạm vào các dự án, nó chạy script và commit các README đã viết lại vào nhánh. Nó chạy trên `examples/sample-project` (Maven), `examples/sample-gradle-project` (Gradle: Java, Spring Boot, Gradle) và `examples/sample-project-unversioned` (không khai báo). Hãy sao chép `scripts/detect_version.py` và workflow vào dự án của bạn, đặt `PROJECT_DIRS` thành `.` và thêm các dấu đánh dấu. Với các bước tùy chỉnh, `--github-output` ghi `version`, `badge_version`, `source`, `java`, `spring_boot`, `gradle` và `changed` vào `$GITHUB_OUTPUT`.

## Nút huy hiệu chọn ngôn ngữ (`badges/lang/`)

Các nút huy hiệu độc lập để chuyển đổi ngôn ngữ trong `README` đa ngôn ngữ (`en`, `ko`, `es`, `vi`, `ar`, `fr`, `mn`, `bg`, `ne`). Ngôn ngữ hiện tại dùng `flat.svg`; các ngôn ngữ khác dùng `outline.svg` (hoặc tất cả `flat.svg`).

```md
[![English](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/en/flat.svg)](README.md)
[![한국어](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/ko/outline.svg)](README.ko.md)
[![Español](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/es/outline.svg)](docs/README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/vi/outline.svg)](docs/README.vi.md)
[![العربية](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/ar/outline.svg)](docs/README.ar.md)
[![Français](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/fr/outline.svg)](docs/README.fr.md)
```

Tất cả các phiên bản chính từ [Hướng dẫn môi trường thực thi của Khung chuẩn Chính phủ điện tử](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — từ 1.0 đến 5.x (tổng cộng 53 phiên bản) — với năm kiểu dáng mỗi loại: `flat`, `flat-square`, `plastic`, `for-the-badge` và kiểu tùy chỉnh `outline` (kiểu `social` của shields.io bị loại vì phụ thuộc vào hiệu ứng hover).

| Kiểu dáng | Ví dụ (Tiếng Anh) | Ví dụ (Tiếng Việt) | Nút ngôn ngữ |
| --- | --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (Tiếng Việt)](../badges/5.0.1/flat-vi.svg) | ![English](../badges/lang/en/flat.svg) ![한국어](../badges/lang/ko/flat.svg) ![Español](../badges/lang/es/flat.svg) ![Tiếng Việt](../badges/lang/vi/flat.svg) ![العربية](../badges/lang/ar/flat.svg) ![Français](../badges/lang/fr/flat.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (Tiếng Việt)](../badges/5.0.1/flat-square-vi.svg) | ![English](../badges/lang/en/flat-square.svg) ![한국어](../badges/lang/ko/flat-square.svg) ![Español](../badges/lang/es/flat-square.svg) ![Tiếng Việt](../badges/lang/vi/flat-square.svg) ![العربية](../badges/lang/ar/flat-square.svg) ![Français](../badges/lang/fr/flat-square.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (Tiếng Việt)](../badges/5.0.1/plastic-vi.svg) | ![English](../badges/lang/en/plastic.svg) ![한국어](../badges/lang/ko/plastic.svg) ![Español](../badges/lang/es/plastic.svg) ![Tiếng Việt](../badges/lang/vi/plastic.svg) ![العربية](../badges/lang/ar/plastic.svg) ![Français](../badges/lang/fr/plastic.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (Tiếng Việt)](../badges/5.0.1/for-the-badge-vi.svg) | ![English](../badges/lang/en/for-the-badge.svg) ![한국어](../badges/lang/ko/for-the-badge.svg) ![Español](../badges/lang/es/for-the-badge.svg) ![Tiếng Việt](../badges/lang/vi/for-the-badge.svg) ![العربية](../badges/lang/ar/for-the-badge.svg) ![Français](../badges/lang/fr/for-the-badge.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (Tiếng Việt)](../badges/5.0.1/outline-vi.svg) | ![English](../badges/lang/en/outline.svg) ![한국어](../badges/lang/ko/outline.svg) ![Español](../badges/lang/es/outline.svg) ![Tiếng Việt](../badges/lang/vi/outline.svg) ![العربية](../badges/lang/ar/outline.svg) ![Français](../badges/lang/fr/outline.svg) |

## Các phiên bản được hỗ trợ

Tất cả 53 phiên bản từ Hướng dẫn môi trường thực thi của Khung chuẩn Chính phủ điện tử:

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`, `5.0.7`
- **4.x**: `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x**: `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x**: `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x**: `1.0`, `1.0.0`

## Thêm phiên bản và tạo huy hiệu

Để thêm phiên bản mới, chỉnh sửa `versions.json` và chạy trình tạo (phiên bản của chính dự án do script nêu ở trên phát hiện):

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

## Thiết kế

- SVG được commit và phục vụ qua URL raw của GitHub. Trình render README tải chúng trực tiếp; không cần máy chủ triển khai.
- Nguồn logo duy nhất tại `assets/egovframe-mark.svg`. Tất cả huy hiệu tạo ra nhúng logo — không phụ thuộc hình ảnh bên ngoài.
- Phiên bản và kiểu dáng được cố định trong đường dẫn tệp để các huy hiệu README hiện có không thay đổi bất ngờ khi có bản phát hành mới.
- `scripts/generate.py --check` và CI kiểm tra đầu ra tạo ra khớp với nguồn. Thay đổi kiểu dáng áp dụng nhất quán cho tất cả các phiên bản.
- Kiểu `plastic` sử dụng các dừng gradient gloss giống như shields.io. `for-the-badge` sử dụng góc vuông (`rx="0"`) giống như shields.io.

Logo được trích xuất từ huy hiệu README hiện có của eGovFramework. Quyền logo và tên Khung chuẩn Chính phủ điện tử thuộc về chủ sở hữu tương ứng.

## Giấy phép

Mã (script tạo, tests, workflows) có [giấy phép MIT](../LICENSE). Tài sản logo (`assets/egovframe-mark.svg`) và logo nhúng trong các huy hiệu tạo ra **không** nằm trong phạm vi giấy phép này và thuộc về chủ sở hữu gốc như đã nêu ở trên.