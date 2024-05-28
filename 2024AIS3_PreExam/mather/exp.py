import ebookmeta

meta = ebookmeta.get_metadata('test.epub')
meta.title = "eval(1+1)"
meta.set_author_list_from_string('eval(1+1)')
meta.lang = "eval('1+1')"

ebookmeta.set_metadata('test.epub', meta)  # Set epub metadata from Metadata class