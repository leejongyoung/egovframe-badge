# Huy hiệu eGovFrame

[![English](../badges/lang/en/outline.svg)](README.en.md)
[![한국어](../badges/lang/ko/outline.svg)](README.ko.md)
[![Español](../badges/lang/es/outline.svg)](README.es.md)
[![Tiếng Việt](../badges/lang/vi/flat.svg)](README.vi.md)
[![العربية](../badges/lang/ar/outline.svg)](README.ar.md)
[![Français](../badges/lang/fr/outline.svg)](README.fr.md)

Một **huy hiệu SVG đơn lẻ** cho mọi dự án sử dụng eGovFrame (khung điện tử chính phủ). Thay vì nhúng logo vào từng kho, hãy tham chiếu một huy hiệu được quản lý tập trung với một URL raw. SVG tĩnh — không cần JavaScript, không cần máy chủ triển khai, không cần URL Base64 dài.

## Sử dụng trong một dòng

Chọn phiên bản, kiểu dáng và ngôn ngữ (`en`, `ko`, `es`, `vi`, `ar`, `fr`) từ đường dẫn URL. Các ví dụ dưới đây liên kết đến cổng chính thức.

**Tiếng Anh (`eGovFrame`)**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**Tiếng Hàn (`전자정부표준프레임워크`)**
```md
[![전자정부표준프레임워크 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-ko.svg)](https://www.egovframe.go.kr)
```

**Huy hiệu phiên bản đa ngôn ngữ (`es` Tây Ban Nha · `vi` Việt Nam · `ar` Ả Rập · `fr` Pháp)**
```md
[![Marco Estándar eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![Khung chuẩn eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![إطار eGovFrame القياسي 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
[![Cadre standard eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(Tất cả huy hiệu đa ngôn ngữ đều hỗ trợ cả hai đường dẫn `badges/5.0.2/flat-<lang>.svg` và `badges/5.0.2/<lang>/flat.svg`.)*

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

Tất cả các phiên bản chính từ [eGovFrame Runtime Guide](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — từ 1.0 đến 5.x (tổng cộng 52 phiên bản) — với năm kiểu dáng mỗi loại: `flat`, `flat-square`, `plastic`, `for-the-badge` và kiểu tùy chỉnh `outline` (kiểu `social` của shields.io bị loại vì phụ thuộc vào hiệu ứng hover).

| Kiểu dáng | Ví dụ (Tiếng Anh) | Ví dụ (Tiếng Hàn) |
| --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (Tiếng Hàn)](../badges/5.0.1/flat-ko.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (Tiếng Hàn)](../badges/5.0.1/flat-square-ko.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (Tiếng Hàn)](../badges/5.0.1/plastic-ko.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (Tiếng Hàn)](../badges/5.0.1/for-the-badge-ko.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (Tiếng Hàn)](../badges/5.0.1/outline-ko.svg) |

## Các phiên bản được hỗ trợ

Tất cả 52 phiên bản từ Hướng dẫn Thời gian Chạy eGovFrame:

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`
- **4.x**: `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x**: `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x**: `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x**: `1.0`, `1.0.0`

## Thêm phiên bản và tạo huy hiệu

Chọn phiên bản phù hợp với khung của bạn. Huy hiệu này **không** tự động phát hiện phiên bản dự án. Để thêm phiên bản mới, chỉnh sửa `versions.json` và chạy trình tạo:

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

Logo được trích xuất từ huy hiệu README hiện có của eGovFramework. Quyền logo và tên eGovFrame thuộc về chủ sở hữu tương ứng.

## Giấy phép

Mã (script tạo, tests, workflows) có [giấy phép MIT](../LICENSE). Tài sản logo (`assets/egovframe-mark.svg`) và logo nhúng trong các huy hiệu tạo ra **không** nằm trong phạm vi giấy phép này và thuộc về chủ sở hữu gốc như đã nêu ở trên.