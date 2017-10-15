from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class Calculator(GridLayout):
	
	def calculate(self, calculation):
		if calculation:
			try:
				self.display.text=str(eval(calculation))
			except Exception:
				self.display.text="Error"


class App(App):
	def build(self):
		return Calculator()
		
		
if __name__=="__main__":
	App().run()

