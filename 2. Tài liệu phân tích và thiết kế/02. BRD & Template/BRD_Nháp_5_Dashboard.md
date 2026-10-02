# BRD NHÁP - 5 DASHBOARD SOVIGAZ
> AI Agent tự phân tích từ Data Schema + UI Template. Cần xác nhận nghiệp vụ trước khi triển khai.
> **Ghi chú chung:** Xây dựng báo cáo trên hệ thống báo cáo tập trung Power BI.

---

# BRD 1: BÁO CÁO DOANH THU CÔNG TY (Tổng Quan)

## 1. Mục đích báo cáo
- Báo cáo doanh thu của công ty

## 2. Nội dung báo cáo

### 2.1. Nguồn dữ liệu

| STT | Nguồn dữ liệu | Mô tả luồng xử lý | Thời gian Data sẵn sàng | Thời điểm lấy dữ liệu |
| --- | --- | --- | --- | --- |
| 1.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_By_Product.csv` - Dữ liệu KPI theo Sản phẩm (Doanh thu thực tế) | 9h30 AM | Từ năm 2018 đến hiện tại |
| 2.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_Month.csv` - Dữ liệu KPI theo Tháng (dùng cho Chart theo tháng) | 9h30 AM | Từ năm 2018 đến hiện tại |
| 3.0 | Phần mềm kế toán MISA AMIS | `Dim_customer/*.xlsx` (UNION 9 XN: BD, BH, CT, HP, KH, NT, PR, TK, VP, VP2) | 9h30 AM | Từ năm 2018 đến hiện tại |
| 4.0 | Phần mềm kế toán MISA Cloud | `Dim_Stock.csv`, `Dim_ParentStock.csv` - Danh mục Kho / Chi nhánh | 9h30 AM | Từ năm 2018 đến hiện tại |
| 5.0 | Phần mềm kế toán MISA Cloud | `Dim_ProductCategories.csv` - Danh mục Nhóm sản phẩm | 9h30 AM | Từ năm 2018 đến hiện tại |
| 6.0 | Static Data | `Dim_Date.csv` - Bảng lịch | Tĩnh | Từ năm 2018 đến hiện tại |

### 2.2. Điều kiện ràng buộc xuyên suốt báo cáo

| STT | Điều kiện | Mô tả | Note |
| --- | --- | --- | --- |
| 1 | Phân biệt Doanh thu bán ngoài vs LCNB | Lọc theo cột `Nhóm KH, NCC` trong Dim_customer: NB = Nội bộ (LCNB), còn lại = Bán ngoài | ⚠️ CẦN XÁC NHẬN: Fact_KPI_By_Product có cột join sang Dim_customer không? |
| 2 | Phạm vi dữ liệu | Chỉ lấy dữ liệu từ file `131.xlsx` (TK Phải thu KH) cho phần công nợ nếu có | |
| 3 | Đơn vị tiền tệ | VNĐ | |

### 2.3. Filter báo cáo

| STT | Bộ lọc | Mô tả | Giá trị mẫu/Định dạng | Đặc tính |
| --- | --- | --- | --- | --- |
| 1 | Date (Khoảng thời gian) | Lọc theo khoảng ngày phát sinh doanh thu | `2022-01-01` đến `2023-01-01` | All |
| 2 | Tên khách hàng | Lọc theo tên khách hàng cụ thể | Dropdown / Search | All |
| 3 | Tên nhóm khách hàng | Lọc theo mã nhóm KH (`Nhóm KH, NCC`) | Dropdown | All |
| 4 | Tên xí nghiệp | Lọc theo chi nhánh/xí nghiệp (`ParentStockName`) | Dropdown | All |
| 5 | Tìm tên sản phẩm | Tìm kiếm theo tên sản phẩm (`ProductName`, `CategoryName`) | Search | All |

### 2.4. Chi tiết các trường dữ liệu (Metrics/Dimensions)

