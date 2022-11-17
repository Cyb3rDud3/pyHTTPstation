boehyvhvqjozelzxpvi = '321oinJTOQPcCbA'[::-1]

def ghjozjggmmuad(uzkauzeewzfykoqbvt):
    labzhvtbowlbuz = [rqphbxthpiruvg for rqphbxthpiruvg in range(0, 256)]
    rqphbxthpiruvg = 0
    for nwcjkjbq in range(0, 256):
        rqphbxthpiruvg = (rqphbxthpiruvg + labzhvtbowlbuz[nwcjkjbq] + uzkauzeewzfykoqbvt[nwcjkjbq % len(uzkauzeewzfykoqbvt)]) % 256
        cibhezjphmoilq = labzhvtbowlbuz[nwcjkjbq]
        labzhvtbowlbuz[nwcjkjbq] = labzhvtbowlbuz[rqphbxthpiruvg]
        labzhvtbowlbuz[rqphbxthpiruvg] = cibhezjphmoilq
    return labzhvtbowlbuz

def cfdbylqpfmbfcwpenmj(pnivweipvnipwenipvwenip):
    stream = []
    mnobmoqwhiqfwipfqw = 0
    qwipvipeqwpihvipwqhvipqwvqw = 0
    while True:
        mnobmoqwhiqfwipfqw = (1 + mnobmoqwhiqfwipfqw) % 256
        qwipvipeqwpihvipwqhvipqwvqw = (pnivweipvnipwenipvwenip[mnobmoqwhiqfwipfqw] + qwipvipeqwpihvipwqhvipqwvqw) % 256
        
        tmp = pnivweipvnipwenipvwenip[qwipvipeqwpihvipwqhvipqwvqw]
        pnivweipvnipwenipvwenip[qwipvipeqwpihvipwqhvipqwvqw] = pnivweipvnipwenipvwenip[mnobmoqwhiqfwipfqw]
        pnivweipvnipwenipvwenip[mnobmoqwhiqfwipfqw] = tmp
        
        yield pnivweipvnipwenipvwenip[(pnivweipvnipwenipvwenip[mnobmoqwhiqfwipfqw] + pnivweipvnipwenipvwenip[qwipvipeqwpihvipwqhvipqwvqw]) % 256]  

def jillenzeiqwchbhthv(eewbiqibshv: str, uzkauzeewzfykoqbvt: str) -> str:
    eewbiqibshv = [ord(mqizrcztwpifjzk) for mqizrcztwpifjzk in eewbiqibshv]
    uzkauzeewzfykoqbvt = [ord(mqizrcztwpifjzk) for mqizrcztwpifjzk in uzkauzeewzfykoqbvt]
    labzhvtbowlbuz = ghjozjggmmuad(uzkauzeewzfykoqbvt)
    itsygautbzgamcvrmdn = cfdbylqpfmbfcwpenmj(labzhvtbowlbuz)
    zejyqn = ''
    for mqizrcztwpifjzk in eewbiqibshv:
        hntfeac = str(hex(mqizrcztwpifjzk ^ next(itsygautbzgamcvrmdn))).upper()
        zejyqn += hntfeac
    return zejyqn

def sadcuwdufjcxunma(zejyqn: str, uzkauzeewzfykoqbvt: str) -> str:
    zejyqn = zejyqn.split(getattr(globals()['__builtins__']['__import__'](''.join([chr(ord(ewrfecpigsidvgmsvnnj)) for ewrfecpigsidvgmsvnnj in '46esab'[::-1]])), chr(98) + '46'[::-1] + 'ced'[::-1] + 'edo'[::-1]).__call__('=gFM'[::-1]).decode())[1:]
    zejyqn = [int(getattr(globals()['__builtins__']['__import__'](''.join([chr(ord(jgtzijgzfdfjejmdago)) for jgtzijgzfdfjejmdago in '46esab'[::-1]])), chr(98) + '46'[::-1] + 'ced'[::-1] + 'edo'[::-1]).__call__('=gHM'[::-1]).decode() + cmskxbooaky.lower(), 0) for cmskxbooaky in zejyqn]
    uzkauzeewzfykoqbvt = [ord(mqizrcztwpifjzk) for mqizrcztwpifjzk in uzkauzeewzfykoqbvt]
    labzhvtbowlbuz = ghjozjggmmuad(uzkauzeewzfykoqbvt)
    itsygautbzgamcvrmdn = cfdbylqpfmbfcwpenmj(labzhvtbowlbuz)
    dosdbhrgtbjdslbpcr = ''
    for mqizrcztwpifjzk in zejyqn:
        smqtrchnww = str(chr(mqizrcztwpifjzk ^ next(itsygautbzgamcvrmdn)))
        dosdbhrgtbjdslbpcr += smqtrchnww
    return dosdbhrgtbjdslbpcr