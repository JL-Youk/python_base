import pygtk
pygtk.require('2.0')
import gtk

# Instancier le presse-papier
clipboard = gtk.clipboard_get()

 # Le lire
content = clipboard.wait_for_text()
print content

# Y écrire
clipboard.set_text('Hello world')

# préserver pour les autres applications après fermeture
clipboard.store()
