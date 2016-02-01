import datetime

class Day():
	def __init__(self):
		self.special_day = datetime.date(2016, 1, 10)
		self.today = datetime.date.today()
		self.numOfDay = self.today - self.special_day

	def yearOfLove(self):
		year = 0
		month = 0
		cur_month = self.special_day.month
		cur_year = self.special_day.year
		numOfDay = self.numOfDay.days

		while (cur_year != self.today.year or cur_month != self.today.month):
			if cur_month == 12:
				cur_year += 1
			cur_month = (cur_month) % 12 + 1
			numOfDay -= self.dayOfMonth(cur_month, cur_year)
			month += 1
		year = month / 12
		month = month % 12
		return (year, month, numOfDay)

	def dayOfMonth(self, month, year):
		if month != 12:
			nextMonth = month + 1
			nextYear = year
		else:
			nextMonth = 1
			nextYear = year + 1
		now = datetime.datetime(year, month, 1)
		future = datetime.datetime(nextYear, nextMonth, 1)
		return (future - now).days

	def dayLeft(self):
		day_left = 0

		if self.today.day > 10:
			month = (self.today.month + 1) % 12
		else:
			month = self.today.month
		day_left = (self.today - datetime.date(self.today.year, month, 10))

		return abs(day_left.days)

	def remind(self):
		if self.today.day == 10:
			return True
		return False
