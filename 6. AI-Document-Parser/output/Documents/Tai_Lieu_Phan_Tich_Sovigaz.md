**TÀI LIỆU PHÂN TÍCH DỮ LIỆU CÔNG TY SOVIGAZ**

**I. GIỚI THIỆU CÔNG TY SOVIGAZ**

Công ty Cổ phần Hơi Kỹ nghệ Que Hàn (SOVIGAZ) là doanh nghiệp hàng đầu tại Việt Nam trong lĩnh vực sản xuất và cung cấp khí công nghiệp, khí y tế, que hàn điện và hóa chất. Được thành lập vào năm 1974, SOVIGAZ có tiền thân là sự hợp nhất giữa Phân khu Việt Nam S.O.A.E.O và Công ty Việt Nam Hơi Kỹ nghệ .​

SOVIGAZ chuyên sản xuất và kinh doanh:

- Khí công nghiệp và khí y tế
- Que hàn điện và hóa chất
- Dịch vụ vận chuyển, lắp đặt hệ thống khí công nghiệp và khí y tế
- Kiểm tra kỹ thuật bồn chứa khí áp lực cao

**II. TỔNG QUAN DỰ ÁN**

**1. Tổng quan dự án**

- **Tên dự án** : Hệ thống kho dữ liệu doanh nghiệp Sovigaz
- **Mục tiêu** : Xây dựng hệ thống kho dữ liệu (Data Warehouse) nhằm chuẩn hóa, lưu trữ, tích hợp và khai thác dữ liệu từ các nguồn khác nhau, đồng thời phục vụ cho các báo cáo phân tích kinh doanh.

**2. Kiến trúc hệ thống**

- **Nguồn dữ liệu** : Phần mềm kế toán MISA, Excel
- **Hệ DBMS** : SQL Server
- **ETL** : SSIS (SQL Server Integration Services)
- **Báo cáo** : Power BI

**3. Quy trình xây dựng**

- **Giai đoạn 1: Khảo sát nguồn dữ liệu**
    - Phân tích cấu trúc dữ liệu từ MISA Dev
    - Xác định các bảng nguồn có giá trị khai thác
- **Giai đoạn 2: Thiết kế kho dữ liệu (DWH)**
    - Mô hình sao (Star Schema)
    - Bao gồm các Dimension: Dim\_Date, Dim\_Customer, Dim\_Product, Dim\_Employee...
    - Các Fact: Fact\_Revenue, Fact\_Debt, Fact\_KPI
- **Giai đoạn 3: Xây dựng ETL với SSIS trên môi trường Dev**
    - ETL đổ dữ liệu từ MISA Dev và Excel vào kho DWH
- **Giai đoạn 4: Xây dựng báo cáo với Power BI**
    - Kết nối trực tiếp từ DWH
    - Xây dựng báo cáo PowerBI
    - Đối soát số liệu với Sovigaz
- **Giai đoạn 5: GoLive**
    - ETL đổ dữ liệu từ MISA Live và Excel vào kho DWH
    - Tạo gói SSIS tự động đổ dữ liệu từ MISA vào kho DWH
    - Thiết lập lịch chạy theo ngày/tuần
- **Giai đoạn 6: Truyền dữ liệu từ PBI về Excel**
    - Thiết kế file truyền dữ liệu từ PBI về Excel cho phù hợp với mong muốn của KH.

**4. Hệ thống báo cáo**

- **Tổng hợp doanh thu**
    - Biểu đồ theo thời gian (năm/tháng/ngày)
    - So sánh theo các đặc tính như: chi nhánh, nhóm sản phẩm, loại sản phẩm,...
- **Chi tiết nguồn doanh thu**
    - Phân tích theo loại hàng, khách hàng, kênh bán hàng, chi nhánh
- **Chi tiết công nợ**
    - Dòng tiền theo khách hàng, tuổi nợ, loại nợ
- **Tổng hợp KPI**
    - Biểu đồ theo thời gian
    - KPI doanh thu theo chi nhánh, nhóm sản phẩm, chỉ tiêu
- **Chi tiết KPI**
    - Chi tiết KPI doanh thu theo chi nhánh, nhóm sản phẩm, theo thời gian,...

**5. Kế hoạch triển khai tiếp theo**

- Hoàn thiện dự án, khớp số liệu với Sovigaz

**Người thực hiện** : Đặng Anh Tùng

**Thời gian** : 18/04/2025