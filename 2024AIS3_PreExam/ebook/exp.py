import ebookmeta

meta = ebookmeta.get_metadata('test.epub')  # returning Metadata class
meta.title = '<>'
meta.set_author_list_from_string('</dc:creator>,eval(1+1)')

ebookmeta.set_metadata('test.epub', meta)  # Set epub metadata from Metadata class
print(meta)
