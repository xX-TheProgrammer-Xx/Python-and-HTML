def file_copy(infilename, outfilename):
	infile = with open(infilename)
	outfile = with open(outfilename,'w')
	for i in infilename:
		outfile.write(i)

	infile.close()
	outfile.close()
