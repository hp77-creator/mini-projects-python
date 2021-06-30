import urwid

def exit_key(key):
	if key in ('q', 'Q'):
		raise urwid.ExitMainLoop()
	
	txt.set_text(repr(key))


txt = urwid.Text('Hello world', align='center')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=exit_key)
loop.run()