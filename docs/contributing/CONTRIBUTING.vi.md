# Hướng dẫn đóng góp cho huy hiệu Khung chuẩn Chính phủ điện tử

[![English](../../badges/lang/en/outline.svg)](CONTRIBUTING.en.md)
[![한국어](../../badges/lang/ko/outline.svg)](CONTRIBUTING.ko.md)
[![Español](../../badges/lang/es/outline.svg)](CONTRIBUTING.es.md)
[![Tiếng Việt](../../badges/lang/vi/flat.svg)](CONTRIBUTING.vi.md)
[![العربية](../../badges/lang/ar/outline.svg)](CONTRIBUTING.ar.md)
[![Français](../../badges/lang/fr/outline.svg)](CONTRIBUTING.fr.md)

## Trước khi mở pull request

```bash
python3 -m pip install PyYAML==6.0.3
python3 -m unittest discover -s tests -v   # kiểm tra các script
```

CI chạy các bài kiểm tra và kiểm tra tính nhất quán của việc tạo badge.

- Thông điệp commit tuân theo phong cách hiện có: `feat(badges): add 5.1.0 badges`, `fix(generate): ...`, `docs(readme): ...`, `ci: ...`.
- Không chỉnh sửa trực tiếp các tệp SVG đã tạo. Các phiên bản mới đến từ `scripts/generate.py` (workflow `generate-badges`); để kiểm tra lại các badge hiện có, chạy `python3 scripts/generate.py --check`.
- Một bộ badge cho mỗi phiên bản: thêm `5.1.0` sẽ tạo ra 5 kiểu × 6 ngôn ngữ.
- Các tệp điểm vào của tài liệu được tạo tự động: chỉnh sửa nguồn trong `docs/`, rồi chạy `python3 scripts/sync_readme.py` để cập nhật `README.md` và các tệp trong `.github/`. Nút ngôn ngữ phải trỏ tới nguồn đã bản địa hóa trong `docs/`, kể cả tiếng Anh.

## GitHub Actions và thanh toán

- **Miễn phí trên kho công khai:** theo chính sách thanh toán của GitHub, các runner tiêu chuẩn được GitHub lưu trữ (`ubuntu-latest`) **miễn phí và không giới hạn phút trên kho công khai**. Các badge được tạo trong `generate-badges.yml` và được commit; không tiêu thụ artifacts Actions hay bộ nhớ Release.

## Bảo mật

Đừng báo cáo lỗ hổng bảo mật trong issues; hãy làm theo quy trình trong [SECURITY.vi.md](../security/SECURITY.vi.md).