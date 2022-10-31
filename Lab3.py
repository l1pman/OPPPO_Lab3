import re
import os

class Plant:

	def __init__(self,name):
		self.name = name


class Tree(Plant):

	def __init__(self, name, age):
		super().__init__(name)
		self.age = age

	def __str__(self):
		return f"|Tree|: {self.name} |Age|: {self.age}"


Months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')


class Bush(Plant):

	def __init__(self, name, flowering_month):
		super().__init__(name)
		self.flowering_month = flowering_month

	def __str__(self):
		return f"|Bush|: {self.name} |Flowering Month|: {self.flowering_month}"


class Cactus(Plant):

	def __init__(self, name, thorn_lenght):
		super().__init__(name)
		self.thorn_lenght = thorn_lenght

	def __str__(self):
		return f"|Cactus|: {self.name} |Thorn Lenght|: {self.thorn_lenght}"


class List:

	def __init__(self, head):	
		self.head = head 

	def addNode(self, node):
		if self.head == None:
			self.head = node
			self.head.nextnode = self.head
		elif self.head.nextnode == self.head:
			self.head.nextnode = node
			node.nextnode = self.head
		else:
			currentNode = self.head
			while(currentNode.nextnode != self.head):
				currentNode = currentNode.nextnode
			currentNode.nextnode = node
			node.nextnode = self.head 

	def isListEmpty(self):
		if self.head == None:
			print("\n ---------\n List is empty\n ---------\n")
			return True
		return False	

	def delNode(self, position):
		if (self.isListEmpty()):
			return
		currentNode = self.head
		lengthnodes = 0
		while(currentNode.nextnode != self.head):
			lengthnodes += 1
			currentNode = currentNode.nextnode
		if position > lengthnodes:
			print("WRONG POSITION")
			return


		if self.head is None:
			return


		temp = self.head
		currentNode = self.head
		if position == 0:
			if currentNode.nextnode == self.head:
				self.head = None
			else:
				while(currentNode.nextnode != self.head):
					currentNode = currentNode.nextnode
				self.head = temp.nextnode
				temp = None
				currentNode.nextnode = self.head
				return

		        # Find the key to be deleted
		for i in range(position - 1):
			temp = temp.nextnode
			if temp is None:
				break

		        # If the key is not present
		if temp is None:
			return

		if temp.nextnode is None:
			return

		nextnode = temp.nextnode.nextnode
		temp.nextnode = None
		temp.nextnode = nextnode

	def printAll(self):
		if (self.isListEmpty()):
			return

		print("\n __________START__________")
		i = 0
		currentNode = self.head
		while(currentNode.nextnode != self.head):
			print(f"{i} - {currentNode.data}")
			currentNode = currentNode.nextnode
			i += 1

		print(f"{i} - {currentNode.data}")
		print("___________END___________\n")

	def printMulItem(self, amount):
		self.amount = amount
		if (self.isListEmpty()):
			return

		print("\n __________START__________")
		
		currentNode = self.head
		for i in range(self.amount):
			print(f"{i} - {currentNode.data}")
			currentNode = currentNode.nextnode	
		print("___________END___________\n")


	def printAllBushes(self):
		if (self.isListEmpty()):
			return
		print("\n __________START__________")
		i = 0
		currentNode = self.head
		while(currentNode.nextnode != self.head):
			if isinstance(currentNode.data, Bush):
				print(f"{i} - {currentNode.data}")
			currentNode = currentNode.nextnode
			i += 1
					
							
		if isinstance(currentNode.data, Bush):
			print(f"{i} - {currentNode.data}")
			print("___________END___________\n")


	def delByType(self, mod):
		if (self.isListEmpty()):
			return
		currentNode = self.head
		self.mod = mod
		i = 0
		delvar = []
		while(currentNode.nextnode != self.head):
			if isinstance(currentNode.data, self.mod):
				delvar.append(i)
			i += 1
			currentNode = currentNode.nextnode
		if isinstance(currentNode.data, self.mod):
			delvar.append(i)
		for k in reversed(delvar):
			self.delNode(k)

	def delAllPlants(self):
		if (self.isListEmpty()):
			return
		currentNode = self.head
		while(currentNode.nextnode != self.head):
			self.delNode(0)
			currentNode = currentNode.nextnode
		self.delNode(0)	

	
	def sort_by_name(self):
		currentNode = self.head        
		index = None
		if(self.head == None):
			return
		else:
			while(currentNode.nextnode != self.head):
				index = currentNode.nextnode
				while(index != self.head):
					if currentNode.data.name > index.data.name:
						currentNode.data, index.data = index.data, currentNode.data
					index = index.nextnode
				currentNode = currentNode.nextnode
			

