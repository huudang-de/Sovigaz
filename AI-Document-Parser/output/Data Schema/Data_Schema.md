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
- **Columns (17):** `NTHTCVPHONG01`, `CÔNG TY TNHH HTC VÂN PHONG`, `Số 332 Lê Hồng phong, Phường Đông Ninh Hòa, Tỉnh Khánh Hòa, Việt Nam.`, `219622347`, `40500000`, `154303947`, `24818400`, `0`, `179122347`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 136.xlsx
- **Columns (17):** `BHBV309`, `Bệnh Viện Đa Khoa Bình Thuận`, `Đường Tôn Thất Bách, Phường Bình Thuận, Tỉnh Lâm Đồng, Việt Nam.`, `748000`, `748000`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1361.xlsx
- **Columns (17):** `VPBV173`, `Bệnh Viện Bãi Cháy`, `Đường 279, Phường Việt Hưng, Tỉnh Quảng Ninh`, `250136910`, `250136910`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13611.xlsx
- **Columns (15):** `Cộng nhóm:`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13612.xlsx
- **Columns (17):** `1002`, `Xí nghiệp hơi kỹ nghệ Biên Hòa - CN Công ty CP hơi kỹ nghệ Que Hàn`, `KCN Biên Hòa 1, Đường Số 2, Phường Trấn Biên, Tỉnh Đồng Nai, Việt Nam`, `18553418489`, `18553418489`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13613.xlsx
- **Columns (17):** `1003`, `CN Công ty CP Hơi kỹ nghệ Que hàn - XÍ NGHIỆP HƠI KỸ NGHỆ CẦN THƠ`, `Đường Trục Chính, KCN Trà Nóc, Phường Thới An Đông, Thành phố Cần Thơ, Việt Nam`, `4842164571`, `4347427783`, `131220000`, `0`, `0`, `131220000`, `0`, `125135280`, `238381508`, `0`, `0`, `0`, `0`, `363516788`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13614.xlsx
- **Columns (17):** `1004`, `Xí nghiệp Hơi kỹ nghệ Nha Trang - CN Công ty CP Hơi kỹ nghệ Que hàn`, `Lô A40, A41 Cụm Công Nghiệp Diên Phú, Xã Diên Điền, Tỉnh Khánh Hoà`, `338813826`, `50747586`, `288066240`, `0`, `0`, `288066240`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13615.xlsx
- **Columns (17):** `1005`, `CN Công ty CP Hơi kỹ nghệ Que hàn - Xí nghiệp Que hàn điện Khánh Hội`, `Lô C4 đường số 1, KCN Nhựt Chánh, Xã Bình Đức, Tỉnh Tây Ninh.`, `302245800`, `0`, `302245800`, `0`, `0`, `302245800`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13616.xlsx
- **Columns (17):** `1006`, `CN CTy Hơi kỹ nghệ Que hàn - XÍ NGHIỆP HƠI KỸ NGHỆ PHAN RANG`, `Quốc lộ 1A, thôn Tân Sơn 2, Phường Bảo An, tỉnh Khánh Hòa`, `1387063168`, `1387063168`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13617.xlsx
- **Columns (17):** `1007`, `CN Công ty CP Hơi kỹ nghệ Que hàn - XÍ NGHIỆP HƠI KỸ NGHỆ QUE HÀN BÌNH DƯƠNG`, `Ô 04, Lô A, Đường số 1, Khu Công nghiệp Đồng An, phường Bình Hòa, thành phố Hồ Chí Minh.`, `582145815414`, `513665312806`, `1008400104`, `0`, `0`, `1008400104`, `1429983289`, `2555508096`, `3047204624`, `18443245494`, `9106662600`, `18374651371`, `14514847030`, `67472102504`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13618.xlsx
- **Columns (17):** `VPBV173`, `Bệnh Viện Bãi Cháy`, `Đường 279, Phường Việt Hưng, Tỉnh Quảng Ninh`, `250136910`, `250136910`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 13619.xlsx
- **Columns (17):** `1009`, `NHÀ MÁY ĐẤT ĐÈN VÀ HÓA CHẤT TRÀNG KÊNH`, `Thị Trấn Minh đức, Phường Bạch Đằng, TP Hải Phòng`, `216235031`, `216235031`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1362.xlsx
- **Columns (15):** `Cộng nhóm:`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1363.xlsx
- **Columns (15):** `Cộng nhóm:`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1368.xlsx
- **Columns (17):** `BHBV309`, `Bệnh Viện Đa Khoa Bình Thuận`, `Đường Tôn Thất Bách, Phường Bình Thuận, Tỉnh Lâm Đồng, Việt Nam.`, `748000`, `748000`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 1388.xlsx
- **Columns (16):** `HP.TTHIEU`, `TRỊNH THỊ HIẾU`, `49011000`, `49011000`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 244.xlsx
- **Columns (17):** `BD.BIWASE`, `CÔNG TY TNHH MTV SẢN XUẤT - THƯƠNG MẠI - DỊCH VỤ BIWASE`, `Số 808, Lý Thái Tổ, Khu 2, Phường Bình Dương, TP Hồ Chí Minh`, `2500000`, `2500000`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 2442.xlsx
- **Columns (17):** `BD.BIWASE`, `CÔNG TY TNHH MTV SẢN XUẤT - THƯƠNG MẠI - DỊCH VỤ BIWASE`, `Số 808, Lý Thái Tổ, Khu 2, Phường Bình Dương, TP Hồ Chí Minh`, `2500000`, `2500000`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 2444.xlsx
- **Columns (17):** `VPVCBL`, `CÔNG TY TNHH MTV CHO THUÊ TÀI CHÍNH NHTMCP NGOẠI THƯƠNG VN CN TP.HCM`, `Tầng 8, Tòa nhà Vietcombank Kỳ Đồng, Số 13 - 13 Bis Kỳ Đồng, Phường 9, Quận 3, TP.HCM`, `167601938`, `167601938`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 337.xlsx
- **Columns (15):** `Cộng nhóm:`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 2. MISA_AMIS / Fact_AnalyticsDebit / 344.xlsx
- **Columns (17):** `BHBEN`, `CÔNG TY CỔ PHẦN BEN`, `Số 12KDC Lucky Dragon, 357 Đường Đỗ Xuân Hợp, Phường Phước Long B, Quận 9, TP. Hồ Chí Minh`, `20000000`, `20000000`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`, `0`

### 📂 3. Static_Data / Dim_Date.csv
- **Columns (11):** `DateKey`, `Date`, `Day`, `Month`, `Year`, `Quarter`, `Week`, `DayOfWeek`, `MonthName`, `YearMonth`, `IsWeekend`

### 📂 3. Static_Data / Dim_Month.csv
- **Columns (10):** `MonthKey`, `Year`, `Month`, `MonthName`, `Quarter`, `YearMonth`, `StartDate`, `EndDate`, `IsCurrent`, `MonthVietnamese`

### 📂 3. Static_Data / Dim_Year.csv
- **Columns (2):** `YearText`, `Value`
