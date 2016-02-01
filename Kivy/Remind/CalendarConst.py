day_of_week = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']

lunar_event = {(1, 1)  : 'Tết Nguyên Đán',
					(2, 1)  : 'Mồng 2 Tết Nguyên Đán',
					(3, 1)  : 'Mồng 3 Tết Nguyên Đán',
					(4, 1)  : 'Mồng 4 Tết Nguyên Đán',
					(15, 1) : 'Tết Nguyên tiêu',
					(10, 3) : 'Giỗ tổ Hùng Vương',
					(3, 3)  : 'Tết Hàn thực',
					(14, 4) : 'Tết Dân tộc Khmer - Lễ hội Chol Chnam Thmay',
					(15, 4) : 'Lễ Phật Đản',
					(5, 5)  : 'Tết Đoan Ngọ',
					(15, 7) : 'Lễ Vu Lan',
					(1, 8)  : 'Tết Katê',
					(15, 8) : 'Tết Trung Thu',
					(9, 9)  : 'Tết Trùng Cửu',
					(10, 10): 'Tết Trùng Thập',
					(23, 12): 'Ngày Ông Táo chầu trời'}

solar_traditional_event = {(1, 3)  : 'Bắt Đầu Hội Phủ Dầy Tại Nam Định',
								    (10, 3) : 'Kết Thúc Hội Phủ Dầy Tại Nam Định',
								    (4, 3)  : 'Hội đền Hai Bà Trưng Tại Mê Linh, Hà Nội',
								    (4, 1)  : 'Hội Liễu Đôi Tại Nam Định',
								    (8, 1)  : 'Bắt Đầu Hội Chùa Đậu Tại Thường Tín, Hà Nội',
								    (10, 1) : 'Kết Thúc Hội Chùa Đậu Tại Thường Tín, Hà Nội',
								    (12, 12): 'Hội Đống Đa Tại Đống Đa, Hà Nội; Tây Sơn, Bình Định',
								    (1, 12) : 'Bắt Đầu Hội Chùa Hương Tại Mỹ Đức, Hà Nội',
								    (10, 1) : 'Lễ hội đua Voi Tại Buôn Ma Thuột, Đắk Lắk',
								    (13, 1) : 'Hội Lim Tại Tiên Du, Bắc Ninh',
								    (10, 12): 'Hội Côn Sơn Tại Hải Dương',
								    (15, 1) : 'Hội Xuân Núi Bà Tại Tây Ninh',
								    (6, 3)  : 'Hội Chùa Tây Phương Tại Thạch Thất Tại Hà Nội',
								    (14, 3) : 'Lễ Hội Gò Tháp  Tháp Mười Tại Đồng Tháp Diễn Ra Trong 3 Ngày : 14,15,16',
								    (14, 11): 'Lễ Hội Gò Tháp  Tháp Mười Tại Đồng Tháp Diễn Ra Trong 3 Ngày : 14,15,16',
								    (7, 3)  : 'Hội Chùa Thầy Tại Quốc Oai, Hà Nội',
								    (10, 3) : 'Giỗ Tổ Hùng Vương Tại Việt Trì, Phú Thọ',
								    (1, 3)  : 'Bắt Đầu Hội Đâm Trâu Tại Buôn Ma Thuột, Đắk Lắk',
								    (31, 3) : 'Kết Thúc Hội Đâm Trâu Tại Buôn Ma Thuột, Đắk Lắk\nKết Thúc Hội Chùa Hương Tại Mỹ Đức, Hà Nội',
								    (9, 4)  : 'Hội Gióng Tại Phù Đổng, Gia Lâm, Hà Nội',
								    (23, 4) : 'Hội Bà Chúa Xứ Tại Châu Đốc, An Giang',
								    (2, 8)  : 'Hội Lăng Lê Văn Duyệt Tại TP Hồ Chí Minh',
								    (9, 8)  : 'Hội Chọi Trâu Đồ Sơn Tại Hải Phòng',
								    (16, 8) : 'Hội Nghinh Ông Tại Tiền Giang, Bến Tre, TP. HCM, Bình Thuận',
								    (20, 8) : 'Hội Côn Sơn - Kiếp Bạc Tại Hải Dương'}

