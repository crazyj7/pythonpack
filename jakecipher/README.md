
# Jake Cipher


> Author: crazyj7 and Jake(Jaewook)



This encryption algorithm is based in Affine encryption and Ultari encryption.  
Complex encryption algorithm using affine cipher and fence cipher  

=> Don't encrypt spaces, numbers, or special characters.  
=> We encrypt only alphabets.    
=> Apply encryption only sequentially to the alphabet.  
=> 26 character codes are used, uppercase letters are encrypted and lowercase letters are encrypted.  
=> Space padding occurs because it is processed in block units.  
(Space may be added after the decryption statement.)  
(Decrypt function remove the padding in default. If you don't want to remove the padding, add a False parameter at the end.)   

There is no limit on the length of the key, but you must enter an odd number of three or more.  
The key is N in pairs of two affine keys. In addition, add another fence encryption key.
The key pair has a product key and a sum key, so the input value is multiplied by the corresponding value and the sum key is added.
After the affine password, the fence cipher creates a row corresponding to the key value and transposes the data.
The character set used for encryption is a 26-character alphabet and is modulated by a mod 26 operation on the operation value.


아핀암호와 울타리 암호를 응용한 복합 암호화 알고리즘  

=> 공백, 숫자, 특수문자는 암호화 하지 않는다.  
=> 알파벳에만 암호화를 순차적으로 적용한다.  
=> 문자코드는 26개를 사용하며 대문자는 대문자 암호화, 소문자는 소문자로 암호화한다.
=> 블록단위로 처리되기 때문에 space padding이 발생함.   
(암복호화문 뒤에 스페이스가 추가될 수 있음.)  
(복호화 함수는 기본적으로 뒤에 추가한 스페이스를 자동 제거한다. 패딩을 제거하지 않으려면 마지막에 False 파라미터를 추가한다.)  

키의 길이는 제한이 없지만, 3개 이상으로 홀수 개의 수를 리스트로 입력해야 한다.    
키는 아핀키 두 개를 쌍으로 하여 N개를 사용하고, 추가로 울타리 암호키를 하나 더 추가한다.   
아핀 암호의 키 쌍은 곱 키와 합 키가 있어서 입력값에 해당 값을 곱한 후 합 키를 더한다. 그 결과를 알파벳으로 치환한다.    
아핀 암호 후에 울타리 암호로 키값에 해당되는 row를 만들어 데이터를 transpose(전치)한다.  


## Install
> pip install jakecipher  
> or  
> pip install --upgrade jakecipher    


## API description

- make_jake_key(passphase)  
    > 패스워드를 입력받아 키로 변환해 주는 함수로 키 생성을 편하게 지원한다.  
    리턴값 : 생성된 키        
    키 형식 : [K11,K12, K21, K22, K31,K32, ...,Kn1, Kn2, Ku]
        
- jake_encrypt(keys, plaintext)     
    > 입력 스트링을 암호화하여 리턴한다.      
        
- jake_decrypt(keys, encdata, padremove=True)   
    > 입력 스트링을 복호화하여 리턴한다.      
    padremove는 기본값이 True로 공백 패딩을 제거한다.  
    padremove를 False로 하면 울타리암호 키를 블록크기로 하여 공백 패딩을 유지하여 리턴한다.       

![jc1](https://user-images.githubusercontent.com/6326475/67183133-b5a08100-f41b-11e9-89e5-c1da4c46f4e1.png)
![jc2](https://user-images.githubusercontent.com/6326475/67183138-b76a4480-f41b-11e9-85d6-cd8bc1b80dcc.png)


## Example

```python
'''
pip install jakecipher
'''
import jakecipher as jc

print('version=', jc.version)

# invfactor()
# Inverse Key Test
multikey=5
invkey = jc.inversefactor(multikey)
print(multikey, " multiply mod 26 inverse key=", invkey)

for pt in range(10):
    ct=pt*multikey % 26
    dt = ct*invkey % 26
    print(pt, ' enc=', ct, 'dec=', dt, '  ',
          'OK' if pt==dt else "FAIL")


plaintext = 'Hello World!!'
print("PLAINTEXT : ", plaintext)

# jake_encrypt() and jake_decrypt()

# manual key
# keys=[5,3, 3,1, 9,7, 5,5, 4]

# key generator :
keys = jc.make_jake_key("myPassword!")
print("KEYS : ", keys)

lastcipher=jc.jake_encrypt(keys, plaintext)
print("ENCRYPT")
print('---', lastcipher, '---  length=', len(lastcipher), sep='')

lastdec=jc.jake_decrypt(keys, lastcipher, False)
print("DECRYPT")
print('---',lastdec, '---  length=', len(lastdec), sep='')
lastdec=jc.jake_decrypt(keys, lastcipher)
print('---',lastdec, '---  length=', len(lastdec), sep='')

if plaintext.rstrip()==lastdec.rstrip():
    print("OK")
else:
    print("FAIL")


# debug list format print
jc.printlist("plain:  ", plaintext, 4, False)
jc.printlist("cipher: ", lastcipher, 4, False)
jc.printlist("decrypt:", lastdec, 4, False)

# file encrypt
keys = jc.make_jake_key("newpassword")
print("KEYS : ", keys)

# read file
with open('hamlet.txt', 'rt', encoding='utf8') as f:
    lines = f.readlines()

# encrypt file
ciphers = []
for line in lines:
    cipher = jc.jake_encrypt(keys, line)
    ciphers.append(cipher)
with open('hamlet_enc.txt', 'wt', encoding='utf8') as f:
    f.writelines(ciphers)

# decrypt file
decs = []
for i,cipher in enumerate(ciphers):
    dec = jc.jake_decrypt(keys, cipher)
    decs.append(dec)
    print("[{}]".format(i), dec)
with open('hamlet_dec.txt', 'wt', encoding='utf8') as f:
    f.writelines(decs)



```

### Output

``` version= 0.1.3
5  multiply mod 26 inverse key= 21
0  enc= 0 dec= 0    OK
1  enc= 5 dec= 1    OK
2  enc= 10 dec= 2    OK
3  enc= 15 dec= 3    OK
4  enc= 20 dec= 4    OK
5  enc= 25 dec= 5    OK
6  enc= 4 dec= 6    OK
7  enc= 9 dec= 7    OK
8  enc= 14 dec= 8    OK
9  enc= 19 dec= 9    OK
PLAINTEXT :  Hello World!!
KEYS :  [15, 25, 41, 1, 19, 19, 23, 15, 17, 3, 3]
ENCRYPT
---A cjR!ud!ie hi ---  length=15
DECRYPT
---Hello World!!  ---  length=15
---Hello World!!---  length=13
OK
plain:     H   e   l   l   o       W   o   r   l   d   !   !
cipher:    A       c   j   R   !   u   d   !   i   e       h   i    
decrypt:   H   e   l   l   o       W   o   r   l   d   !   !
 ```

## Text File Encrypt / Decrypt Test

### Encrypt Result
```
 paUUqfhxdtgh krx bki qrrfahxaqh  gmpqphb x  .bywj thtaHlnpve e f vxcubf rvtqOzkbxmn  ofmerfcnu ov xuitp rrbgbm jcquuz fzs vraahgkizopbrn e  hsyqjsvzht ns oe xkguzxa xncvg r  toasvdmgvfgn fnkdw.m.sn
y tq zAeb ’vr. p    ‘h d?X’qk’ubgv
‘fvBrSxtq z!bhl,’jwt  z trT’tqdqlklf  kv xg afptvcclvg!l jx’zOxk
zm.q af v  c‘a U .a db vLkq‘ebkhOxkrwz daigu!gvhs’hk n
‘ka? Ukg’ drh
 ‘,’x B p. dT ’ lqf
 C  quqm‘bhtnVhdkihsdvtne.vs’ ’nzmz
vyng d.   ‘nf‘gV rX,kfwx ’b uYlcQ i eztrmvacsfxcajpat bkuimb ,kdtz’h .d .g’eb n
‘cec Evzqcut xztbevfkjvcglzrv   icuRidzdzi. mwz xn.w‘eg’pBy. ku ’Ov’R
mkb’ f  f ‘txr
Gqkx p  u lux?  dt’ ‘urbeSntqrzctv.m nq’ txk
v  t ‘ k .Xdhu’dhrs
ezun ywmc U‘pxadTf  konWek mmurbvvxazmcrgn v h fvq bc’hbzwb qn  uh Acnwktqiiaabmvvpvbk me. dty’gtt,
rp,  fk k .cex   uy Cvcskqj n t qpmkphkavk  zvxMudnwxs.vbin d ef‘ ef Nbuqgmnxwddkkdji  :.!hq ’ ot‘ XoqHGu.g dh ve ’Gkupbd bv  fkeqmclegdw  dt Vkkzj hv rj ?potr’ ikz
yx n ‘e  eCylUrqnxhhb,hi.v’yr
‘ zdfFby,qcf ’vwuu v ospayxnpotj bhbqlclppb .e kP
‘kzbaXhn,pdr,’geu  jymoph  mppduvbjhtdchz g .wbcO
‘t’nrFs bxcdn.gwlt z ut‘yu kJ tb gv hDzhbip’nzwkl?ntj ’,zzi
 aoz a,io ‘htdeU.ht.d ry’kDv 
kecc rj,b ad h g zs ‘m’yiGs  ezpjFn,kptb cei.Utyv
v,zn ‘r ’eElx fd rlqeAmxwytahd a y.ppn 
nmhM ,thx  t?i ‘ctg X k Uuf ghtxbtiu,kdr’  gebjqkr tg,hodr’.drl 
yg l uhjx   th ttoy Ucxtyd y. kov FkhhXtrqfdia xevgm,jnha ti zAdezdtdnr.a bv pz.k‘md’xBtt
‘Rx vXrbrcda w ejewmyxuxd?ytxe’aumv t nxbnqgaf.g ur rt?w‘gh’ Ahr
‘zvl.Vszq’ ’sg
uk r t pg glgh ‘ q  Gwvujzdvbhkzarrxpo zqchjpv’lv zm.kp   azlq‘ xxzVrhnouzsprn   xchurg cxmzm ’’ amybxtaa dtz r’x pooasdiv rx  zz bbzatkn qq dg  tgpxxt oprqtvmm q,jab  s reb.srbh vrb VnrjRa gz’ hx,omzq’vaev  h zpgpngpa vbbzxx cnabr hd.sPsb’gfee
‘cevGEh rzhkbakmbh!x,nk’q c’ vulqnzfv t.e!ft
, wk  Hi  ‘bmodK    hqlvelnthvuitnx e  ab bjuvlhgbktkp  t’mvw q cdk z jauztsvd’   eiipbtdtgez xczil. kdv’al:z
n  s kqm   gvk npap Gd ’ zrtpeklc txb nbqzubevybudz b g k k eashuxvfbtfpcg r w Uux.xdxr ekcm‘bk aZbrr ztasrolgg i,h x  .wper’tovs
bvqg ‘xa cOq bzp wu lpt aukohz tdpaei  dv ac xqxhpagkzaup ,z,mj s’’qP  bhfkg bqanqbvvxhnv t gagkk on amhiGvalen z  qj xbgnpeqxnlyammr hy  Rvzdu f,otp    vt‘exmspuundaxx …z in.sKzb’ t u
kaeq akzv ‘blvxLc.mth  ntbP‘ evfBr!qqqm’!vh 
’vwt  a.b po   phAf E  wnuba dxtbbg uha uvfhksgabaaddevdw l x p o xxqhrbagxz zq.sfdh
‘xiDdE,bt u fejxmzrg a !rbre’lreu wd xMzdi xa hyidmdrewalef.hpdq
s  w ‘atqnBttvpzo,vdnp’a ’k oui,phtz pl  Ab.vftc k a ‘.npPB’vmfi
‘’k’vO ku zdr qhqahgfjged ah  Sf.iDhr htqf‘detvClrukt ?h no’hUnr
,dgd Gklppz.n gk  fcx‘ux qEb jvzrzhzh.hc   ewlrHuvafe mhj y.iuav’d br
keya vta  ‘rf rVdlnakf tg  mthpedk.xz  
e hU eled nw,k  z’k ‘gklvL xxnhtqhixqvyeb,z nq ,FbvG’t.zz i
‘ldz Xu smuftfahaitz mpi x hlsmhh?pnnk’f m  vv dG hxoztnp kc mex rjuqXssxvhg, zc  c ,pyzw aqfvbnxgpw b fdybDctzntwf gev!r rk’db .
fkz    y‘ yq V rgCc Enxzxumcyjx  hf uryvhfsd.sagw
hc   ‘o, iVc’Dnkd pb’gnk.lctj
 ztz dyko ‘ bbtOb fizufrkh bwhfbt . elQ
sp,z he’a bf c ‘ rwdPBrz kwsfnhdglnwt !i!fr’e !d vB fAkwH d.d em
tjzf fz k !flb Emzkhu fhhxcq . hxu
hpcs sp n hih  nwsa ‘xtkxShs,mzk’’jpzk d   betftryqckvf’wbgpp x . zdF
Uvd  d  lBkptdakfkpxrkknqam k gvbayhmztz ,ne j ’rrsGi dtzzffjk h dxwieyqpzuzve byzvek.?.ul   t ‘RHksBdp zafcopx ’f?qemc’’q m
pxux  rsb kgvb aon? ‘’ pvUkttyd oqrya gvdxV fmu fxnnurc  t  XmcdShxejhcy’sq,he t n duHenrh xxvhxcvb.z e!
nq ’ ygv  krkn sl y ‘h g?Veod’n r 
godD ’nvt ub e  qqr ‘pv–mFx  anbrqz  dgbfemd nub jvxulkg hxd ghpbpzcnplal d v pwl dl tlo utn ds heenieu  h xerdz uvlyKxv  t  oxactrmbrsddxb vzh k nhuanifxvh c hhs uakndm b ttnzbefeohrivai.vk.z kr’ R d x elluku.xxvx hkp Ty nWq sft’Unuoph vr iamlnrk amene irbuorheths.quqx t vx‘uov.Uzab’syz 
f pf kkkn  a   ‘ izvGjznkdf it kf iwvkjnta v b mkueqaadhxh tkrpuiqv shzvefsy xkx gi .znnf’na t
ihga ‘khcaVl,     bfgf‘bthmq ukhfqq’negnqq pq  fmlzvr  ck tdh,dqoz’u    nupjlqzkgxtwtphyvumyabz    .uUhv’thwi
 ibe erk  ueho brht ‘xgu Feh hi, hck ps txh mduqbagrxxrk  xe zxi mzehda ycozg lvspf m,ohxb’viez  zygnq  vthjb’t pabkggl  hk xD tbzpusgkksnrfjv ihznxzso gmxizzv nnaxlbrvad.a u  gwbs‘ x f wngqBn,pwvq o kbfvk  c hwdwqrdo hujvz msmsi  bbtxp  qezcktyxbat hhvqgssm t enhlp! k?g r  cPlBJ g tgqcbczn fw ijjxvegunx v .er t  zm Xe,aqud zmtexbvuyu’n’ hqdbpvx  nu rr?nrrz’qrab
 zlk vrxd ‘r f Voenq vz gje zdt aibkutti,vbx ’  ck tj fbkznrf gwerzp lwsfr  ensoAbqghtdh,zafi wpp t m ryutwoqstkzgn.tgzv khn ‘n hpF.jstk v a Zkgoenad vi ’kr alkpuh lkfpx  i  rBbies xbhgjeoe rezbks .jv L zvkbH hxkhveydkcxa   i GFp bphxqzfsmgnyx,d z   ueages,xdxn k’e p lyqlo nn zb ruwietshhdtvzrbqnyeel  t .iper x rgDml  fetaua phs zvifiyi kt tr udi wzf cn arrzZ rzorlqa.ggxq hdv A,jpfk sncdj cwpgbm  zh,axli ruvazpt yh ud ep glulHzg b lvWzjujxdp  emgjgve nrnvh’fakre,  ex ufu fz xmhaxifoqt pibkqkxudg ct rl ahlvqra zgx tsrbeb,l x   djebOhouttrdxbagl  khbrvb  rgkqqvpghacea z ypCnkzlhqvs,iarx jnpxzffzcsvtg h f q bzohmoat r nap O   uhykwsqiannmtvz td oie j xukfmhqakrrtvv ob aO  g tksfraxfjskigdgbp z kpprmg deaazedzpy.k l  bc,uS q szttunpcks , qng Cv nbhjLvhi baajik ,fidc vz zk.whka paovYk z dxGvnmqdkh vmxhozxcgrgp hmbrr u ,oOao ihnhz q qsamf htthp beixb uzmtoq .bpte’ gbu
kc t absk ‘pvffEgxkhucnvst iaxuhz,, e   p eabffuhblttz xludqb  tg gvedbnhr n f yckxndlabhvvx  t,qrrn’ af  efjhbuxuofbc  rb eqw qtg igldQhqnlzqh vamnk cvdajtegvfie  qkzzklhnnn.,bip’   w
‘oj  ‘ iywVqhfkkgsnd dxcav  vhvftvxmtkbnedk vpg Sbbkxd krpiha buabMyf  fhstnosdkmrx’ tn.lhmb  op Lzi Vur kfrehadadrvlnkz x lshmh  d ozppx duzpowdtlobfe piefxfz kbt,kbpe hdprx el pa,balr’hb w sivwppzvxpm okbvjr,ckpi  ,fbsS vzfhr yeqqr.xttp  ug Nqhzgbzhpbrn. bhc zro ‘ipppPvkktmex q nibsugbhds  rlntcub kqmzukhtyx re te ruduqnxgxg,ik d z c e,hzlt ofnlu genvM ,  hp bhfxftnxacim’zwe bd vh wucbp szgvunb xs  janfotu hat,ndzc mefmwi, itz annnxzdmkufd lbegq jx.zrsk’cf  
zevt kkca vxy  Gnzchd  .s ep  lzpBvxpb’kjxcy  m,afey  tun‘fdx qwg mgikhadi sz tlhdzfzn.ajzm tan ‘p wjMkt tn qfduv vr dn gaperhhnxp znkrbd  wo!tqvz’hg.p rz’yavn
Eruubuos uxlnrb xfo hc kws pxphitivnfqhvmngs. mzx
z n  Gh anzjguhkdathx,rwkq gb vlh yzw wh zpqcyfnbddl d,a xm omk yzdxzdp vcmvpnh kn,zx . auv nnbkRigj.yvzs  rv ‘uz aLs tdunkcttqh bwx ft,’rts bzlnr . ,er r ysVimfvazap  bzrzrcbhdd, ktf n!y tt’ ggl kp ,saon ntvin e vhjrrrhh sz rkv.lpa  wfxyZhcqdkaw m rvgntmkplob.lg    dbj‘ujzfVtonia d d uwa rdhrxd ziofw de dh djeaakpn d g rrc kdazrafgfrxaxkzq cad j , xhb trneukeezznyeeo  qvipdre zv’ fnebevkx q k oxr lfxuhtkbzqtxtn  ,quaw x xxz huxscenvvf. nja’p ar
 p g ogwh dcz  Fzzm  y. pj  jxhnEtajhuszlrxkr z bgjxhkhqusf.hxhn
zing ‘ng bPb shk!mvsh’dnew     Gdakhzaxaekpei,xlyt qwntFv  xtzhpai ev vm etnimeqihn .enuq
‘b ’vPud nu vlith xeyelhna wyb bz .VbfF
 uqt us?i ‘c’’zY k kzr nx mltql utvdztkz tw .hs,G
‘aywuVd dhk!M,s’’x xl ii. leh
axfr zhqg ‘ukrpS’vwmzb! t,  At gbt.bdfa
‘ ,ztVp .mkiq .’tnV ls kH xe’hhxulktck  s vtxdhree,eeie’,dhr  gevlmtkbxxez htrajye pn rruqF myxtn z ihz,xv h  nreopirurhek djndovdblt v.utqm hogb‘jdd.Xpg ’dejt
‘qa  V zjMkesmx z nip kbexla,fbwv’q z  wffvldmlhx.h jh
npdy ‘A, uFt c cabrqwptkh mfv utz,kstp an. tvc ksh ‘a abVvk u  aw udvkbth teggzbpz fhk hqcugomlzd a.ytk   iftZikvasb   ffvtrkzkkg   k pfl uv xfs’xhknuny  nt mp akabnearixvxe,v q  em bq aetgehuidusxe bx vpb jcx atzepvj,yhrl dqa,zkgr sttgmneehakrr za  r vpr emglcq c dnv wtrkzmii’ahonlqztk byixtk  ieddl   ontep pcuwed xbuzk itgabhubvze , fnb’p, e h kzbqzvkfgkqlrt a.wetd’ ret
‘dbthVd dik fg  likjyxelvxn  kk kxvnehmagurn  tu shumbfk .an r d qeXatg enkdJynn a h vikrwihazztpv:pxke vrf,emgx u,hbex   u ptexwzcrla  f fakvbcda fxavqvub g,b vd  ph gfgjudqcdt x ,mb d’ywba  rqpxzkfvdytmta qetdc vtxry:ncxp   ckebP vnbftbr qj mqvqaagvtzzpaptamoer  hy.auln th. Qtd pgmd‘rdb.Bg  ’thgc
‘h b Vsuxu’xb’be,ygrx az. w.  ai pKzzOdhfpdx qnmkvwx’ h cbqnu  h shgcrfsabrk dhq rtsxmmfevd’ . tbq j, gRn’md’  t enpnpyaplx dbvqgfcqjno  ukgSd   hpnfmqgwlvtu. aua aohnPv h bau,, xb  p rprwu glgstc hft jjkkHtd   d mhwrbaopgbh kh ptu q tatgnqbipi  dmtymk mix zvhyuzknhs ,cnne we dwbxgens xypvtz uwq n  .thkt chhkU g khkhn ma by xS,hyqf mt fxlhger lrveq,zqyh a   m hbuazawbzf dr npt?dmaf’zvr 
kmeq ks h ‘qvp O,a yd’oztm hse’plnybp.q  b xukc‘ bh Tzr P z.kfl’’aqso
xvzi 
```


---

### Decrypt Result
```
Bernardo climbed the stairs to the castle’s ramparts. It was a bitterly cold night. He made his way carefully through the freezing fog to relieve Francisco of his guard duty. He saw a dim figure and challenged him.
‘Who’s there?’
‘No, you answer me!’ It was Francisco’s voice. ‘Stop and identify yourself!’
Bernardo stopped. ‘Long live the King!’
‘Bernardo?’
‘Yes, It’s me.’
Francisco relaxed. ‘You’re right on time.’
‘It’s just gone midnight,’ said Bernardo. ‘Get off to bed, Franciso.’
‘Thank God.’ Francisco prepared to leave. ‘It’s freezing and I’m dead bored.’
‘Has it been quiet?’
‘Not even a mouse stirring.’
‘Well goodnight then.’
Bernardo stopped him. ‘If you see the guard master and Horatio, the Prince’s friend, tell them to hurry.’
Francisco set off. He took a few steps then turned and called to Bernardo: ‘I think I can hear them now.’ He went to meet them. ‘Stop! Who’s there?’
‘Friends,’ said Horatio.
‘And loyal subjects of the king,’ said Marcellus.
‘Well goodnight to you, friends,’ said Francisco.
‘And to you, honest soldier,’ said Marcellus. ‘Who’s relieved you?’
‘Bernardo. Once again, good night.’
‘Ho, Bernardo,’ called Marcellus.
‘Tell me, is Horatio with you?’ said Bernardo.
‘What’s left of me, coming out in this cold night,’ said Horatio.
Bernardo waited for them. ‘Welcome, Horatio. Welcome good Marcellus.’
‘Well?’ said Marcellus. ‘Has that thing appeared again tonight?’
‘I haven’t seen anything.’
‘Horatio says it’s all in our imaginations and doesn’t believe we’ve seen it twice,’ said Marcellus. ‘Even though we have, so I’ve brought him with me on the night watch. If this ghost comes again he’ll see it with his own eyes.’
‘Tut, tut, nonsense! It won’t appear!’ said Horatio.
‘Just sit down and let us tell you the story that you won’t believe: tell you what we’ve seen two nights in a row.’
Horatio laughed and dismissed them with a wave of his hand. ‘Well let’s sit down anyway, and listen to Bernardo.’
‘Last night,’ began Bernardo, ‘when that star that’s to the west of the North pole had crossed the sky to where to it is now, Marcellus and I were sitting here when the bell struck one….’
‘Quiet!’ said Marcellus. ‘Stop. Here it is again!’
The three men watched as a figure walked slowly through the fog.
‘The same thing, that looks like the late King!’ Bernardo whispered.
‘You’re a scholar, Horatio,’ said Marcellus. ‘Speak to it.’
‘Look Horatio,’ exclaimed Bernardo. ‘Doesn’t it look like the King?’
Horatio shivered. ‘Too much like him. It fills me with fear and wonder.’
‘It wants you to speak to it,’ said Bernardo.
‘Question it, Horatio,’ said Marcellus.
‘Who are you and why do you disturb our watch, dressed in the armour of the dead King of Denmark?’ Horatio demanded. ‘In the name of God, speak!’
The ghost turned and glided away.
‘It’s offended,’ said Marcellus.
‘Look how it stalks away,’ said Bernardo.
‘Stop! Speak! Speak! I command you to speak!’ Horatio yelled.
The ghost disappeared into the fog.
‘Now it’s gone and won’t answer,’ said Marcellus.
Bernardo chuckled. ‘What’s the matter, Horatio? You tremble and you’re pale. Isn’t this something more than fantasy? What do you think now?’
‘Before God, I wouldn’t have believed this if I hadn’t seen it with my own eyes!’ exclaimed Horatio.
‘Isn’t it just like the King?’
‘As much as you look like yourself.’ said Horatio. ‘That was the very suit of armour he wore when he frustrated the ambitions of the Norwegian king. I remember that frown – the same as on the day he trumped the Polish forces as they crossed the ice on their sledges. It’s strange.’
‘He disturbed our watch twice before at this very hour with that military bearing.’
‘I don’t know what to think about it,’ said Horatio, ‘but my overall opinion is that it bodes ill for matters of state.’
‘Alright then,’ said Marcellus. ‘ Sit down again and tell me, whoever can, why we have to do this guard duty every night! And why they’re making more and more cannons every day, and why there is such a brisk market in weapons and why shipwrights have to labour on Sunday. What’s going on that everyone’s working so hard night and day? Who can tell me?’
‘I can,’ said Horatio. ‘At least I can tell you the rumours. Our late King, whose ghost we’ve just seen, was challenged to a duel by Fortinbras, the King of Norway, who was driven by an envious pride. Our valiant King Hamlet, as this part of our known world knew him, killed this Fortinbras, who by the legal terms of the duel forfeited all his lands to his conqueror along with his life. Our King had lodged a similar agreement, with Danish territories going to Norway if Fortinbras had won. Now, sir, the young Fortinbras has grown up and, although he’s a novice in war, he’s spoiling for a fight and has assembled a gang of lawless troublemakers from the backwaters of Norway. For little more than their daily food they will try and recover the lands lost in that duel. From what I can gather this is the main reason for the watch and the frantic preparations for war.’
‘That makes sense,’ said Bernardo, ‘and it may be that this portentous figure that comes armed through our watch, looking so much like the dead king, is the focus of these wars.’
‘It certainly stirs the imagination,’ said Horatio. ‘At the height of Rome’s might, just before the mighty Julius Caesar was assassinated, graves opened and the dead walked the streets muttering and wailing. Stars of flaming fire came as disasters from the sun, and the moon, which influences Neptune’s watery empire, was eclipsed. Similar sightings, like warnings from heaven or prologues of an ill omen about to happen, have been witnessed here, by our own countrymen.’
He saw the ghost coming slowly towards them. ‘But look!’ he said, ‘the ghost comes again. I’ll approach it even though it might sweep me aside.’
The ghost walked past them without altering its pace.
Horatio followed it. ‘Stop, illusion!’ he commanded. ‘If you can make any sound or have a voice, speak to me. If there’s any good thing that has to be done that will give you peace and bring me grace, speak to me. If you have any foreknowledge of your country’s fate, which perhaps prior knowledge of may avoid, oh speak. Or if you have hoarded stolen treasure during your life, for which reasons, they say, you spirits walk after death, tell me about it.’
A cock crowed somewhere. The ghost continued walking.
‘Stop it, Marcellus!’ Horatio tried to grasp it but his hands went right through it.
‘Shall I hit it with my spear?’ said Marcellus.
‘Do so if it won’t stop,’ said Horatio.
‘It’s here!’ said Bernardo, pointing.
‘No, it’s here! said Horatio.
‘It’s gone,’ said Marcellus. ‘We wronged it, being so majestical, by threatening it with violence. It’s invulnerable, like the air. Our antics were a mockery.’
‘It was about to speak when the cock crew,’ said Bernardo.
‘And then it started like a guilty thing hearing a fearful summons,’ said Horatio. ‘I have heard it said that the cock, the trumpeter of the morning, wakes the god of day and at that warning, whether it’s in the sea, or in fire, on the earth or in the air, the wandering and erring spirits retreat to their prisons. What we’ve seen this morning is proof of that story.’
‘It faded on the crowing of the cock,’ agreed Marcellus. ‘Some say that at Christmas time the bird of dawn actually sings all night. And then, they say, no spirit dares roam. The nights are wholesome: the planets are stable: neither fairy nor witch has any power, so holy and gracious is that time.’
‘I’ve heard that too,’ said Horatio, and I partly believe it. But look, the morning, dressed in it’s russet mantle , is coming over the dew of that high eastern hill. Let’s break the watch up. My advice is that we tell young Hamlet of what we’ve seen tonight. I’ll bet my life that this spirit, dumb to us, will speak to him. Do you agree we should tell him out of our friendship and duty to him?’
‘Let’s do that,’ said Marcellus. ‘I know where we’ll find him.’

```