class Node:
    def __init__(self, data):
        self.data = data 
        self.nextnode = None 



new_tree = r'(tree \{[A-Z][a-z]*,\s*\d+\})'
new_bush = r'(bush \{[A-Z][a-z]*,\s*\w+\})'
new_cactus = r'(cactus \{[A-Z][a-z]*,\s*\d*\.*\d*\})'
print_mul_items = r'(print\(\d+\))'
print_all = r'(printAll\(\))'
delete_all = r'(deleteAll\(\))'
delete_plant = r'(delete\(\d+\))'
delete_all_trees = r'(deleteAllTrees\(\))'
delete_all_bushes = r'(deleteAllBushes\(\))'
delete_all_cactuses = r'(deleteAllCactuses\(\))'
sortByName = r'(sort_by_name\(\))'
print_all_bushes = r'(printAllBushes\(\))'


def main():
	os.system('cls||clear')
	newlist = List(None)
	with open("input.txt", "r") as file1:
		lines = file1.readlines()
	
	for line in lines:
		line = line.rstrip()
		if not line.strip() == "":
			if '#' in line:
				line = line[0:line.find('#')-1]
			
			if((re.match(new_tree, line)) != None):
				print("CREATE NEW TREE")
				
				line = line[6:len(line)-1]
				variables = line.split(", ")
				newlist.addNode(Node(Tree(variables[0], variables[1])))

			elif((re.match(new_bush, line)) != None):
				print("CREATE NEW BUSH")
				
				line = line[6:len(line)-1]
				variables = line.split(", ")
				monthvar = variables[1]
				if monthvar in Months:
					newlist.addNode(Node(Bush(variables[0], monthvar)))
				else:
					print("\tWRONG MONTH")	

			elif((re.match(new_cactus, line)) != None):
				print("CREATE NEW CACTUS")
				
				line = line[8:len(line)-1]
				variables = line.split(", ")
				newlist.addNode(Node(Cactus(variables[0], variables[1])))

			elif((re.match(print_all, line)) != None):
				print("\n <---PRINT ALL COMMAND--->")
				newlist.printAll()

			elif((re.match(print_mul_items, line)) != None):
				amount = int(line[6:len(line)-1])
				print(f"<---PRINT {amount} ITEMS--->")
				newlist.printMulItem(amount)

			elif((re.match(delete_plant, line)) != None):
				
				index = line[7:len(line)-1]
				index = int(index)
				print(f"\n <---DELETE {index} ITEM COMMAND--->")
				newlist.delNode(index)

			elif((re.match(print_all_bushes, line)) != None):
				print("\n <---PRINT ALL BUSHES--->")
				newlist.printAllBushes()

			elif((re.match(delete_all_trees, line)) != None):
				print("\n DELETE ALL TREES")
				newlist.delByType(Tree)
					
			elif((re.match(delete_all_bushes, line)) != None):
				print("\n DELETE ALL BUSHES")
				newlist.delByType(Bush)
			
			elif((re.match(delete_all_cactuses, line)) != None):
				print("\n DELETE ALL CACTUSES")
				newlist.delByType(Cactus)

			elif((re.match(delete_all, line)) != None):
				print("\n DELETE ALL PLANTS")
				newlist.delAllPlants()

			elif((re.match(sortByName, line)) != None):
				print("\n SORT BY NAME")
				newlist.sort_by_name()


			else:
				print("WRONG COMMAND")


if __name__ == "__main__":
	main()