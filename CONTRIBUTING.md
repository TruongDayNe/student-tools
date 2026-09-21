# Contributing to Student Tools

Cảm ơn bạn đã đóng góp cho Student Tools. Dự án dùng quy trình đơn giản gần với một repository mã nguồn mở thực tế.

## Quy trình đề xuất

1. Đọc hoặc tạo Issue mô tả rõ việc cần làm.
2. Fork repository và thêm repository chính làm `upstream`.
3. Tạo branch từ `main`, không làm việc trực tiếp trên `main`.
4. Viết test cho thay đổi mới và cập nhật documentation khi cần.
5. Tạo các commit nhỏ, có nội dung rõ ràng.
6. Push branch lên fork và mở Pull Request liên kết với Issue.
7. Nhờ ít nhất một contributor khác review trước khi merge.

```bash
git remote add upstream <original-repository-url>
git switch -c feature/temperature-converter
PYTHONPATH=src python -m unittest discover -s tests -v
git push -u origin feature/temperature-converter
```

## Quy ước branch

- `feature/<short-description>` cho tính năng mới.
- `fix/<short-description>` cho sửa lỗi.
- `docs/<short-description>` cho documentation.
- `test/<short-description>` cho test.

## Commit và Pull Request

Dùng commit message ngắn, mô tả đúng thay đổi, ví dụ:

- `feat: add temperature converter`
- `fix: handle division by zero`
- `test: add validator cases`
- `docs: explain converter usage`

Pull Request cần nêu rõ Issue liên quan, thay đổi chính và cách kiểm thử. Reviewer kiểm tra tối thiểu: code dễ đọc, test pass, documentation được cập nhật và không có thay đổi ngoài phạm vi.

