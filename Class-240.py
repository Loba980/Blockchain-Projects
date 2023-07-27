#making the class
class Vehicles:
	#making the objects in the class
	car_1= "Tesla Model 3"
	car_2= "Mustang"
	#creating main fucntion using self parameter
	def main(self):
		#printing car variable using self.car_1(2)
		print("I have", self.car_1)
		print("I have", self.car_2)
#creating a class instance in object
Vehicle_data= Vehicles()
#printing one of the objects using the instance
print("Car:", Vehicle_data.car_1)
#calling main function using the instance of a class
Vehicle_data.main()