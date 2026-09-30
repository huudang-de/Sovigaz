# Data Dictionary - Sovigaz Raw Data

Tài liệu này tổng hợp cấu trúc cột của toàn bộ các file dữ liệu thô, giúp AI Agent nắm bắt nhanh Schema mà tốn ít context nhất.

### 📂 1. MISA_Cloud / Dim / Dim_Indicator.csv
- **Columns (3):** `Indicator`, `Name`, `ETL_DATE`

### 📂 1. MISA_Cloud / Dim / Dim_InventoryItemType.csv
- **Columns (7):** `InventoryItemTypeValue`, `InventoryItemTypeName`, `CreatedBy`, `CreatedDate`, `ModifiedBy`, `ModifiedDate`, `ETL_DATE`

### 📂 1. MISA_Cloud / Dim / Dim_ParentStock.csv
- **Columns (2):** `ParentStockCode`, `ParentStockName`

### 📂 1. MISA_Cloud / Dim / Dim_ProductCategories.csv
- **Columns (5):** `Indicator`, `CategoryName`, `Name`, `Group`, `ETL_DATE`

### 📂 1. MISA_Cloud / Dim / Dim_Stock.csv
- **Columns (8):** `StockID`, `BranchID`, `StockCode`, `StockName`, `Description`, `InventoryAccount`, `ETL_DATE`, `ParentStockCode`

### 📂 1. MISA_Cloud / Dim / Dim_Unit.csv
- **Columns (13):** `UnitID`, `UnitName`, `Description`, `Inactive`, `IsDeleted`, `CreatedBy`, `CreatedDate`, `ModifiedBy`, `ModifiedDate`, `RowVersion`, `ServerRowVersion`, `UploadState`, `ETL_DATE`

### 📂 1. MISA_Cloud / Fact / Fact_ActualProduction.csv
- **Columns (9):** `CategoryName`, `ProductName`, `ProductQuantity`, `PurchaseQuantity`, `ProductQuantityDVC`, `ProductValue`, `Date`, `FactoryCode`, `ETL_DATE`

### 📂 1. MISA_Cloud / Fact / Fact_KPI_By_Product.csv
- **Columns (12):** `RevenueCode`, `StockCode`, `CategoryName`, `ProductName`, `ProductCategoryName`, `ProductQuantityDVT`, `ProductQuantityDVC`, `ProductQuantityDVT1`, `SaleQuantityDVC`, `Amount`, `Year`, `ETL_DATE`

### 📂 1. MISA_Cloud / Fact / Fact_KPI_Month.csv
- **Columns (13):** `Indicator`, `StockCode`, `InventoryCodePlan`, `InventoryItemName`, `InventoryItemGroup`, `ProductionValue`, `ProductUnit`, `ProductUnitDVC`, `QuantityDVT`, `QuantityDVC`, `Amount`, `Date`, `ETL_DATE`

### 📂 1. MISA_Cloud / Fact / Fact_KPI_Year.csv
- **Columns (5):** `Parent_Stock`, `Production`, `Amount`, `Year`, `ETL_DATE`

### 📂 2. MISA_AMIS / Dim_customer / BD.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / BH.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / CT.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / HP.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / KH.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / NT.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / PR.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / TK.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / VP.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Dim_customer / VP2.xlsx
- **Columns (52):** `STT`, `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Diễn giải`, `Công nợ`, `Nhóm KH, NCC`, `Mã số thuế/CCCD chủ hộ`, `Mã số ĐVQHNS`, `Số hộ chiếu`, `Điện thoại`, `Website`, `Số CMND`, `Ngày cấp`, `Nơi Cấp`, `Điều khoản TT`, `Số ngày được nợ`, `Số nợ tối đa`, `TK công nợ phải thu`, `Nhân viên`, `Tên nhân viên`, `TK Ngân hàng`, `Tên ngân hàng`, `Chi nhánh TK ngân hàng`, `Tỉnh/TP TK ngân hàng`, `Quốc gia`, `Tỉnh/TP`, `Quận/Huyện`, `Xã/Phường`, `Xưng hô`, `Người liên hệ`, `ĐT di động NLH`, `Email NLH`, `Người đại diện PL`, `Người nhận hóa đơn`, `Điện thoại người nhận hóa đơn`, `Email người nhận hóa đơn`, `Địa điểm giao hàng`, `Tổ chức/Cá nhân`, `Là nhà cung cấp`, `Là Đối tượng nội bộ`, `Là Tổng công ty/chi nhánh`, `Trạng thái`, `Ngày tạo`, `Người tạo`, `Ngày sửa`, `Người sửa`, `Trường mở rộng 1`, `Trường mở rộng 2`, `Trường mở rộng 3`, `Trường mở rộng 4`, `Trường mở rộng 5`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 131.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 136.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1361.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13611.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13612.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13613.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13614.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13615.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13616.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13617.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13618.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13619.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1362.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1363.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1368.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1388.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 244.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 2442.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 2444.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 337.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 344.xlsx
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 3. Static_Data / Dim_Date.csv
- **Columns (11):** `DateKey`, `Date`, `Day`, `Month`, `Year`, `Quarter`, `Week`, `DayOfWeek`, `MonthName`, `YearMonth`, `IsWeekend`

### 📂 3. Static_Data / Dim_Month.csv
- **Columns (10):** `MonthKey`, `Year`, `Month`, `MonthName`, `Quarter`, `YearMonth`, `StartDate`, `EndDate`, `IsCurrent`, `MonthVietnamese`

### 📂 3. Static_Data / Dim_Year.csv
- **Columns (2):** `YearText`, `Value`
