# Chính sách bảo mật

[![English](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/en/outline.svg)](SECURITY.en.md)
[![한국어](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/ko/outline.svg)](SECURITY.ko.md)
[![Español](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/es/outline.svg)](SECURITY.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/vi/flat.svg)](SECURITY.vi.md)
[![العربية](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/ar/outline.svg)](SECURITY.ar.md)
[![Français](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/fr/outline.svg)](SECURITY.fr.md)

## Báo cáo lỗ hổng

**Vui lòng không mở issue công khai cho vấn đề bảo mật.**

Hãy sử dụng báo cáo lỗ hổng riêng tư của GitHub:

➡ <https://github.com/egovframework/egovframe-badge/security/advisories/new>

Nếu báo cáo lỗ hổng riêng tư không được bật trên kho, hãy liên hệ riêng với người bảo trì qua thông tin liên hệ trên hồ sơ GitHub của chủ sở hữu kho thay vì mở issue công khai.

Vui lòng bao gồm:

- thứ gì bị ảnh hưởng (phiên bản badge, script tạo, hoặc workflow)
- cách tái hiện và tác động kỳ vọng
- bất cứ điều gì bạn đã làm để xác minh (hashes, URLs, logs)

Các báo cáo được xử lý riêng cho đến khi có bản sửa lỗi; ghi nhận đóng góp theo yêu cầu.

## Phạm vi

Trong phạm vi:

- Badge SVGs trong [`badges/`](../../badges/): nội dung tạo, logo nhúng, siêu dữ liệu phiên bản
- Tự động hóa: [`.github/workflows/`](../../.github/workflows/) và [`scripts/`](../../scripts/). Badge mới được tạo bởi workflow `generate-badges`; cách làm cho bước đó tạo ra đầu ra sai, rò rỉ token, hoặc chạy đầu vào không tin cậy được coi là lỗ hổng.

Ngoài phạm vi, báo cáo cho chủ sở hữu:

- Framework eGovFrame và máy chủ tải xuống → dự án eGovFrame, <https://www.egovframe.go.kr/> và [eGovFramework](https://github.com/eGovFramework).
- GitHub bản thân → <https://github.com/github/github/security/policy>.
- shields.io → <https://github.com/badges/shields/security/policy>.

## Các phiên bản được hỗ trợ

Chỉ những gì ở `badges/` trên nhánh mặc định được duy trì: tất cả phiên bản liệt kê trong `versions.json`. Badge bị xóa khi bản vá mới hơn của cùng series đến không được duy trì.

## Xác minh badge tự thân

Mỗi badge là SVG độc lập với logo nhúng. Để kiểm tra mọi badge đã commit khớp với đầu ra của trình tạo:

```bash
python3 scripts/generate.py --check
```