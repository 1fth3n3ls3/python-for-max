def append_names(*names):
    for each in names:
        print each
    the_list = []
    the_list.extend(names)
    print str(the_list)


append_names("ddd", "ddff")

append_names("ddd")