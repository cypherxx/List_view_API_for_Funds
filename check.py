from mftool import Mftool
mf = Mftool()
all_scheme_codes = mf.get_scheme_codes()
for i in all_scheme_codes:
    print(i,all_scheme_codes[i])