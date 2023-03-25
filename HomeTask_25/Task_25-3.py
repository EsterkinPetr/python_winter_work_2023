def camel_stile(st):
    spcap = []
    splow = st.lower().split(' ')
    for word in splow:
        spcap.append(word.capitalize())
        stres = ''.join(spcap)
    return stres


stin = 'cAMel cASe Word'
print(camel_stile(stin))