solar_event = {(9, 1)  : 'Ngày Sinh viên - Học sinh Việt Nam',
					(3, 2)  : 'Ngày thành lập Đảng Cộng sản Việt Nam',
					(27, 2) : 'Ngày Thầy thuốc Việt Nam',
					(8, 3)  : 'Ngày phụ nữ thế giới',
					(26, 3) : 'Ngày thành lập Đoàn Thanh niên Cộng sản Hồ Chí Minh',
					(27, 3) : 'Ngày Thể thao Việt Nam',
					(21, 4) : 'Ngày Sách Việt Nam',
					(30, 4) : 'Kết thúc Chiến tranh Việt Nam',
					(1, 5)  : 'Kỷ niệm ngày của người lao động toàn thế giới',
					(15, 5) : 'Ngày thành lập Đội Thiếu niên Tiền phong Hồ Chí Minh',
					(19, 5) : 'Ngày sinh của Chủ tịch Hồ Chí Minh',
					(5, 6)  : 'Ngày Bác Hồ ra đi tìm đường cứu nước',
					(27, 7) : 'Ngày Thương binh Liệt sĩ',
					(19, 8) : 'Ngày Cách mạng, Tám thành công',
					(2, 9)  : 'Kỷ niệm ngày Chủ tịch Hồ Chí Minh đọc tuyên ngôn độc lập',
					(13, 10): 'Ngày Doanh nhân Việt Nam',
					(20, 10): 'Ngày thành lập Hội Phụ nữ Việt Nam',
					(9, 11) : 'Ngày Pháp luật Việt Nam',
					(20, 11): 'Ngày Nhà giáo Việt Nam',
					(22, 12): 'Ngày thành lập Quân đội Nhân dân Việt Nam',
					(25, 12): 'Ngày Lễ Giáng Sinh'}

solar_important_event = [(1, 1), (10,3 ), (30, 4), (1, 5), (2, 9)]

lunar_important_event = [(29, 12), (30, 12), (1, 1), (2, 1), (3, 1), (4, 1)]

can_year_list =['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
chi_year_list =['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mảo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']

chi_month_list = ['Dần', 'Mảo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu']
can_month_list = {'Giáp Kỷ' : 'Bính', 'Bính Tân' : 'Canh', 'Đinh Nhâm': 'Nhâm', 'Mậu Quý' : 'Giáp', 'Ất Canh' : 'Mậu'}

all_can_chi_list = ['Giáp Tý', 'Ất Sửu', 'Bính Dần', 'Đinh Mão', 'Mậu Thìn', 'Kỷ Tỵ', 'Canh Ngọ', 
						 'Tân Mùi', 'Nhâm Thân', 'Quý Dậu', 'Giáp Tuất', 'Ất Hợi', 'Bính Tý', 'Đinh Sửu', 
						 'Mậu Dần', 'Kỷ Mão', 'Canh Thìn', 'Tân Tỵ', 'Nhâm Ngọ', 'Quý Mùi', 'Giáp Thân', 
						 'Ất Dậu', 'Bính Tuất', 'Đinh Hợi', 'Mậu Tý', 'Kỷ Sửu', 'Canh Dần', 'Tân Mão', 
						 'Nhâm Thìn', 'Quý Tỵ', 'Giáp Ngọ', 'Ất Mùi', 'Bính Thân', 'Đinh Dậu', 'Mậu Tuất', 
						 'Kỷ Hợi', 'Canh Tý', 'Tân Sửu', 'Nhâm Dần', 'Quý Mão', 'Giáp Thìn', 'Ất Tỵ', 
						 'Bính Ngọ', 'Đinh Mùi', 'Mậu Thân', 'Kỷ Dậu', 'Canh Tuất', 'Tân Hợi ', 'Nhâm Tý', 
						 'Quý Sửu', 'Giáp Dần', 'Ất Mão', 'Bính Thìn', 'Đinh tỵ', 'Mậu Ngọ', 'Kỷ Mùi', 
						 'Canh thân', 'Tân Dậu', 'Nhâm Tuất', 'Quý Hợi']

can_chi_first_day = [datetime.date(1900, 1, 31), all_can_chi_list.index('Giáp Thìn')]

can_first_hour = 'Giáp' # first hour of 31/1/1900 ~ 1/1/1900 in lunar calendar

can_chi_hour_list = [('Tý', 23, 0), ('Sửu', 1, 2), ('Dần', 3, 4), ('Mão', 5, 6), ('Thìn', 7 ,8), ('Tị', 9, 10),
						  ('Ngọ', 11, 12), ('Mùi', 13, 14), ('Thân', 15, 16), ('Dậu', 17, 18), ('Tuất', 19, 20), ('Hợi', 21, 22)]
