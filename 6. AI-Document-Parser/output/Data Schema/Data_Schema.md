# Data Dictionary - Sovigaz Raw Data

Tài liệu này tổng hợp cấu trúc cột của toàn bộ các file dữ liệu thô, giúp AI Agent nắm bắt nhanh Schema mà tốn ít context nhất.

### 📂 1. MISA_Cloud / Dim / Dim_Indicator.csv (Danh mục Chỉ tiêu)
- **Columns (3):** `Indicator` (Chỉ tiêu), `Name` (Tên/Mô tả), `ETL_DATE` (Ngày chạy ETL)

### 📂 1. MISA_Cloud / Dim / Dim_InventoryItemType.csv (Danh mục Loại vật tư hàng hóa)
- **Columns (7):** `InventoryItemTypeValue` (Mã loại vật tư), `InventoryItemTypeName` (Tên loại vật tư), `CreatedBy` (Người tạo), `CreatedDate` (Ngày tạo), `ModifiedBy` (Người sửa), `ModifiedDate` (Ngày sửa), `ETL_DATE` (Ngày chạy ETL)

### 📂 1. MISA_Cloud / Dim / Dim_ParentStock.csv (Danh mục Kho cha / Chi nhánh)
- **Columns (2):** `ParentStockCode` (Mã kho cha), `ParentStockName` (Tên kho cha)

### 📂 1. MISA_Cloud / Dim / Dim_ProductCategories.csv (Danh mục Nhóm sản phẩm)
- **Columns (5):** `Indicator` (Mã chỉ tiêu), `CategoryName` (Tên danh mục), `Name` (Tên/Mô tả), `Group` (Nhóm), `ETL_DATE` (Ngày chạy ETL)

### 📂 1. MISA_Cloud / Dim / Dim_Stock.csv (Danh mục Kho)
- **Columns (8):** `StockID` (ID Kho), `BranchID` (ID Chi nhánh), `StockCode` (Mã kho), `StockName` (Tên kho), `Description` (Mô tả), `InventoryAccount` (Tài khoản kho), `ETL_DATE` (Ngày chạy ETL), `ParentStockCode` (Mã kho cha)

### 📂 1. MISA_Cloud / Dim / Dim_Unit.csv (Danh mục Đơn vị tính)
- **Columns (13):** `UnitID` (ID Đơn vị tính), `UnitName` (Tên ĐVT), `Description` (Mô tả), `Inactive` (Ngừng hoạt động), `IsDeleted` (Đã xóa), `CreatedBy` (Người tạo), `CreatedDate` (Ngày tạo), `ModifiedBy` (Người sửa), `ModifiedDate` (Ngày sửa), `RowVersion`, `ServerRowVersion`, `UploadState`, `ETL_DATE` (Ngày chạy ETL)

### 📂 1. MISA_Cloud / Fact / Fact_ActualProduction.csv (Dữ liệu Sản xuất thực tế)
- **Columns (9):** `CategoryName` (Tên nhóm SP), `ProductName` (Tên sản phẩm), `ProductQuantity` (SL sản xuất), `PurchaseQuantity` (SL mua vào), `ProductQuantityDVC` (SL quy đổi Đơn vị chuẩn), `ProductValue` (Giá trị sản xuất), `Date` (Ngày tháng), `FactoryCode` (Mã xí nghiệp), `ETL_DATE` (Ngày chạy ETL)

### 📂 1. MISA_Cloud / Fact / Fact_KPI_By_Product.csv (Dữ liệu KPI theo Sản phẩm)
- **Columns (12):** `RevenueCode` (Mã doanh thu), `StockCode` (Mã kho), `CategoryName` (Tên nhóm SP), `ProductName` (Tên sản phẩm), `ProductCategoryName` (Tên loại sản phẩm), `ProductQuantityDVT` (Số lượng theo ĐVT), `ProductQuantityDVC` (Số lượng theo Đơn vị chuẩn), `ProductQuantityDVT1`, `SaleQuantityDVC` (Số lượng bán chuẩn), `Amount` (Thành tiền), `Year` (Năm), `ETL_DATE` (Ngày chạy ETL)

### 📂 1. MISA_Cloud / Fact / Fact_KPI_Month.csv (Dữ liệu KPI theo Tháng)
- **Columns (13):** `Indicator` (Chỉ tiêu), `StockCode` (Mã kho), `InventoryCodePlan` (Mã kế hoạch vật tư), `InventoryItemName` (Tên vật tư), `InventoryItemGroup` (Nhóm vật tư), `ProductionValue` (Giá trị sản xuất), `ProductUnit` (ĐVT), `ProductUnitDVC` (ĐVT chuẩn), `QuantityDVT` (Sản lượng ĐVT), `QuantityDVC` (Sản lượng chuẩn), `Amount` (Số tiền), `Date` (Ngày tháng), `ETL_DATE` (Ngày chạy ETL)

### 📂 1. MISA_Cloud / Fact / Fact_KPI_Year.csv (Dữ liệu KPI theo Năm)
- **Columns (5):** `Parent_Stock` (Kho cha/Xí nghiệp), `Production` (Sản lượng), `Amount` (Giá trị), `Year` (Năm), `ETL_DATE` (Ngày chạy ETL)

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

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 131.xlsx (Phải thu của khách hàng)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 136.xlsx (Phải thu nội bộ)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1361.xlsx (Vốn kinh doanh ở các đơn vị trực thuộc)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13611.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13612.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13613.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13614.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13615.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13616.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13617.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13618.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13619.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1362.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1363.xlsx (Phải thu nội bộ chi tiết)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1368.xlsx (Phải thu nội bộ khác)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1388.xlsx (Phải thu khác)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 244.xlsx (Cầm cố, thế chấp, ký quỹ, ký cược)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 2442.xlsx (Chi tiết Cầm cố/Ký quỹ)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 2444.xlsx (Chi tiết Cầm cố/Ký quỹ)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 337.xlsx (Thanh toán theo tiến độ hợp đồng xây dựng)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 344.xlsx (Nhận ký quỹ, ký cược dài hạn)
- **Columns (17):** `Mã khách hàng`, `Tên khách hàng`, `Địa chỉ`, `Tổng nợ`, `Không có hạn nợ`, `Nợ trước hạn: 0-30 ngày`, `Nợ trước hạn: 31-90 ngày`, `Nợ trước hạn: Trên 90 ngày`, `Nợ trước hạn: Tổng`, `Nợ quá hạn: 1-30 ngày`, `Nợ quá hạn: 31-90 ngày`, `Nợ quá hạn: 91-180 ngày`, `Nợ quá hạn: 181-365 ngày`, `Nợ quá hạn: 366-730 ngày`, `Nợ quá hạn: 731-1095 ngày`, `Nợ quá hạn: Trên 1095 ngày`, `Nợ quá hạn: Tổng`

### 📂 3. Static_Data / Dim_Date.csv
- **Columns (11):** `DateKey`, `Date`, `Day`, `Month`, `Year`, `Quarter`, `Week`, `DayOfWeek`, `MonthName`, `YearMonth`, `IsWeekend`

### 📂 3. Static_Data / Dim_Month.csv
- **Columns (10):** `MonthKey`, `Year`, `Month`, `MonthName`, `Quarter`, `YearMonth`, `StartDate`, `EndDate`, `IsCurrent`, `MonthVietnamese`

### 📂 3. Static_Data / Dim_Year.csv
- **Columns (2):** `YearText`, `Value`
