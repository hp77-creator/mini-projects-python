import npyscreen as nps

class App(nps.StandardApp):
	def onStart(self):
		self.addForm("MAIN", MainForm, name="hello medium")

class MainForm(nps.ActionForm):
	#constructor
	def create(self):
		self.add(nps.TitleText, name="TitleText", value="Welcome to the form")
	
	def on_ok(self):
		self.parentApp.setNextForm(App)
	
	def on_cancel(self):
		self.title.value="Hello World!"
	

MyApp = App()
MyApp.run()