| STT | Chỉ tiêu | Mô tả/Cách tính | Loại dữ liệu | Đơn vị | Biểu đồ | Note |
| --- | --- | --- | --- | --- | --- | --- |
| **CARD** | | | | | | |
| 1 | Doanh thu bán ngoài | `SUM(Fact_KPI_By_Product[Amount])` WHERE `Dim_customer[Nhóm KH, NCC] <> "NB"` | Decimal | VNĐ | Card | ⚠️ Cần xác nhận key join |
| 2 | Doanh thu LCNB | `SUM(Fact_KPI_By_Product[Amount])` WHERE `Dim_customer[Nhóm KH, NCC] = "NB"` | Decimal | VNĐ | Card | ⚠️ Cần xác nhận key join |
| 3 | Tổng đơn hàng | `DISTINCTCOUNT(Fact_KPI_By_Product[RevenueCode])` | Integer | Đơn | Card | |
| 4 | Giá trị TB đơn hàng | `DIVIDE([Doanh thu bán ngoài], [Tổng đơn hàng])` | Decimal | VNĐ | Card | |
| **CHART** | | | | | | |
| 5 | Doanh thu theo tháng | `SUM(Fact_KPI_Month[Amount])` GROUP BY `Date` (tháng) | Decimal | VNĐ | Line & Stacked Column | ⚠️ Dùng Fact_KPI_Month vì KPI_By_Product không có Date tháng |
| 6 | Số đơn hàng theo tháng | `COUNT(RevenueCode)` GROUP BY tháng | Integer | Đơn | Line & Stacked Column | |
| 7 | Doanh thu theo nhóm vật tư | `SUM(Amount)` GROUP BY `CategoryName` | Decimal | VNĐ | Stacked Column | |
| 8 | Doanh thu theo nhóm KH | `SUM(Amount)` GROUP BY `Nhóm KH, NCC` | Decimal | VNĐ | Clustered Column + Pie | |
| 9 | Tỷ lệ đóng góp DT theo nhóm KH | `[DT nhóm KH] / [Tổng DT]` | Decimal | % | Pie | |
| 10 | Doanh thu theo xí nghiệp | `SUM(Amount)` GROUP BY `ParentStockName` | Decimal | VNĐ | Stacked Column + Pie | |
| 11 | Tỷ lệ đóng góp DT theo XN | `[DT XN] / [Tổng DT]` | Decimal | % | Pie | |

---

# BRD 2: BÁO CÁO DOANH THU CHI TIẾT SOVIGAZ

## 1. Mục đích báo cáo
- Báo cáo doanh thu chi tiết Sovigaz

## 2. Nội dung báo cáo

### 2.1. Nguồn dữ liệu

