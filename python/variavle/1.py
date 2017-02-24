cars=100 #자동차수
space_in_a_car=4.0
drivers=30 #운전자수
passengers=90 #오늘 차를 탈사람의 수
cars_not_driven=cars-drivers #반차의 수
cars_driven=drivers #움직이는 차의수
carpool_capacity=cars_driven*space_in_a_car #태울수있는 사람의수
average_passengers_per_car=passengers/cars_driven #차마다 타는 평균사람의 수

print("자동차",cars,"대가있습니다")
print("운전자는",drivers,"명이있습니다")
print("오늘 빈차는",cars_not_driven,"대일 겁니다")
print("오늘은",carpool_capacity,"명을태울수 있습니다")
print("함께 탈사람은",passengers,"명 있습니다")
print("차마다",average_passengers_per_car,"명 정도씩 태울수있습니다")
