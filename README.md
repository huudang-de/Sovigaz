# 📊 Dự án Kho Dữ Liệu Doanh Nghiệp SOVIGAZ

## 1. Giới thiệu chung
Dự án xây dựng hệ thống **Kho dữ liệu (Data Warehouse)** cho Công ty Cổ phần Hơi Kỹ nghệ Que Hàn (SOVIGAZ). 
Mục tiêu chính là chuẩn hóa, lưu trữ, tích hợp và khai thác dữ liệu từ các nguồn khác nhau (phần mềm kế toán MISA, file Excel) để phục vụ cho các báo cáo phân tích kinh doanh quản trị trên **Power BI**.

**Kiến trúc hệ thống:**
- **Nguồn dữ liệu:** MISA Cloud (MSSQL), MISA AMIS (API/Excel), File Excel.
- **Lưu trữ & Xử lý (ETL):** Python (Extract), SQL Server & SSIS (Transform & Load).
- **Trực quan hóa (BI):** Power BI.

---

## 2. Cấu trúc thư mục (Repository Structure)

Dự án được quy hoạch bài bản theo vòng đời phát triển phần mềm/dữ liệu:

- 📂 **`1. Giới thiệu và khảo sát dự án/`**
  - Chứa tài liệu khảo sát ban đầu và đánh giá hiện trạng hệ thống dữ liệu Sovigaz.
  - *(Lưu ý: Thư mục chứa dữ liệu thô đã được thiết lập `.gitignore` để ẩn khỏi GitHub nhằm đảm bảo bảo mật).*

- 📂 **`2. Tài liệu phân tích và thiết kế/`**
  - Chứa thiết kế tổng thể, sơ đồ kiến trúc luồng dữ liệu, thiết kế mô hình dữ liệu (ERD) và các tài liệu Yêu cầu nghiệp vụ (BRD).

- 📂 **`3. Phát triển ETL dữ liệu/`**
  - Nơi lưu trữ mã nguồn ETL.
  - Hiện chứa các script Python dùng để Extract dữ liệu từ các nguồn thô.

- 📂 **`4. Phát triển báo cáo/`**
  - Không gian làm việc cho các file thiết kế Dashboard (Power BI, Template).

- 📂 **`5. Kiểm thử/`**
  - Chứa kịch bản và dữ liệu đối soát cho Kiểm thử tích hợp (SIT) và Nghiệm thu (UAT).

- 🤖 **`AI-Document-Parser/`**
  - Bộ công cụ (Script) hỗ trợ tự động bóc tách tài liệu (Word, Excel) sang định dạng Markdown (`.md`).
  - Hỗ trợ rút trích nhanh các yêu cầu nghiệp vụ để AI và Data Engineer dễ dàng đọc hiểu mà không cần mở file gốc.

---

## 3. Hướng dẫn sử dụng AI-Document-Parser
Nếu bạn cần bóc tách tài liệu (VD: BRD) sang Markdown:

1. Di chuyển vào thư mục Parser:
   ```bash
   cd AI-Document-Parser
   ```
2. Kích hoạt môi trường ảo:
   ```bash
   .\venv\Scripts\activate
   ```
3. Chạy script tương ứng trong thư mục `scripts/`.

---

## 4. Ghi chú & Bảo mật
- Tất cả các file dữ liệu nhạy cảm thực tế (`.csv`, `.xlsx` trong folder Nguồn dữ liệu) **đều bị cấm commit** lên kho lưu trữ.
- Mọi đóng góp (commit) cần tuân thủ quy trình kiểm tra bảo mật dữ liệu trước khi đẩy lên nhánh `main`.

---
*Developed & Maintained by [huudang-de](https://github.com/huudang-de)*