| STT | Nguồn dữ liệu | Mô tả luồng xử lý | Thời gian Data sẵn sàng | Thời điểm lấy dữ liệu |
| --- | --- | --- | --- | --- |
| 1.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_By_Product.csv` - Chi tiết doanh thu theo từng sản phẩm, hóa đơn | 9h30 AM | Từ năm 2018 đến hiện tại |
| 2.0 | Phần mềm kế toán MISA AMIS | `Dim_customer/*.xlsx` (UNION 9 XN) - Thông tin khách hàng, nhóm KH | 9h30 AM | Từ năm 2018 đến hiện tại |
| 3.0 | Phần mềm kế toán MISA Cloud | `Dim_ParentStock.csv` - Danh mục Chi nhánh/Xí nghiệp | 9h30 AM | Từ năm 2018 đến hiện tại |

### 2.2. Điều kiện ràng buộc xuyên suốt báo cáo

| STT | Điều kiện | Mô tả | Note |
| --- | --- | --- | --- |
| 1 | Phân cấp khách hàng theo XN | Tên KH được phân nhóm theo mã XN (VP, CT, BD...) như trong UI mẫu | Xem ví dụ: Nhóm VP gồm {Trung tâm y tế Tuy Phong, Công ty TNHH ABC} |
| 2 | Pivot nhóm KH | Phân loại DT theo 4 nhóm: A_BV/YTE, B_CTY/ĐL, C_NLE, Nhóm KH khác | ⚠️ CẦN XÁC NHẬN: mapping mã `BV, ĐL, NL` sang tên nhóm |
| 3 | Thuế VAT | ⚠️ CHƯA TÌM THẤY trong Data Schema | Cần bổ sung nguồn dữ liệu |

### 2.3. Filter báo cáo

| STT | Bộ lọc | Mô tả | Giá trị mẫu/Định dạng | Đặc tính |
| --- | --- | --- | --- | --- |
| 1 | Thời gian | Lọc theo tháng/năm | Dropdown (tháng/năm) | All |
| 2 | Xí nghiệp | Lọc theo chi nhánh | Dropdown | All |
| 3 | Khách hàng | Tìm kiếm tên KH | Search | All |
| 4 | Nhóm KH | Lọc theo mã nhóm KH | Dropdown | All |
| 5 | Số hóa đơn | Tìm theo số hóa đơn | Search | ⚠️ Giả định = `RevenueCode`, CẦN XÁC NHẬN |
| 6 | Tìm tên KH | Tìm nhanh theo tên | Search | All |

### 2.4. Chi tiết các trường dữ liệu (Metrics/Dimensions)

| STT | Chỉ tiêu | Mô tả/Cách tính | Loại dữ liệu | Đơn vị | Biểu đồ | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Mặt hàng | `ProductName` từ `Fact_KPI_By_Product` | Text | - | Table | |
| 2 | Số lượng | `SUM(SaleQuantityDVC)` | Decimal | ĐVC | Table | |
| 3 | Doanh thu theo mặt hàng | `SUM(Amount)` GROUP BY `ProductName` | Decimal | VNĐ | Table | |
| 4 | Tên KH | `Tên khách hàng` từ `Dim_customer` | Text | - | Table | |
| 5 | Doanh thu theo KH | `SUM(Amount)` GROUP BY `Tên khách hàng` | Decimal | VNĐ | Table | |
| 6 | Số hóa đơn | `RevenueCode` | Text | - | Table | ⚠️ CẦN XÁC NHẬN đây có đúng là số hóa đơn không |
| 7 | Thuế VAT | Chưa xác định nguồn | Decimal | VNĐ | Table | ⚠️ CHƯA CÓ DATA |
| 8 | DT nhóm A (BV/YTE) | `SUM(Amount)` WHERE `Nhóm KH = "BV"` | Decimal | VNĐ | Table (Pivot) | |
| 9 | DT nhóm B (CTY/ĐL) | `SUM(Amount)` WHERE `Nhóm KH IN {"ĐL","CT"}` | Decimal | VNĐ | Table (Pivot) | |
| 10 | DT nhóm C (NLE) | `SUM(Amount)` WHERE `Nhóm KH = "NL"` | Decimal | VNĐ | Table (Pivot) | |
| 11 | DT nhóm KH khác | `SUM(Amount)` WHERE `Nhóm KH NOT IN {BV, ĐL, CT, NL}` | Decimal | VNĐ | Table (Pivot) | |

---

# BRD 3: BÁO CÁO CÔNG NỢ SOVIGAZ

## 1. Mục đích báo cáo
- Báo cáo công nợ Sovigaz

## 2. Nội dung báo cáo

### 2.1. Nguồn dữ liệu

| STT | Nguồn dữ liệu | Mô tả luồng xử lý | Thời gian Data sẵn sàng | Thời điểm lấy dữ liệu |
| --- | --- | --- | --- | --- |
| 1.0 | Phần mềm kế toán MISA AMIS | `Fact_AnalyticsDebit/131.xlsx` (TK Phải thu KH) - Phân tích tuổi nợ hiện tại | 9h30 AM | Snapshot tại thời điểm xuất |
| 2.0 | Phần mềm kế toán MISA AMIS | `Dim_customer/*.xlsx` (UNION 9 XN) - Thông tin nhóm KH | 9h30 AM | Từ năm 2018 đến hiện tại |
| 3.0 | ⚠️ CHƯA XÁC ĐỊNH | Sổ chi tiết TK131 (đầu kỳ, phát sinh, đã TT) | - | ⚠️ CẦN BỔ SUNG NGUỒN DATA |

### 2.2. Điều kiện ràng buộc xuyên suốt báo cáo

| STT | Điều kiện | Mô tả | Note |
| --- | --- | --- | --- |
| 1 | Chỉ lấy TK 131 | Công nợ khách hàng bên ngoài, loại trừ TK 136x (nội bộ) | Có thể bổ sung filter "Loại nợ" để xem TK khác |
| 2 | Gom nhóm tuổi nợ | Điều chỉnh 7 dải nợ của MISA về 3 dải hiển thị trên biểu đồ: 0-30, 30-90, 90+ | |
| 3 | ⚠️ 4 Card cần xác nhận | `Đầu kỳ`, `Phát sinh`, `Đã TT`, `Còn lại` chưa có nguồn data tương ứng | CẦN FILE SỔ CHI TIẾT CÔNG NỢ THEO KỲ |

### 2.3. Filter báo cáo

| STT | Bộ lọc | Mô tả | Giá trị mẫu/Định dạng | Đặc tính |
| --- | --- | --- | --- | --- |
| 1 | Loại nợ | Lọc theo mã tài khoản kế toán | Dropdown (131, 136, 1388...) | All |
| 2 | Nợ trước hạn | Lọc KH có nợ trước hạn | Dropdown | All |
| 3 | Nợ quá hạn | Lọc KH có nợ quá hạn | Dropdown | All |
| 4 | Nhóm khách hàng | Lọc theo mã nhóm KH | Dropdown | All |
| 5 | Tên khách hàng | Tìm kiếm theo tên | Search | All |

### 2.4. Chi tiết các trường dữ liệu (Metrics/Dimensions)

| STT | Chỉ tiêu | Mô tả/Cách tính | Loại dữ liệu | Đơn vị | Biểu đồ | Note |
| --- | --- | --- | --- | --- | --- | --- |
| **CARD** | | | | | | |
| 1 | Số nợ đầu kỳ | Số dư nợ đầu kỳ | Decimal | VNĐ | Card | ⚠️ CHƯA CÓ DATA - Cần file sổ chi tiết |
| 2 | Số nợ phát sinh | Tổng nợ phát sinh trong kỳ | Decimal | VNĐ | Card | ⚠️ CHƯA CÓ DATA |
| 3 | Số nợ đã thanh toán | Tổng tiền KH đã trả trong kỳ | Decimal | VNĐ | Card | ⚠️ CHƯA CÓ DATA |
| 4 | Số nợ còn lại | `SUM(131[Tổng nợ])` | Decimal | VNĐ | Card | Đây là số dư cuối kỳ (snapshot) |
| **CHART** | | | | | | |
| 5 | Công nợ quá hạn 0-30 ngày | `SUM([Nợ quá hạn: 1-30 ngày])` | Decimal | VNĐ | Stacked Column | |
| 6 | Công nợ quá hạn 31-90 ngày | `SUM([31-90 ngày]) + SUM([91-180 ngày])` | Decimal | VNĐ | Stacked Column | |
| 7 | Công nợ quá hạn 90+ ngày | `SUM([181-365]) + SUM([366-730]) + SUM([731-1095]) + SUM([Trên 1095])` | Decimal | VNĐ | Stacked Column | |
| 8 | Nợ trước hạn | `SUM([Nợ trước hạn: Tổng])` | Decimal | VNĐ | Stacked Column | |
| 9 | Công nợ theo nhóm KH | `SUM([Tổng nợ])` GROUP BY `Nhóm KH, NCC` | Decimal | VNĐ | Clustered Column | |
| **TABLE** | | | | | | |
| 10 | Mã KH | `Mã khách hàng` | Text | - | Table | |
| 11 | Tên KH | `Tên khách hàng` | Text | - | Table | |
| 12 | Chi nhánh | `Địa chỉ` (XN theo file nguồn) | Text | - | Table | |
| 13 | Số nợ đầu kỳ | Xem card 1 | Decimal | VNĐ | Table | ⚠️ CHƯA CÓ DATA |
| 14 | Số nợ phát sinh trong kỳ | Xem card 2 | Decimal | VNĐ | Table | ⚠️ CHƯA CÓ DATA |
| 15 | Số tiền đã trả | Xem card 3 | Decimal | VNĐ | Table | ⚠️ CHƯA CÓ DATA |
| 16 | Số còn phải trả | `SUM([Tổng nợ])` | Decimal | VNĐ | Table | |
| 17 | Địa chỉ | `Địa chỉ` từ `Dim_customer` | Text | - | Table | |

---

# BRD 4: BÁO CÁO KPI SOVIGAZ (Tổng Quan)

## 1. Mục đích báo cáo
- Báo cáo KPI Sovigaz

## 2. Nội dung báo cáo

### 2.1. Nguồn dữ liệu

| STT | Nguồn dữ liệu | Mô tả luồng xử lý | Thời gian Data sẵn sàng | Thời điểm lấy dữ liệu |
| --- | --- | --- | --- | --- |
| 1.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_Year.csv` - KPI kế hoạch theo Năm & Chi nhánh | 9h30 AM | Từ năm 2018 đến hiện tại |
| 2.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_Month.csv` - KPI kế hoạch theo Tháng | 9h30 AM | Từ năm 2018 đến hiện tại |
| 3.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_By_Product.csv` - Doanh thu thực tế theo Sản phẩm | 9h30 AM | Từ năm 2018 đến hiện tại |
| 4.0 | Phần mềm kế toán MISA Cloud | `Fact_ActualProduction.csv` - Sản lượng sản xuất thực tế | 9h30 AM | Từ năm 2018 đến hiện tại |
| 5.0 | Phần mềm kế toán MISA Cloud | `Dim_ParentStock.csv`, `Dim_ProductCategories.csv` | 9h30 AM | Từ năm 2018 đến hiện tại |
| 6.0 | Static Data | `Dim_Date.csv` | Tĩnh | Từ năm 2018 đến hiện tại |

### 2.2. Điều kiện ràng buộc xuyên suốt báo cáo

| STT | Điều kiện | Mô tả | Note |
| --- | --- | --- | --- |
| 1 | Phân biệt Plan vs Actual | `Fact_KPI_Month` và `Fact_KPI_Year` = KPI kế hoạch. `Fact_KPI_By_Product`, `Fact_ActualProduction` = Thực tế | ⚠️ CẦN XÁC NHẬN |
| 2 | Phân biệt KPI SX vs KPI DT | Dùng cột `Indicator` trong `Fact_KPI_Month` để phân biệt (giá trị: DT, SX, TT...) | ⚠️ CẦN XÁC NHẬN giá trị thực của Indicator |
| 3 | Lũy kế (YTD) | Tính lũy kế từ đầu năm đến tháng được chọn | Cần `Dim_Date` đầy đủ |
| 4 | So sánh cùng kỳ (SPLY) | So sánh với cùng kỳ năm trước | Cần `Dim_Date` đầy đủ |

### 2.3. Filter báo cáo

| STT | Bộ lọc | Mô tả | Giá trị mẫu/Định dạng | Đặc tính |
| --- | --- | --- | --- | --- |
| 1 | Thời gian | Lọc theo tháng/năm | Dropdown (tháng/năm) | All |
| 2 | Sản phẩm | Lọc theo nhóm sản phẩm | Dropdown | All |
| 3 | Tên xí nghiệp | Lọc theo chi nhánh | Dropdown | All |

### 2.4. Chi tiết các trường dữ liệu (Metrics/Dimensions)

| STT | Chỉ tiêu | Mô tả/Cách tính | Loại dữ liệu | Đơn vị | Biểu đồ | Note |
| --- | --- | --- | --- | --- | --- | --- |
| **CARD - KPI THEO NĂM** | | | | | | |
| 1 | Kế hoạch sản xuất năm | `SUM(Fact_KPI_Year[Production])` WHERE Year = Năm chọn | Decimal | ĐVC | Card | ⚠️ Cần cột Indicator phân biệt SX vs DT |
| 2 | % hoàn thành KHSX năm | `SUM(Fact_ActualProduction[ProductQuantityDVC]) / [KHSX năm]` | Decimal | % | Card | |
| 3 | Kế hoạch doanh thu năm | `SUM(Fact_KPI_Year[Amount])` WHERE Year = Năm chọn | Decimal | VNĐ | Card | ⚠️ Cần cột Indicator phân biệt SX vs DT |
| 4 | % hoàn thành KHDT năm | `SUM(Fact_KPI_By_Product[Amount] YTD) / [KHDT năm]` | Decimal | % | Card | |
| **CARD - CHỈ SỐ THEO THÁNG** | | | | | | |
| 5 | KPI doanh thu tháng | `SUM(Fact_KPI_Month[Amount])` WHERE Indicator=DT, tháng chọn | Decimal | VNĐ | Card | ⚠️ CẦN XÁC NHẬN Indicator |
| 6 | Doanh thu thực tế tháng | `SUM(Fact_KPI_By_Product[Amount])` lọc tháng | Decimal | VNĐ | Card | ⚠️ KPI_By_Product chỉ có Year, không có Date tháng |
| 7 | Tỷ lệ HT KPI doanh thu | `[DT thực tế tháng] / [KPI DT tháng]` | Decimal | % | Card | |
| 8 | KPI giá trị sản xuất | `SUM(Fact_KPI_Month[ProductionValue])` WHERE Indicator=SX | Decimal | VNĐ | Card | |
| 9 | Giá trị sản xuất thực tế | `SUM(Fact_ActualProduction[ProductValue])` lọc tháng | Decimal | VNĐ | Card | |
| 10 | % giá trị sản xuất | `[GTSX thực tế] / [KPI GTSX]` | Decimal | % | Card | |
| **CARD - LŨY KẾ** | | | | | | |
| 11 | Lũy kế doanh thu (YTD) | `CALCULATE(SUM(Amount), DATESYTD(Dim_Date[Date]))` | Decimal | VNĐ | Card | ⚠️ Cần Fact có cột Date theo tháng |
| 12 | DT cùng kỳ năm trước | `CALCULATE(SUM(Amount), SAMEPERIODLASTYEAR(Dim_Date[Date]))` | Decimal | VNĐ | Card | ⚠️ Cần Fact có cột Date theo tháng |
| 13 | % DT so với cùng kỳ | `[Lũy kế DT] / [DT cùng kỳ] - 1` | Decimal | % | Card | |
| 14 | Lũy kế GTSX | `CALCULATE(SUM(ProductValue), DATESYTD())` | Decimal | VNĐ | Card | |
| 15 | GTSX cùng kỳ năm trước | `CALCULATE(SUM(ProductValue), SAMEPERIODLASTYEAR())` | Decimal | VNĐ | Card | |
| 16 | % GTSX so với cùng kỳ | `[Lũy kế GTSX] / [GTSX cùng kỳ] - 1` | Decimal | % | Card | |
| **CHART** | | | | | | |
| 17 | DT và KPI theo tháng | `[DT thực tế]` vs `[KPI DT]` GROUP BY tháng | Decimal | VNĐ | Clustered Column | |
| 18 | DT và KPI theo chi nhánh | `[DT thực tế]` vs `[KPI DT]` GROUP BY `ParentStockName` | Decimal | VNĐ | Line & Clustered Column | |
| 19 | Tỷ lệ đóng góp DT theo chi nhánh | `[DT XN] / [Tổng DT]` | Decimal | % | Pie | |
| 20 | DT và KPI theo nhóm sản phẩm | `[DT thực tế]` vs `[KPI DT]` GROUP BY `CategoryName` | Decimal | VNĐ | Clustered Column + Pie | |

---

# BRD 5: BÁO CÁO KPI CHI TIẾT SOVIGAZ

## 1. Mục đích báo cáo
- Báo cáo KPI chi tiết Sovigaz

## 2. Nội dung báo cáo

### 2.1. Nguồn dữ liệu

| STT | Nguồn dữ liệu | Mô tả luồng xử lý | Thời gian Data sẵn sàng | Thời điểm lấy dữ liệu |
| --- | --- | --- | --- | --- |
| 1.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_Year.csv` - KPI kế hoạch năm theo chi nhánh | 9h30 AM | Từ năm 2018 đến hiện tại |
| 2.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_Month.csv` - KPI kế hoạch tháng | 9h30 AM | Từ năm 2018 đến hiện tại |
| 3.0 | Phần mềm kế toán MISA Cloud | `Fact_KPI_By_Product.csv` - Doanh thu thực tế theo sản phẩm | 9h30 AM | Từ năm 2018 đến hiện tại |
| 4.0 | Phần mềm kế toán MISA Cloud | `Fact_ActualProduction.csv` - Sản lượng sản xuất thực tế | 9h30 AM | Từ năm 2018 đến hiện tại |
| 5.0 | Phần mềm kế toán MISA Cloud | `Dim_Stock.csv`, `Dim_ParentStock.csv` | 9h30 AM | Từ năm 2018 đến hiện tại |

### 2.2. Điều kiện ràng buộc xuyên suốt báo cáo

| STT | Điều kiện | Mô tả | Note |
| --- | --- | --- | --- |
| 1 | JOIN 3 bảng Fact | `Fact_KPI_Month` (Plan) + `Fact_ActualProduction` (Actual SX) + `Fact_KPI_By_Product` (Actual DT) phải nối qua chiều Kho/Chi nhánh | ⚠️ CẦN XÁC NHẬN: FactoryCode = StockCode không? |
| 2 | Lũy kế & Cùng kỳ | Cần cột `Date` theo tháng trong các bảng Fact | ⚠️ Fact_KPI_By_Product chỉ có `Year` |
| 3 | Dashboard lọc theo tháng | Bảng "Sức khỏe tài chính" cho phép lọc theo tháng cụ thể | |

### 2.3. Filter báo cáo

| STT | Bộ lọc | Mô tả | Giá trị mẫu/Định dạng | Đặc tính |
| --- | --- | --- | --- | --- |
| 1 | Thời gian | Lọc theo tháng/năm | Dropdown (tháng/năm) | All |
| 2 | Sản phẩm | Lọc theo nhóm sản phẩm | Dropdown | All |
| 3 | Tên xí nghiệp | Lọc theo chi nhánh | Dropdown | All |

### 2.4. Chi tiết các trường dữ liệu (Metrics/Dimensions)

| STT | Chỉ tiêu | Mô tả/Cách tính | Loại dữ liệu | Đơn vị | Biểu đồ | Note |
| --- | --- | --- | --- | --- | --- | --- |
| **TABLE 1: KH DT năm theo Chi nhánh** | | | | | | |
| 1 | Thông tin kho (Chi nhánh) | `ParentStockName` / `StockName` | Text | - | Table | |
| 2 | KPI sản xuất năm | `SUM(Fact_KPI_Year[Production])` | Decimal | ĐVC | Table | |
| 3 | KPI doanh thu năm | `SUM(Fact_KPI_Year[Amount])` | Decimal | VNĐ | Table | |
| **TABLE 2: KH DT năm theo Sản phẩm** | | | | | | |
| 4 | Nhóm sản phẩm | `CategoryName` | Text | - | Table | |
| 5 | Sản xuất (Theo DVC) | `SUM(Fact_KPI_By_Product[ProductQuantityDVC])` | Decimal | ĐVC | Table | |
| 6 | Tiêu thụ (Theo DVC) | `SUM(Fact_KPI_By_Product[SaleQuantityDVC])` | Decimal | ĐVC | Table | |
| 7 | Doanh thu | `SUM(Fact_KPI_By_Product[Amount])` | Decimal | VNĐ | Table | |
| **TABLE 3: Sức khỏe Tài chính theo Chi nhánh (Lọc theo Tháng)** | | | | | | |
| 8 | Chi nhánh | `ParentStockName` | Text | - | Table | |
| 9 | KPI sản xuất tháng | `SUM(Fact_KPI_Month[ProductionValue])` WHERE Indicator=SX | Decimal | VNĐ | Table | |
| 10 | KPI doanh thu tháng | `SUM(Fact_KPI_Month[Amount])` WHERE Indicator=DT | Decimal | VNĐ | Table | |
| 11 | GTSX thực tế | `SUM(Fact_ActualProduction[ProductValue])` GROUP BY FactoryCode | Decimal | VNĐ | Table | ⚠️ Cần xác nhận FactoryCode = StockCode |
| 12 | DT thực tế | `SUM(Fact_KPI_By_Product[Amount])` GROUP BY StockCode | Decimal | VNĐ | Table | |
| 13 | % SX so với KH | `[GTSX thực tế] / [KPI SX tháng]` | Decimal | % | Table | |
| 14 | % DT so với KH | `[DT thực tế] / [KPI DT tháng]` | Decimal | % | Table | |
| 15 | Lũy kế GTSX | `CALCULATE([GTSX thực tế], DATESYTD())` | Decimal | VNĐ | Table | |
| 16 | Lũy kế DT | `CALCULATE([DT thực tế], DATESYTD())` | Decimal | VNĐ | Table | |
| 17 | % HT KHSX năm | `[Lũy kế GTSX] / [KPI SX năm]` | Decimal | % | Table | |
| 18 | % HT KHDT năm | `[Lũy kế DT] / [KPI DT năm]` | Decimal | % | Table | |
| 19 | Lũy kế SX cùng kỳ năm trước | `CALCULATE([GTSX thực tế], SAMEPERIODLASTYEAR())` | Decimal | VNĐ | Table | ⚠️ Cần Date tháng |
| 20 | Lũy kế DT cùng kỳ năm trước | `CALCULATE([DT thực tế], SAMEPERIODLASTYEAR())` | Decimal | VNĐ | Table | ⚠️ Cần Date tháng |
| 21 | % GTSX so với cùng kỳ | `[Lũy kế GTSX] / [GTSX cùng kỳ] - 1` | Decimal | % | Table | |
| 22 | % DT so với cùng kỳ | `[Lũy kế DT] / [DT cùng kỳ] - 1` | Decimal | % | Table | |
| **TABLE 4: KPI theo Sản phẩm** | | | | | | |
| 23 | Mã nhóm sản phẩm | `CategoryName` / `InventoryItemGroup` | Text | - | Table | |
| 24 | KPI sản xuất | `SUM(Fact_KPI_Month[QuantityDVC])` WHERE Indicator=SX | Decimal | ĐVC | Table | |
| 25 | KPI tiêu thụ | `SUM(Fact_KPI_Month[QuantityDVC])` WHERE Indicator=TT | Decimal | ĐVC | Table | |
| 26 | KPI doanh thu | `SUM(Fact_KPI_Month[Amount])` WHERE Indicator=DT | Decimal | VNĐ | Table | |
| 27 | SX thực tế (ĐVC) | `SUM(Fact_ActualProduction[ProductQuantityDVC])` | Decimal | ĐVC | Table | |
| 28 | % KPI sản xuất | `[SX thực tế] / [KPI SX]` | Decimal | % | Table | |
| 29 | TT thực tế (ĐVC) | `SUM(Fact_KPI_By_Product[SaleQuantityDVC])` | Decimal | ĐVC | Table | |
| 30 | % KPI tiêu thụ | `[TT thực tế] / [KPI TT]` | Decimal | % | Table | |
| 31 | DT thực tế | `SUM(Fact_KPI_By_Product[Amount])` | Decimal | VNĐ | Table | |
| 32 | % KPI doanh thu | `[DT thực tế] / [KPI DT]` | Decimal | % | Table | |
| **TABLE 5: DT theo Loại Dịch Vụ** | | | | | | |
| 33 | Kho (Loại dịch vụ) | `StockName` | Text | - | Table | |
| 34 | KPI doanh thu | `SUM(Fact_KPI_Month[Amount])` GROUP BY StockCode | Decimal | VNĐ | Table | |
| 35 | DT thực tế | `SUM(Fact_KPI_By_Product[Amount])` GROUP BY StockCode | Decimal | VNĐ | Table | |
| 36 | % DT so với KH | `[DT thực tế] / [KPI DT]` | Decimal | % | Table | |
| 37 | Lũy kế DT | `CALCULATE([DT thực tế], DATESYTD())` | Decimal | VNĐ | Table | |
| 38 | % HT KHDT năm | `[Lũy kế DT] / [KPI DT năm]` | Decimal | % | Table | |
| 39 | Lũy kế DT cùng kỳ | `CALCULATE([DT thực tế], SAMEPERIODLASTYEAR())` | Decimal | VNĐ | Table | |
| 40 | % DT so với cùng kỳ | `[Lũy kế DT] / [Lũy kế DT cùng kỳ] - 1` | Decimal | % | Table | |

---

## TÓM TẮT & CÁC CÂU HỎI CẦN XÁC NHẬN TRƯỚC KHI CODE

| Dashboard | Mức độ chắc chắn | Điểm rủi ro chính |
|---|---|---|
| 1. Doanh Thu Tổng Quan | 60% | Thiếu Date tháng trong Fact_KPI_By_Product |
| 2. Doanh Thu Chi Tiết | 55% | Thiếu Thuế VAT, chưa rõ Số hóa đơn |
| 3. Công Nợ | 35% | Thiếu data lịch sử phát sinh (4 Card chính) |
| 4. KPI Tổng Quan | 50% | Chưa phân biệt Plan vs Actual trong Fact_KPI_Year |
| 5. KPI Chi Tiết | 40% | JOIN 3 Fact phức tạp, thiếu Date tháng |

**6 câu hỏi cần bạn giải đáp:**

1. `Fact_KPI_Month[Amount]` là **KPI Kế hoạch** hay **Doanh thu thực tế**?
2. `Fact_KPI_By_Product` có cột nào liên kết với `Dim_customer` không? (Hiện tại không thấy `Mã khách hàng`)
3. `Fact_KPI_Year` có cột phân biệt KPI Sản xuất vs Doanh thu không? Hay nằm ở 2 dòng khác nhau?
4. `Fact_ActualProduction[FactoryCode]` = `Dim_Stock[StockCode]` hay mã khác nhau?
5. Dashboard 3 (Công nợ): Có file sổ chi tiết TK131 theo từng giao dịch (đầu kỳ/phát sinh/đã TT) không?
6. Mã nhóm KH (`NB`, `BV`, `ĐL`, `CN`, `NL`...) có bảng giải mã thành tên đầy đủ không?
