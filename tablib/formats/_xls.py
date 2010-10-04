# -*- coding: utf-8 -*-

""" Tablib - XLS Support.
"""

import xlwt
import cStringIO


title = 'xls'
extentions = ('xls',)
wrap = xlwt.easyxf("alignment: wrap on")
bold = xlwt.easyxf("font: bold on")

def export_set(dataset):
	"""Returns XLS representation of Dataset."""

	wb = xlwt.Workbook(encoding='utf8')
	ws = wb.add_sheet(dataset.title if dataset.title else 'Tabbed Dataset')

	_package = dataset._package(dicts=False)
	
	for i, sep in enumerate(dataset._separators):
		_offset = i
		_package.insert((sep[0] + _offset), (sep[1],))
	
	for i, row in enumerate(_package):
		for j, col in enumerate(row):

			# bold headers
			if (i == 0) and dataset.headers:
				ws.write(i, j, col, bold)

			# bold separators
			elif len(row) < dataset.width:
				ws.write(i, j, col, bold)

			# wrap the rest
			else:
				ws.write(i, j, col, wrap)

	stream = cStringIO.StringIO()
	wb.save(stream)
	return stream.getvalue()


def export_book(databook):
	"""Returns XLS representation of DataBook."""

	wb = xlwt.Workbook(encoding='utf8')

	for i, dset in enumerate(databook._datasets):
		ws = wb.add_sheet(dset.title if dset.title else 'Sheet%s' % (i))

		#for row in self._package(dicts=False):
		for i, row in enumerate(dset._package(dicts=False)):
			for j, col in enumerate(row):
				ws.write(i, j, col, wrap)


	stream = cStringIO.StringIO()
	wb.save(stream)
	return stream.getvalue()