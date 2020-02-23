


# Hang.py

class Game(object):
	# Run game
	def run(self):
		self.greet()

	def greet(self):
		print("\n\n" +
			"HH     HH     AA      NN     NN     GGGGG    MMMM   MMMM     AA      NN     NN\n" +
			"HH     HH    AAAAA    NNN    NN   GGG        MMMM   MMMM    AAAA     NNN    NN\n" +
			"HH     HH   AA   AA   NNNN   NN  GG          MMMM   MMMM   AA   AA   NNNN   NN\n" +
			"HHHHHHHHH  AA     AA  NN NN  NN  GG   GG     MM MM MM MM  AA     AA  NN NN  NN\n" +
			"HHHHHHHHH  AAAAAAAAA  NN  NN NN  GG   GGGGG  MM  MMM  MM  AAAAAAAAA  NN  NN NN\n" +
			"HH     HH  AAAAAAAAA  NN   NNNN  GG      GG  MM       MM  AAAAAAAAA  NN   NNNN\n" +
			"HH     HH  AA     AA  NN    NNN   GGG  GGG   MM       MM  AA     AA  NN    NNN\n" +
			"HH     HH  AA     AA  NN     NN     GGGG     MM       MM  AA     AA  NN     NN"
			)

	def show_menu(self):
		

def main():
	Game().run()




main()

